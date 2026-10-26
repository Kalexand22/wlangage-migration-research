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
        "verification_structurelle": "Exécuter tools/check_repository.py; ces métriques ne préjugent pas de son résultat.",
        "limite_controles": "Aucun test de moteur WINDEV/WLangage; contrôle de liens externes distinct et informatif.",
    }
    path = ROOT / "data/metriques-dossier.json"
    path.write_text(json.dumps(output, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Métriques : {len(chapters)} chapitres, {len(rows)} exigences; couverture API non calculable.")


if __name__ == "__main__":
    main()
