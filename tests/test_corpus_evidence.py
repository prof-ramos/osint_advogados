#!/usr/bin/env python3
"""
tests/test_corpus_evidence.py - Testes de regressão forense sobre todo o acervo do repositório.
"""

import glob
import os
import re
import sys
import unittest

REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if os.path.join(REPO_ROOT, "scripts") not in sys.path:
    sys.path.insert(0, os.path.join(REPO_ROOT, "scripts"))

from lint_evidencias import (
    check_file,
    EMPTY_SHA256,
    EVD_ID_STRICT_PATTERN,
    TIMEZONE_PATTERN,
)


class TestCorpusEvidence(unittest.TestCase):
    """Varre todo o acervo real de markdown (casos_praticos e livro) garantindo conformidade forense."""

    @classmethod
    def setUpClass(cls):
        cls.target_dirs = [
            os.path.join(REPO_ROOT, "casos_praticos"),
            os.path.join(REPO_ROOT, "livro"),
        ]
        cls.all_files = []
        for d in cls.target_dirs:
            cls.all_files.extend(sorted(glob.glob(os.path.join(d, "**", "*.md"), recursive=True)))

    def test_all_files_pass_linter(self):
        """Todos os arquivos reais em casos_praticos e livro devem ter 0 erros no check_file()."""
        all_issues = []
        for fpath in self.all_files:
            rel = os.path.relpath(fpath, REPO_ROOT)
            issues = check_file(fpath)
            for iss in issues:
                all_issues.append((rel, iss))

        self.assertEqual(
            len(all_issues),
            0,
            f"Erros de linter encontrados no repositório: {all_issues}",
        )

    def test_no_non_conforming_evd_identifiers(self):
        """Varredura independente para garantir que nenhum identificador foge a EVD-\\d{3}."""
        evd_broad_pattern = re.compile(r"(?i)\b(?:EVD|evd)[_-]?[0-9a-zA-Z]+\b")
        violations = []

        for fpath in self.all_files:
            rel = os.path.relpath(fpath, REPO_ROOT)
            with open(fpath, "r", encoding="utf-8") as f:
                for line_num, line in enumerate(f, start=1):
                    for evd in evd_broad_pattern.findall(line):
                        if not EVD_ID_STRICT_PATTERN.match(evd):
                            violations.append((rel, line_num, evd))

        self.assertEqual(
            len(violations),
            0,
            f"Identificadores EVD fora do padrão encontrados: {violations}",
        )

    def test_no_truncated_or_empty_hashes(self):
        """Varredura independente para garantir inexistência de reticências ou hashes vazios."""
        ellipsis_pattern = re.compile(
            r"(?i)(?:sha-?256|hash)[:\s=]+`?[0-9a-zA-Z._-]*(\.\.\.|…)[0-9a-zA-Z._-]*`?"
        )
        hex64_pattern = re.compile(r"\b[0-9a-fA-F]{64}\b")

        ellipsis_violations = []
        empty_hash_violations = []

        for fpath in self.all_files:
            rel = os.path.relpath(fpath, REPO_ROOT)
            with open(fpath, "r", encoding="utf-8") as f:
                for line_num, line in enumerate(f, start=1):
                    if ellipsis_pattern.search(line):
                        ellipsis_violations.append((rel, line_num, line.strip()))
                    for h in hex64_pattern.findall(line):
                        if h.lower() == EMPTY_SHA256:
                            empty_hash_violations.append((rel, line_num, h))

        self.assertEqual(
            len(ellipsis_violations),
            0,
            f"Hashes truncados com reticências encontrados: {ellipsis_violations}",
        )
        self.assertEqual(
            len(empty_hash_violations),
            0,
            f"Hashes de string vazia encontrados: {empty_hash_violations}",
        )


if __name__ == "__main__":
    unittest.main()
