#!/usr/bin/env python3
"""Report HTTP availability; never validate source contents or compatibility.

Only response headers are inspected. HEAD is retried with GET for HTTP 405/501;
GET response bodies are neither read nor stored. Network failures and access
restrictions are inconclusive. A valid input produces exit status 0, including
when a referenced URL returns HTTP 404 or 410.
"""

import argparse
import http.client
import json
import socket
import ssl
import sys
import urllib.error
import urllib.request
from collections import Counter
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urlsplit

ROOT = Path(__file__).resolve().parents[1]
TIMEOUT_SECONDS = 10
MAX_WORKERS = 4
CLASSIFICATIONS = ("reachable", "unavailable", "indeterminate")
USER_AGENT = "WLangageResearchLinkCheck/1.0 (headers only; advisory)"


def classify_status(status):
    """Distinguish a disappeared URL from a restriction or temporary failure."""
    if status in (404, 410):
        return "unavailable"
    if status is not None and 200 <= status < 300:
        return "reachable"
    return "indeterminate"


def allowed_url(url):
    """Do not authenticate, accept userinfo, or follow non-HTTP redirects."""
    if any(ord(character) < 32 or ord(character) == 127 for character in url):
        return False
    try:
        parsed = urlsplit(url)
        return (
            parsed.scheme in ("http", "https")
            and bool(parsed.hostname)
            and parsed.username is None
            and parsed.password is None
        )
    except ValueError:
        return False


class PublicHTTPRedirectHandler(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, request, response, code, message, headers, newurl):
        if not allowed_url(newurl):
            raise urllib.error.URLError("unsupported_or_authenticated_redirect")
        return super().redirect_request(
            request, response, code, message, headers, newurl
        )


def request_headers(opener, url, method):
    """Close responses and HTTP errors without reading their bodies."""
    request = urllib.request.Request(
        url,
        method=method,
        headers={"User-Agent": USER_AGENT, "Accept": "*/*"},
    )
    try:
        with opener.open(request, timeout=TIMEOUT_SECONDS) as response:
            return {
                "method": method,
                "status_code": response.status,
                "final_url": response.geturl(),
            }
    except urllib.error.HTTPError as error:
        result = {
            "method": method,
            "status_code": error.code,
            "final_url": error.geturl(),
        }
        error.close()
        return result
    except (TimeoutError, socket.timeout):
        reason = "timeout"
    except urllib.error.URLError as error:
        if isinstance(error.reason, (TimeoutError, socket.timeout)):
            reason = "timeout"
        elif isinstance(error.reason, ssl.SSLError):
            reason = "tls_error"
        else:
            reason = "network_or_redirect_error"
    except ssl.SSLError:
        reason = "tls_error"
    except (OSError, http.client.HTTPException, ValueError, UnicodeError):
        reason = "network_or_url_error"
    return {"method": method, "status_code": None, "reason": reason}


def check_url(url):
    if not allowed_url(url):
        # Do not echo possible URL credentials into logs or the JSON report.
        return {
            "url": "[URL invalide ou contenant des identifiants masquée]",
            "classification": "indeterminate",
            "reason": "unsupported_or_authenticated_url",
            "status_code": None,
            "attempts": [],
        }
    # No cookie jar, password manager or authentication handler is installed.
    opener = urllib.request.build_opener(PublicHTTPRedirectHandler())
    attempts = [request_headers(opener, url, "HEAD")]
    if attempts[-1]["status_code"] in (405, 501):
        attempts.append(request_headers(opener, url, "GET"))
    final = attempts[-1]
    status = final["status_code"]
    return {
        "url": url,
        "classification": classify_status(status),
        "status_code": status,
        "reason": final.get("reason", f"http_{status}"),
        "final_url": final.get("final_url"),
        "attempts": attempts,
    }


def load_urls(path):
    content = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(content, dict) or not isinstance(content.get("references"), list):
        raise ValueError("La bibliographie doit contenir une liste 'references'.")
    urls = []
    for index, reference in enumerate(content["references"], start=1):
        if not isinstance(reference, dict):
            raise ValueError(f"Référence {index} : objet JSON attendu.")
        url = reference.get("url")
        if not isinstance(url, str) or not url:
            raise ValueError(f"Référence {index} : URL textuelle non vide attendue.")
        urls.append(url)
    return len(urls), list(dict.fromkeys(urls))


def nonnegative_integer(value):
    parsed = int(value)
    if parsed < 0:
        raise argparse.ArgumentTypeError("La limite doit être positive ou nulle.")
    return parsed


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--input", type=Path, default=ROOT / "data/bibliographie.json",
        help="Bibliographie JSON à consulter (défaut : data/bibliographie.json).",
    )
    parser.add_argument(
        "--limit", type=nonnegative_integer,
        help="Vérifier au maximum N URL distinctes ; 0 n'effectue aucun appel.",
    )
    parser.add_argument(
        "--output", type=Path,
        help="Écrire le rapport JSON à ce chemin, sans corps HTTP.",
    )
    args = parser.parse_args(argv)
    try:
        reference_count, urls = load_urls(args.input)
    except (OSError, UnicodeError, ValueError) as error:
        print(f"Bibliographie JSON invalide ou illisible : {error}", file=sys.stderr)
        return 2
    selected = urls if args.limit is None else urls[: args.limit]
    with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
        results = list(executor.map(check_url, selected))
    counts = Counter(result["classification"] for result in results)
    report = {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "kind": "advisory_http_availability_not_content_or_compatibility_verification",
        "input": str(args.input),
        "reference_count": reference_count,
        "unique_url_count": len(urls),
        "checked_url_count": len(results),
        "limit": args.limit,
        "timeout_seconds_per_request": TIMEOUT_SECONDS,
        "max_workers": MAX_WORKERS,
        "response_bodies_read_or_stored": False,
        "statistics": {name: counts[name] for name in CLASSIFICATIONS},
        "checks": results,
    }
    if args.output is not None:
        try:
            args.output.parent.mkdir(parents=True, exist_ok=True)
            args.output.write_text(
                json.dumps(report, ensure_ascii=False, indent=2) + "\n",
                encoding="utf-8",
            )
        except OSError as error:
            print(f"Rapport JSON impossible à écrire : {error}", file=sys.stderr)
            return 2
    print(
        f"Contrôle informatif : {len(results)}/{len(urls)} URL ; "
        f"accessibles={counts['reachable']}, "
        f"indisponibles (404/410)={counts['unavailable']}, "
        f"indéterminées={counts['indeterminate']}."
    )
    print("403/429, délais et erreurs réseau ne prouvent pas la disparition d'une source.")
    print("Aucun corps HTTP lu ; aucun contenu ni résultat de compatibilité vérifié.")
    for result in results:
        url = json.dumps(result["url"], ensure_ascii=False)
        print(f"- {result['classification']} | {result['reason']} | {url}")
    if args.output is not None:
        print(f"Rapport JSON : {args.output}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
