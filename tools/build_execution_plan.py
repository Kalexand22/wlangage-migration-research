#!/usr/bin/env python3
"""Render the proposed agent backlog. Never starts agents or declares gates passed."""
import csv
import io
import json
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def render(root=ROOT):
    plan = json.loads((root / "data/plan-realisation.json").read_text(encoding="utf-8"))
    with (root / "data/exigences-blocs.csv").open(encoding="utf-8", newline="") as stream:
        mapping = list(csv.DictReader(stream))
    with (root / "data/fonctionnalites.csv").open(encoding="utf-8", newline="") as stream:
        requirements = {row["id"]: row for row in csv.DictReader(stream)}
    counts = Counter(row["block_id"] for row in mapping)
    blocks = plan["blocks"]
    linked_tasks = {}
    for block in blocks:
        for task in block["tasks"]:
            for identity in task.get("requirement_ids", []):
                linked_tasks.setdefault(identity, []).append(task["id"])
    task_count = sum(len(block["tasks"]) for block in blocks)
    outputs = {}
    index = [
        "# Plan de réalisation pour agents IA\n",
        "**Plan proposé, non exécuté.** Base C#, applications maintenues en WLangage, "
        "PostgreSQL + SQLite d’abord. Aucun outil ni composant PC SOFT.\n",
        f"**{len(blocks)} blocs, {task_count} tâches explicites, {len(blocks)} gates et "
        f"{len(mapping)} exigences parents rattachées.** Les exigences parents ne sont pas "
        "des tickets exécutables : les extensions demandent une décomposition complémentaire. "
        "Les tickets ci-dessous bornent le socle et organisent cet élargissement.\n",
        "Sources : [plan JSON](../data/plan-realisation.json), "
        "[backlog CSV](../data/taches-agents.csv), "
        "[rattachement des exigences](../data/exigences-blocs.csv). "
        "[Agenda des parents à décomposer](../data/extensions-a-decomposer.csv). "
        "[Guide de réalisation](../docs/16-plan-detaille-de-realisation.md), "
        "[orchestration](../docs/17-orchestration-agents-et-gates.md), "
        "[architecture C# / multi-BDD](../docs/18-architecture-csharp-multi-bdd-et-reemploi.md).\n",
        "Une tâche vise 2–6 heures de travail d’agent comme budget à réviser. "
        "Dès que le périmètre n’est plus borné, la tâche est suspendue puis redécoupée ; "
        "le temps écoulé ne valide rien. Revue et intégration sont distinctes.\n",
        "| Bloc | Livrable | Tâches | Gate | Prérequis de blocs | Exigences parents |\n"
        "| --- | --- | ---: | --- | --- | ---: |",
    ]
    for block in blocks:
        bid = block["id"]
        gate = block["gate"]
        prereqs = ", ".join(block["depends_on_blocks"]) or "aucun"
        index.append(f"| [{bid}](blocs/{bid}.md) | {block['title']} | {len(block['tasks'])} | "
                     f"{gate['id']} | {prereqs} | {counts[bid]} |")
        lines = [
            f"# {bid} — {block['title']}\n",
            "**Statut : planifié ; gate non exécutée.**\n",
            block["goal"] + "\n",
            f"Piste : `{block['track']}`. Périmètre proposé dans le futur dépôt produit : "
            f"`{block['module_scope']}`. Ces modules ne sont pas implémentés dans ce dossier.\n",
            "[Index du plan](../README.md) · "
            "[Source JSON](../../data/plan-realisation.json)\n",
            "## Conditions de départ\n",
            ("Gates exigées : " + ", ".join("`G-" + x + "`" for x in block["depends_on_blocks"]) + ".\n")
            if block["depends_on_blocks"] else "Aucune gate de bloc préalable ; qualifier les actes avant leur réalisation.\n",
            "Admissions exactes, entrées autorisées et espace isolé sont requis en plus du DAG. "
            "Une nouvelle dépendance doit être admise au moment où elle est nécessaire ; "
            "G-B00 n’autorise pas automatiquement les futurs outils.\n",
            f"## Gate de sortie {gate['id']}\n",
        ]
        lines.extend("- " + criterion for criterion in gate["criteria"])
        lines.extend([
            "\nLa gate examine aussi les admissions, l’exclusion PC SOFT, les résultats de tests "
            "et la conservation des sources/données. Elle exige les preuves de la révision intégrée "
            "finale et une revue par un autre agent. `FAIL`, `BLOCKED`, `non_execute` ou preuve "
            "périmée ferment la gate. Aucun PASS implicite à la fin des tâches.\n",
            "## Tâches ordonnées\n",
            "Chaque tâche est un budget cible de **2–6 h**, pas une garantie. Les cinq fichiers "
            "et 600 lignes évoqués dans la politique sont des signaux de redécoupage, pas des critères "
            "de qualité. Si un ticket contient plusieurs comportements indépendants, le scinder "
            "avant attribution et conserver ses critères au parent.\n",
        ])
        for task in block["tasks"]:
            deps = ", ".join(task["depends_on"]) or "gates de départ du bloc"
            if task["requires_block_gates"]:
                deps += " ; gates supplémentaires " + ", ".join("G-" + x for x in task["requires_block_gates"])
            lines.extend([
                f"### {task['id']} — {task['title']}\n",
                "**Livrable :** " + task["objective"] + ".\n",
                "**Prérequis :** " + deps + ".\n",
                "**Contrat planifié :** `" + task.get("contract_id", "a_preciser") + "`. "
                "**Parents :** " + (", ".join(task.get("requirement_ids", [])) or "aucun rattachement arbitraire") + ". "
                + task.get("requirement_link_reason", "Traçabilité à préciser avant attribution.") + "\n",
                "**Acceptation et procédure de vérification :**\n",
            ])
            lines.extend("- " + criterion for criterion in task["acceptance"])
            lines.append("\n**Preuve à remettre :** révision et arbre exacts, versions/admissions, "
                         "commande ou procédure avec code de sortie, attendus sourcés, résultats, "
                         "diff et limites ; revue indépendante. Aucun test n’a été exécuté pour ce ticket.\n")
        outputs[f"plan/blocs/{bid}.md"] = "\n".join(lines).rstrip() + "\n"
    index.extend([
        "\n## Lecture des dépendances\n",
        "Une flèche indique une gate requise, pas seulement la présence d’un document. "
        "La représentation exacte est le JSON ; chaque fiche rappelle ses prérequis.\n",
        "```mermaid\nflowchart TD",
    ])
    for block in blocks:
        index.append(f"  {block['id']}[\"{block['id']}\"]")
    for block in blocks:
        for dep in block["depends_on_blocks"]:
            index.append(f"  {dep} --> {block['id']}")
    index.extend(["```\n", "Fichier généré par `python3 tools/build_execution_plan.py`. "
                  "Modifier le JSON et la cartographie, puis régénérer.\n"])
    outputs["plan/README.md"] = "\n".join(index)
    stream = io.StringIO(newline="")
    writer = csv.writer(stream, lineterminator="\n")
    writer.writerow(["id", "block_id", "title", "deliverable", "contract_id", "requirement_ids", "requirement_relation", "depends_on_tasks", "required_block_gates",
                     "gate_id", "acceptance", "target_hours_min", "target_hours_max", "status", "validation_status"])
    for block in blocks:
        for task in block["tasks"]:
            required_gates = list(dict.fromkeys(block["depends_on_blocks"] + task["requires_block_gates"]))
            writer.writerow([task["id"], block["id"], task["title"], task["objective"], task.get("contract_id", ""),
                             ";".join(task.get("requirement_ids", [])), task.get("requirement_relation", ""),
                             ";".join(task["depends_on"]), ";".join("G-" + x for x in required_gates),
                             block["gate"]["id"], " ; ".join(task["acceptance"]),
                             task["size"]["target_hours_min"], task["size"]["target_hours_max"],
                             task["status"], task["validation"]["execution_status"]])
    outputs["data/taches-agents.csv"] = stream.getvalue()
    stream = io.StringIO(newline="")
    writer = csv.writer(stream, lineterminator="\n")
    writer.writerow(["extension_id", "requirement_id", "title", "priority", "owner_block", "scope",
                     "acceptance_from_parent", "linked_support_tasks", "status", "schedulable", "remaining_contracts", "closure_claim"])
    for row in sorted(mapping, key=lambda item: (requirements[item["requirement_id"]]["priorite"], item["requirement_id"])):
        requirement = requirements[row["requirement_id"]]
        writer.writerow(["E-" + row["requirement_id"], row["requirement_id"], requirement["fonctionnalite"],
                         requirement["priorite"], row["block_id"], row["delivery_scope"],
                         requirement["critere_acceptation"], ";".join(linked_tasks.get(row["requirement_id"], [])),
                         "a_decomposer", "false", "a_inventorier_par_contrat", "aucune"])
    outputs["data/extensions-a-decomposer.csv"] = stream.getvalue()
    return outputs


def main():
    outputs = render()
    for relative, content in outputs.items():
        path = ROOT / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8")
    print(f"Plan généré : {len(outputs) - 3} fiches de blocs, index, backlog et agenda des parents. Aucune tâche exécutée.")


if __name__ == "__main__":
    main()
