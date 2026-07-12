import unittest
from runbook import extract, markdown


class RunbookTests(unittest.TestCase):
    def incident(self):
        return {"title": "Queue delay", "events": [{"type": "symptom", "text": "lag high"}, {"type": "check", "text": "inspect lag"}, {"type": "action", "text": "restart worker", "destructive": True}]}

    def test_extracts_runbook_sections(self):
        report = extract(self.incident())
        self.assertEqual(report["symptoms"], ["lag high"])
        self.assertEqual(report["checks"], ["inspect lag"])

    def test_marks_sensitive_actions_for_approval(self):
        self.assertTrue(extract(self.incident())["actions"][0]["approval_required"])

    def test_renders_markdown(self):
        output = markdown(extract(self.incident()))
        self.assertIn("# Queue delay", output)
        self.assertIn("[Approval required]", output)


if __name__ == "__main__":
    unittest.main()
