"""Negative cases for the plan guard, using disposable copies of documentary data."""
import json
import shutil
import sys
import tempfile
import unittest
from pathlib import Path

REPOSITORY = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPOSITORY / "tools"))
from build_execution_plan import render
from check_execution_plan import validate


class ExecutionPlanGuardTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name)
        (self.root / "data").mkdir()
        for name in ["plan-realisation.json", "exigences-blocs.csv", "fonctionnalites.csv"]:
            shutil.copyfile(REPOSITORY / "data" / name, self.root / "data" / name)
        self.plan = json.loads((self.root / "data/plan-realisation.json").read_text(encoding="utf-8"))
        self.save()

    def save(self):
        (self.root / "data/plan-realisation.json").write_text(
            json.dumps(self.plan, ensure_ascii=False), encoding="utf-8")
        for relative, content in render(self.root).items():
            path = self.root / relative
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(content, encoding="utf-8")

    def assert_rejected(self, expected):
        self.assertTrue(any(expected in error for error in validate(self.root)), expected)

    def test_proposed_plan_is_structurally_valid(self):
        self.assertEqual(validate(self.root), [])

    def test_cycle_through_block_gates_is_rejected(self):
        self.plan["blocks"][0]["depends_on_blocks"] = ["B06"]
        self.save()
        self.assert_rejected("cycle tâches/gates")

    def test_unknown_task_dependency_is_rejected(self):
        self.plan["blocks"][0]["tasks"][0]["depends_on"] = ["T-ABSENT-01"]
        self.save()
        self.assert_rejected("tâche préalable inconnue")

    def test_task_specific_gate_participates_in_cycle_detection(self):
        self.plan["blocks"][0]["tasks"][0]["requires_block_gates"] = ["B06"]
        self.save()
        self.assert_rejected("cycle tâches/gates")

    def test_gate_cannot_omit_one_of_its_tasks(self):
        self.plan["blocks"][0]["gate"]["required_tasks"].pop()
        self.save()
        self.assert_rejected("gate omet une tâche")

    def test_proposal_cannot_claim_an_executed_gate(self):
        self.plan["blocks"][0]["gate"]["status"] = "pass_verified"
        self.save()
        self.assert_rejected("aucun passage exécuté établi")

    def test_a_lost_requirement_is_not_silent(self):
        path = self.root / "data/exigences-blocs.csv"
        lines = path.read_text(encoding="utf-8").splitlines(keepends=True)
        path.write_text("".join(lines[:-1]), encoding="utf-8")
        self.assert_rejected("cartographie exigences incomplète")

    def test_stale_generated_card_is_rejected(self):
        card = self.root / "plan/blocs/B00.md"
        card.write_text(card.read_text(encoding="utf-8") + "Faux changement manuel.\n", encoding="utf-8")
        self.assert_rejected("Plan généré périmé")

    def test_unbounded_ticket_budget_is_rejected(self):
        self.plan["blocks"][0]["tasks"][0]["size"]["target_hours_max"] = 40
        self.save()
        self.assert_rejected("budget ou règle de découpage")

    def test_unknown_cannot_become_success(self):
        self.plan["task_policy"]["unknown_is_success"] = True
        self.save()
        self.assert_rejected("un inconnu ne peut jamais valoir réussite")

    def test_independent_review_cannot_be_disabled(self):
        self.plan["task_policy"]["review_is_separate"] = False
        self.save()
        self.assert_rejected("invariant obligatoire désactivé : review_is_separate")

    def test_final_revision_evidence_cannot_be_removed(self):
        self.plan["blocks"][0]["tasks"][0]["evidence_required"] = ["resultats_obtenus"]
        self.save()
        self.assert_rejected("preuves obligatoires manquantes")

    def test_gate_common_controls_cannot_be_emptied(self):
        self.plan["blocks"][0]["gate"]["common_checks"] = []
        self.save()
        self.assert_rejected("contrôles communs de gate manquants")

    def test_task_cannot_link_an_invented_requirement(self):
        self.plan["blocks"][0]["tasks"][0]["requirement_ids"] = ["F-9999"]
        self.save()
        self.assert_rejected("lien vers exigence inconnue")

    def test_planning_link_cannot_claim_coverage(self):
        self.plan["blocks"][0]["tasks"][0]["coverage_claim"] = "complete"
        self.save()
        self.assert_rejected("absence de revendication incohérente")


if __name__ == "__main__":
    unittest.main()
