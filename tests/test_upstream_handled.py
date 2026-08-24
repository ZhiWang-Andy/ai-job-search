"""Tests for the personalized fork's manually handled upstream-commit list."""

import importlib.util
import tempfile
import unittest
from pathlib import Path


REPO = Path(__file__).resolve().parent.parent
SCRIPT = REPO / "tools" / "upstream_triage.py"
HANDLED = REPO / ".github" / "upstream-handled.txt"

spec = importlib.util.spec_from_file_location("upstream_triage", SCRIPT)
upstream_triage = importlib.util.module_from_spec(spec)
assert spec.loader is not None
spec.loader.exec_module(upstream_triage)


class PrefixListTests(unittest.TestCase):
    def test_comment_friendly_prefix_loader(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "handled.txt"
            path.write_text("abc123 # adapted\n\n# comment\ndef456\n", encoding="utf-8")
            self.assertEqual(upstream_triage.load_prefix_list(str(path)), ["abc123", "def456"])

    def test_missing_prefix_file_is_empty(self):
        self.assertEqual(upstream_triage.load_prefix_list("definitely-missing-file.txt"), [])


class HandledIntegrationContractTests(unittest.TestCase):
    def test_cli_has_handled_list_and_manual_port_reason(self):
        text = SCRIPT.read_text(encoding="utf-8")
        self.assertIn('ap.add_argument("--handled", default=".github/upstream-handled.txt")', text)
        self.assertIn("already reviewed and ported/adapted manually", text)

    def test_current_adapted_upstream_commits_are_recorded(self):
        text = HANDLED.read_text(encoding="utf-8")
        for prefix in ("7d00ec792", "ff3e2d00b", "eee739ed7", "becdc5dfd"):
            self.assertIn(prefix, text)


if __name__ == "__main__":
    unittest.main()
