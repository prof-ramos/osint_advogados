#!/usr/bin/env python3
"""
tests/test_ci_workflow.py - Validação automatizada da configuração do GitHub Actions.
"""

import os
import unittest

REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
WORKFLOW_FILE = os.path.join(REPO_ROOT, ".github", "workflows", "lint_evidencias.yml")


class TestCIWorkflow(unittest.TestCase):
    """Testa a higidez do arquivo de workflow de integração contínua."""

    def test_workflow_file_exists(self):
        self.assertTrue(os.path.isfile(WORKFLOW_FILE), "O workflow lint_evidencias.yml deve existir.")

    def test_workflow_syntax_and_steps(self):
        with open(WORKFLOW_FILE, "r", encoding="utf-8") as f:
            content = f.read()

        # Verificações estruturais
        self.assertIn("name: Lint de Evidências Digitais", content)
        self.assertIn("- main", content)
        self.assertIn("workflow_dispatch:", content)
        self.assertIn("runs-on: ubuntu-latest", content)
        self.assertIn('python-version: "3.12"', content)
        self.assertIn("scripts/lint_evidencias.py --path casos_praticos", content)
        self.assertIn("scripts/lint_evidencias.py --path livro", content)
        self.assertIn("python3 -m unittest discover -s tests -v", content)


if __name__ == "__main__":
    unittest.main()
