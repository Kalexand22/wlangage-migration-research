#!/usr/bin/env python3
"""Check the research package's structural integrity, never product compatibility."""
import csv
import json
import re
import sys
from collections import Counter
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
LINK = re.compile(r"\[[^\]\n]+\]\(([^\s)]+)\)")
REQUIRED = {
    "id", "domaine", "sous_domaine", "fonctionnalite", "produits_reference",
    "cibles_proposees", "priorite", "strategie", "statut_preuve",
    "critere_acceptation", "source_url", "statut_implementation", "portee_source",
}


def main():
    errors = []
    markdown = sorted(ROOT.glob("*.md")) + sorted((ROOT / "docs").glob("*.md"))
    for path in markdown:
        for target in LINK.findall(path.read_text(encoding="utf-8")):
            if target.startswith(("https://", "http://", "mailto:", "#")):
                continue
            relative = unquote(target.split("#", 1)[0])
            candidate = (path.parent / relative).resolve()
            if not candidate.is_relative_to(ROOT):
                errors.append(f"Lien sortant du dépôt : {path.relative_to(ROOT)} -> {target}")
            elif not candidate.exists():
                errors.append(f"Lien local manquant : {path.relative_to(ROOT)} -> {target}")

    matrix = ROOT / "data/fonctionnalites.csv"
    rows = []
    if not matrix.exists():
        errors.append("Matrice fonctionnelle absente")
    else:
        with matrix.open(encoding="utf-8-sig", newline="") as stream:
            reader = csv.DictReader(stream)
            if not REQUIRED.issubset(reader.fieldnames or []):
                errors.append("Colonnes obligatoires absentes de la matrice")
            rows = list(reader)
        seen = set()
        for line, row in enumerate(rows, start=2):
            identity = row.get("id", "")
            if not re.fullmatch(r"F-\d{4}", identity) or identity in seen:
                errors.append(f"Identifiant invalide ou dupliqué ligne {line}: {identity}")
            seen.add(identity)
            for field in REQUIRED:
                if not (row.get(field) or "").strip():
                    errors.append(f"Champ vide ligne {line}: {field}")
            if row.get("priorite") not in {"P0", "P1", "P2", "P3"}:
                errors.append(f"Priorité invalide ligne {line}")
            if row.get("statut_implementation") != "non implémenté":
                errors.append(f"Ce dossier de recherche ne démontre aucune implémentation : ligne {line}")
            parsed = urlsplit(row.get("source_url", ""))
            if parsed.scheme not in {"http", "https"} or not parsed.hostname:
                errors.append(f"URL source invalide ligne {line}")
            if None in row:
                errors.append(f"Colonnes excédentaires ligne {line}")

    json_paths = sorted((ROOT / "data").glob("*.json")) + sorted((ROOT / "examples").glob("*.json"))
    for path in json_paths:
        try:
            json.loads(path.read_text(encoding="utf-8"))
        except (ValueError, UnicodeError) as exc:
            errors.append(f"JSON invalide {path.relative_to(ROOT)} : {exc}")
    bibliography = ROOT / "data/bibliographie.json"
    if bibliography.exists():
        try:
            content = json.loads(bibliography.read_text(encoding="utf-8"))
            if content["url_count"] != len(content["references"]):
                errors.append("Comptage bibliographique incohérent")
        except (ValueError, KeyError, TypeError):
            errors.append("Structure bibliographique invalide")

    print(f"Chapitres : {len(list((ROOT / 'docs').glob('*.md')))}")
    print(f"Exigences : {len(rows)}")
    print("Domaines : " + str(len({r.get('domaine') for r in rows})))
    print("Priorités : " + json.dumps(dict(sorted(Counter(r.get('priorite') for r in rows).items())), ensure_ascii=False))
    print(f"Fichiers JSON vérifiés : {len(json_paths)}")
    print("Contrôle : liens locaux, structure CSV, identifiants, statuts et JSON uniquement.")
    if errors:
        for error in errors:
            print("ERREUR : " + error, file=sys.stderr)
        return 1
    print("Intégrité documentaire : OK. Aucune compatibilité WLangage testée par ce contrôle.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
