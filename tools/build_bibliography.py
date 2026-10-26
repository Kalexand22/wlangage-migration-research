#!/usr/bin/env python3
"""Index the URLs cited by this research; this does not verify their contents."""
import csv
import json
import re
from pathlib import Path
from urllib.parse import urlsplit

ROOT = Path(__file__).resolve().parents[1]
LINK = re.compile(r"\[([^\]\n]+)\]\((https?://[^\s)]+)\)")


def main():
    references = {}

    def add(url, title, origin):
        record = references.setdefault(url, {
            "url": url,
            "host": urlsplit(url).hostname,
            "labels": [],
            "referenced_in": [],
            "verification": "see_chapter_method_and_qualifications",
        })
        if title not in record["labels"]:
            record["labels"].append(title)
        if origin not in record["referenced_in"]:
            record["referenced_in"].append(origin)

    for path in sorted((ROOT / "docs").glob("*.md")):
        for title, url in LINK.findall(path.read_text(encoding="utf-8")):
            add(url, title, path.relative_to(ROOT).as_posix())
    matrix = ROOT / "data/fonctionnalites.csv"
    if matrix.exists():
        with matrix.open(encoding="utf-8-sig", newline="") as stream:
            for row in csv.DictReader(stream):
                add(row["source_url"], row["domaine"], "data/fonctionnalites.csv")
    output = {
        "research_date": "2026-10-26",
        "kind": "index_of_cited_urls_not_a_network_or_factual_verification",
        "method": "Exact URLs extracted from chapter Markdown and the functional matrix; aliases may point to the same document.",
        "url_count": len(references),
        "references": [references[url] for url in sorted(references)],
    }
    path = ROOT / "data/bibliographie.json"
    path.write_text(json.dumps(output, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"{len(references)} URL citées indexées dans {path.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
