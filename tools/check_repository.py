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
    "nb_fonctions_couvertes", "statut_rattachement_api",
    "decision_perimetre",
}


def main():
    errors = []
    markdown = sorted(path for path in ROOT.rglob("*.md") if ".git" not in path.relative_to(ROOT).parts)
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
            count = row.get("nb_fonctions_couvertes", "")
            if count != "INCONNU" and not count.isdigit():
                errors.append(f"Nombre de fonctions invalide ligne {line}")
            if count == "INCONNU" and row.get("statut_rattachement_api") != "non établi":
                errors.append(f"Rattachement API incohérent ligne {line}")
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

    try:
        policy = json.loads((ROOT / "data/contraintes-projet.json").read_text(encoding="utf-8"))
        if policy["pcsoft_software_allowed"] is not False:
            errors.append("La contrainte du propriétaire exclut les logiciels PC SOFT")
        if policy["publication_license_decision"] != "differee":
            errors.append("Le choix de licence de publication est différé")
        profile = json.loads((ROOT / "examples/profil-migration.exemple.json").read_text(encoding="utf-8"))
        if profile["constraints"]["noPcsoft"] is not True:
            errors.append("Le modèle de profil doit reprendre noPcsoft=true")
        if profile["generation_gate"]["no_PCSoft"] is not True:
            errors.append("Le modèle doit déclarer le contrôle d'exclusion PC SOFT")
    except (OSError, ValueError, KeyError, TypeError):
        errors.append("Contrainte d'indépendance ou profil manquant/incohérent")
    bibliography = ROOT / "data/bibliographie.json"
    if bibliography.exists():
        try:
            content = json.loads(bibliography.read_text(encoding="utf-8"))
            if content["url_count"] != len(content["references"]):
                errors.append("Comptage bibliographique incohérent")
        except (ValueError, KeyError, TypeError):
            errors.append("Structure bibliographique invalide")

    metrics = ROOT / "data/metriques-dossier.json"
    if metrics.exists():
        try:
            data = json.loads(metrics.read_text(encoding="utf-8"))
            if data["exigences_fonctionnelles"] != len(rows):
                errors.append("Métriques : nombre d'exigences périmé")
            if data["chapitres"] != len(list((ROOT / "docs").glob("*.md"))):
                errors.append("Métriques : nombre de chapitres périmé")
            if data["couverture_api"]["ratio"] is not None:
                errors.append("Aucun ratio API n'est démontré dans ce dossier")
        except (ValueError, KeyError, TypeError):
            errors.append("Structure des métriques invalide")

    plan_path = ROOT / "data/premier-lot.csv"
    plan = []
    if plan_path.exists():
        with plan_path.open(encoding="utf-8", newline="") as stream:
            plan = list(csv.DictReader(stream))
        plan_ids = {item["id"] for item in plan}
        requirement_ids = {row["id"] for row in rows}
        if len(plan_ids) != len(plan):
            errors.append("Identifiant de lot dupliqué")
        graph = {}
        for item in plan:
            identity = item["id"]
            dependencies = [x for x in item["dependances"].split(";") if x]
            graph[identity] = dependencies
            for dependency in dependencies:
                if dependency not in plan_ids:
                    errors.append(f"Prérequis inconnu pour {identity}: {dependency}")
            for reference in item["exigences_ids"].split(";"):
                if reference not in requirement_ids:
                    errors.append(f"Exigence inconnue pour {identity}: {reference}")
            if item["statut_execution"] != "non exécuté":
                errors.append(f"Aucune exécution de ce lot n'est démontrée : {identity}")
        active, finished = set(), set()

        def visit(identity):
            if identity in active:
                errors.append(f"Cycle de dépendances dans le lot: {identity}")
                return
            if identity in finished:
                return
            active.add(identity)
            for dependency in graph.get(identity, []):
                visit(dependency)
            active.remove(identity)
            finished.add(identity)

        for identity in graph:
            visit(identity)

    thresholds = ROOT / "data/seuils-decision.csv"
    if thresholds.exists():
        with thresholds.open(encoding="utf-8", newline="") as stream:
            for row in csv.DictReader(stream):
                if row["statut"] != "proposition_non_validee":
                    errors.append(f"Seuil présenté validé sans essai : {row['id']}")
                if not (ROOT / row["reference_document"]).is_file():
                    errors.append(f"Source locale du seuil absente : {row['id']}")

    print(f"Chapitres : {len(list((ROOT / 'docs').glob('*.md')))}")
    print(f"Exigences : {len(rows)}")
    print("Domaines : " + str(len({r.get('domaine') for r in rows})))
    print("Priorités : " + json.dumps(dict(sorted(Counter(r.get('priorite') for r in rows).items())), ensure_ascii=False))
    print(f"Fichiers JSON vérifiés : {len(json_paths)}")
    print(f"Tâches du premier lot : {len(plan)} ; références et absence de cycle vérifiées.")
    print("Contrôle : structure documentaire, JSON, identifiants, références, seuils proposés et graphe du lot.")
    if errors:
        for error in errors:
            print("ERREUR : " + error, file=sys.stderr)
        return 1
    print("Intégrité documentaire : OK. Aucune compatibilité WLangage testée par ce contrôle.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
