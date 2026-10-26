#!/usr/bin/env python3
"""Validate the documentary DAG and generated backlog, not any product gate."""
import csv
import json
import sys
from pathlib import Path

from build_execution_plan import render

ROOT = Path(__file__).resolve().parents[1]


def validate(root=ROOT):
    errors = []
    try:
        plan = json.loads((root / "data/plan-realisation.json").read_text(encoding="utf-8"))
        blocks = plan["blocks"]
        if plan["pcsoft_software_allowed"] is not False or plan["publication_license_decision"] != "differee":
            errors.append("Plan : contraintes PC SOFT ou licence de publication altérées")
        if plan["product_status"] != "non_implemente" or plan["execution_authorized_by_this_plan"] is not False:
            errors.append("Plan : une proposition documentaire n’exécute pas le produit")
        if plan["task_policy"]["required_gate_status_to_start"] != "pass_verified":
            errors.append("Plan : passage de gate non vérifié interdit")
        for key in ["review_is_separate", "gate_requires_final_revision_evidence", "stop_and_split_on_budget"]:
            if plan["task_policy"][key] is not True:
                errors.append("Plan : invariant obligatoire désactivé : " + key)
        if plan["task_policy"]["unknown_is_success"] is not False:
            errors.append("Plan : un inconnu ne peut jamais valoir réussite")
        if not {"pcsoft_exclusion", "unresolved_usage_rights", "data_loss", "unknown_claimed_conformant"}.issubset(plan["common_gate"]["no_waiver"]):
            errors.append("Plan : contraintes sans dérogation manquantes")
        if plan["database_policy"]["first_real_engines"] != ["PostgreSQL", "SQLite"]:
            errors.append("Plan : deux moteurs réels requis au premier jalon données")
        block_ids = [block["id"] for block in blocks]
        tasks = [task for block in blocks for task in block["tasks"]]
        task_ids = [task["id"] for task in tasks]
        gate_ids = [block["gate"]["id"] for block in blocks]
        for label, identities in [("blocs", block_ids), ("tâches", task_ids), ("gates", gate_ids)]:
            if len(identities) != len(set(identities)):
                errors.append("Plan : identifiants dupliqués de " + label)
        graph = {}
        for block in blocks:
            bid = block["id"]
            gate = block["gate"]
            if gate["id"] != "G-" + bid:
                errors.append(f"Plan : gate incorrecte pour {bid}")
            if gate["status"] != "non_execute" or block["status"] != "planifie":
                errors.append(f"Plan : aucun passage exécuté établi pour {bid}")
            if not gate["criteria"] or not block["tasks"]:
                errors.append(f"Plan : bloc sans critère ou tâche {bid}")
            if not {"admission_par_version_acte_et_contexte", "aucune_dependance_PC_SOFT", "aucune_perte_ou_inconnu_masque", "preuves_revision_finale", "revue_independante"}.issubset(gate["common_checks"]):
                errors.append(f"Plan : contrôles communs de gate manquants {bid}")
            if gate["required_tasks"] != [task["id"] for task in block["tasks"]]:
                errors.append(f"Plan : gate omet une tâche de {bid}")
            for dep in block["depends_on_blocks"]:
                if dep not in block_ids:
                    errors.append(f"Plan : bloc préalable inconnu {bid} -> {dep}")
            for task in block["tasks"]:
                tid = task["id"]
                if not tid.startswith("T-" + bid + "-"):
                    errors.append(f"Plan : tâche hors de son bloc {tid}")
                if task["status"] != "planifie" or task["validation"]["execution_status"] != "non_execute":
                    errors.append(f"Plan : exécution non démontrée {tid}")
                if not task["objective"] or not task["acceptance"] or not task["deliverables"]:
                    errors.append(f"Plan : ticket sans résultat vérifiable {tid}")
                if task["deliverables"] != [task["objective"]] or task["validation"]["procedure"] != " ; ".join(task["acceptance"]):
                    errors.append(f"Plan : livrable ou procédure en désaccord avec le contrat {tid}")
                low, high = task["size"]["target_hours_min"], task["size"]["target_hours_max"]
                if not 0 < low <= high <= 6 or not task["size"]["split_if_unbounded"]:
                    errors.append(f"Plan : budget ou règle de découpage incohérents {tid}")
                if task["review_role"] != "reviewer_independant" or not task["evidence_required"]:
                    errors.append(f"Plan : absence de revue/preuves {tid}")
                if not {"revision_finale", "arbre_final_integre", "versions_et_admissions", "commandes_et_codes_sortie", "resultats_attendus_sources", "resultats_obtenus", "diff_et_limites"}.issubset(task["evidence_required"]):
                    errors.append(f"Plan : preuves obligatoires manquantes {tid}")
                if not {"usage_PC_SOFT", "copie_privee_non_admise", "auto_approbation", "PASS_sans_execution", "modification_silencieuse_sources"}.issubset(task["forbidden"]):
                    errors.append(f"Plan : interdictions obligatoires manquantes {tid}")
                for dep in task["depends_on"]:
                    if dep not in task_ids:
                        errors.append(f"Plan : tâche préalable inconnue {tid} -> {dep}")
                for dep in task["requires_block_gates"]:
                    if dep not in block_ids:
                        errors.append(f"Plan : gate supplémentaire inconnue {tid} -> {dep}")
                graph[tid] = list(task["depends_on"]) + ["G-" + dep for dep in block["depends_on_blocks"] + task["requires_block_gates"]]
            graph[gate["id"]] = list(gate["required_tasks"])
        active, visited = set(), set()

        def visit(identity):
            if identity in active:
                errors.append("Plan : cycle tâches/gates à " + identity)
                return
            if identity in visited:
                return
            active.add(identity)
            for dep in graph.get(identity, []):
                visit(dep)
            active.remove(identity)
            visited.add(identity)

        for identity in graph:
            visit(identity)
        with (root / "data/fonctionnalites.csv").open(encoding="utf-8", newline="") as stream:
            requirements = {row["id"] for row in csv.DictReader(stream)}
        contracts = []
        for task in tasks:
            contracts.append(task["contract_id"])
            if task["contract_id"] != "K-" + task["id"][2:] or task["coverage_claim"] != "none":
                errors.append("Plan : contrat planifié ou absence de revendication incohérente " + task["id"])
            relation = task["requirement_relation"]
            if relation not in {"preparation", "support_partiel", "enabler_hors_matrice", "a_rattacher_apres_choix"} or not task["requirement_link_reason"]:
                errors.append("Plan : lien d’exigence sans qualification " + task["id"])
            references = task["requirement_ids"]
            if len(references) != len(set(references)) or not set(references).issubset(requirements):
                errors.append("Plan : lien vers exigence inconnue ou dupliquée " + task["id"])
            if relation in {"preparation", "support_partiel"} and not references:
                errors.append("Plan : relation de support sans parent " + task["id"])
            if relation in {"enabler_hors_matrice", "a_rattacher_apres_choix"} and references:
                errors.append("Plan : parent artificiel sur lien non établi " + task["id"])
        if len(contracts) != len(set(contracts)):
            errors.append("Plan : identifiant de contrat dupliqué")
        with (root / "data/exigences-blocs.csv").open(encoding="utf-8", newline="") as stream:
            mapping = list(csv.DictReader(stream))
        mapped_ids = [row["requirement_id"] for row in mapping]
        if len(mapped_ids) != len(set(mapped_ids)) or set(mapped_ids) != requirements:
            errors.append("Plan : cartographie exigences incomplète ou dupliquée")
        scopes = {"socle_partiel", "extension_a_decomposer", "exclu_technologie_pcsoft_comportement_a_reimplementer"}
        for row in mapping:
            if row["block_id"] not in block_ids or row["delivery_scope"] not in scopes:
                errors.append("Plan : rattachement invalide de " + row["requirement_id"])
            if row["execution_status"] != "non_execute" or not row["notes"]:
                errors.append("Plan : parent sans limite explicite " + row["requirement_id"])
        for relative, expected in render(root).items():
            path = root / relative
            if not path.exists() or path.read_text(encoding="utf-8") != expected:
                errors.append("Plan généré périmé : " + relative)
    except (OSError, ValueError, KeyError, TypeError) as exc:
        errors.append("Plan : structure ou fichier invalide : " + str(exc))
    return errors


def main():
    errors = validate()
    if errors:
        for error in errors:
            print("ERREUR : " + error, file=sys.stderr)
        return 1
    print("Plan : DAG tâches/gates, parents, budgets déclarés et fichiers générés cohérents. Aucune gate produit exécutée.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
