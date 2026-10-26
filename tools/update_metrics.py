#!/usr/bin/env python3
"""Regenerate documentary counts without inventing API or runtime coverage."""
import csv
import json
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def read_csv(relative):
    with (ROOT / relative).open(encoding="utf-8-sig", newline="") as stream:
        return list(csv.DictReader(stream))


def main():
    rows = read_csv("data/fonctionnalites.csv")
    chapters = sorted((ROOT / "docs").glob("*.md"))
    bibliography = json.loads((ROOT / "data/bibliographie.json").read_text(encoding="utf-8"))
    precise = [row["id"] for row in rows if "référence ciblée" in row["statut_preuve"]]
    policy = json.loads((ROOT / "data/contraintes-projet.json").read_text(encoding="utf-8"))
    execution_plan = json.loads((ROOT / "data/plan-realisation.json").read_text(encoding="utf-8"))
    assignments = read_csv("data/exigences-blocs.csv")
    execution_tasks = [task for block in execution_plan["blocks"] for task in block["tasks"]]
    linked_requirements = {identity for task in execution_tasks for identity in task["requirement_ids"]}
    output = {
        "date_recherche": "2026-10-26",
        "nature": "mesures_du_dossier_documentaire_uniquement",
        "chapitres": len(chapters),
        "mots_chapitres": sum(len(path.read_text(encoding="utf-8").split()) for path in chapters),
        "exigences_fonctionnelles": len(rows),
        "domaines": len({row["domaine"] for row in rows}),
        "priorites": dict(sorted(Counter(row["priorite"] for row in rows).items())),
        "url_distinctes_citees": bibliography["url_count"],
        "statuts_implementation": dict(sorted(Counter(row["statut_implementation"] for row in rows).items())),
        "compatibilite_executee_mesuree": False,
        "catalogue_api_exhaustif_certifie": False,
        "logiciels_pcsoft_autorises": policy["pcsoft_software_allowed"],
        "choix_licence_publication": policy["publication_license_decision"],
        "preuve_independance_binaire": "non réalisée; aucun produit implémenté à inspecter",
        "admission_outils": "candidats non admis; aucun droit d'usage du futur produit vérifié par ces métriques",
        "couverture_api": {
            "rattachement_fonctions_catalogue": "non établi",
            "denominateur_versionne": None,
            "nb_fonctions_couvertes": None,
            "ratio": None,
            "raison": "Exigences et fonctions sont des unités différentes; catalogue fermé et preuves absents.",
        },
        "exigences_rattachement_api_inconnu": sum(row["nb_fonctions_couvertes"] == "INCONNU" for row in rows),
        "references_ciblees": {"nombre": len(precise), "exigences": precise},
        "taches_premier_lot": len(read_csv("data/premier-lot.csv")),
        "seuils_proposes_non_valides": len(read_csv("data/seuils-decision.csv")),
        "plan_realisation": {
            "blocs": len(execution_plan["blocks"]),
            "taches_explicites": sum(len(block["tasks"]) for block in execution_plan["blocks"]),
            "gates": len(execution_plan["blocks"]),
            "gates_executees": 0,
            "exigences_parents_rattachees": len(assignments),
            "parents_avec_lien_de_support_ou_preparation": len(linked_requirements),
            "parents_sans_ticket_de_support_explicite": len(rows) - len(linked_requirements),
            "liens_de_taches": dict(sorted(Counter(task["requirement_relation"] for task in execution_tasks).items())),
            "portees": dict(sorted(Counter(row["delivery_scope"] for row in assignments).items())),
            "budgets_tickets": "2–6 h cibles, à redécouper si non borné; ni délai garanti ni estimation totale",
            "limite": "Socle explicite et extensions à décomposer; aucune fonction ou exigence implémentée par la planification.",
        },
        "verification_structurelle": "Exécuter tools/check_repository.py; ces métriques ne préjugent pas de son résultat.",
        "limite_controles": "Aucun test de moteur WINDEV/WLangage; contrôle de liens externes distinct et informatif.",
    }
    path = ROOT / "data/metriques-dossier.json"
    path.write_text(json.dumps(output, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Métriques : {len(chapters)} chapitres, {len(rows)} exigences; couverture API non calculable.")


if __name__ == "__main__":
    main()
