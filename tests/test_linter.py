#!/usr/bin/env python3
"""
tests/test_linter.py - Testes unitários para o motor de validação de evidências forenses.
"""

import os
import sys
import tempfile
import unittest

REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if os.path.join(REPO_ROOT, "scripts") not in sys.path:
    sys.path.insert(0, os.path.join(REPO_ROOT, "scripts"))

from lint_evidencias import (
    check_file,
    EMPTY_SHA256,
    EVD_ID_STRICT_PATTERN,
    TIMEZONE_PATTERN,
    FILE_EXT_PATTERN,
)


class TestLinterUnit(unittest.TestCase):
    """Testes unitários isolados para regras de validação forense."""

    def _check_snippet(self, snippet: str, filename: str = "test.md") -> list[dict]:
        temp_dir = tempfile.mkdtemp()
        temp_path = os.path.join(temp_dir, filename)
        with open(temp_path, "w", encoding="utf-8") as tf:
            tf.write(snippet)
        try:
            return check_file(temp_path)
        finally:
            if os.path.exists(temp_path):
                os.remove(temp_path)
            if os.path.exists(temp_dir):
                os.rmdir(temp_dir)

    def test_truncated_hashes_detected(self):
        """Verifica detecção de hashes truncados com reticências ou reticências unicode."""
        cases = [
            "Evidência SHA-256: `4a3b...c89d`",
            "Evidência SHA-256: `4a3b…c89d`",
            "Hash: 4a3b...c89d",
            "hash: `4a3b...c89d`",
            "sha-256: `4a3b...c89d`",
        ]
        for snip in cases:
            with self.subTest(snippet=snip):
                issues = self._check_snippet(snip)
                self.assertTrue(
                    any(i["type"] == "TRUNCATED_HASH" for i in issues),
                    f"Falha ao detectar hash truncado em: {snip}",
                )

    def test_empty_string_hash_detected(self):
        """Verifica proibição do hash correspondente à string vazia."""
        snip = f"Evidência SHA-256: `{EMPTY_SHA256}`"
        issues = self._check_snippet(snip)
        self.assertTrue(
            any(i["type"] == "EMPTY_STRING_HASH" for i in issues),
            "Deveria rejeitar hash de string vazia",
        )

    def test_invalid_hash_lengths_and_chars(self):
        """Verifica rejeição de hashes com menos ou mais de 64 caracteres, ou caracteres não hex."""
        invalid_hashes = [
            "a" * 63,
            "a" * 65,
            ("a" * 63) + "g",
            ("a" * 63) + "Z",
        ]
        for h in invalid_hashes:
            with self.subTest(hash_val=h):
                snip = f"Evidência SHA-256: `{h}`"
                issues = self._check_snippet(snip)
                self.assertTrue(
                    any(i["type"] == "INVALID_SHA256_FORMAT" for i in issues),
                    f"Deveria rejeitar hash inválido: {h}",
                )

    def test_valid_64_char_hash_allowed(self):
        """Verifica aceitação de hashes de 64 hexadecimais válidos."""
        valid_hash = "d54d9b23b49c7be7708579d4fdc7bc5ef44c3c3a4f6cf70e340c4974fa2e1c93"
        for prefix in ["SHA-256:", "Hash:", "sha-256:", "hash:"]:
            with self.subTest(prefix=prefix):
                snip = f"Evidência {prefix} `{valid_hash}`"
                issues = self._check_snippet(snip)
                self.assertEqual(
                    len(issues), 0, f"Hash válido foi rejeitado com prefixo {prefix}: {issues}"
                )

    def test_evidence_id_formatting(self):
        """Verifica o formato estrito EVD-\\d{3}."""
        invalid_ids = ["EVD-1", "EVD-01", "EVD-0001", "EVD-ABCD", "evd-001"]
        for bad_id in invalid_ids:
            with self.subTest(bad_id=bad_id):
                snip = f"Item {bad_id} registrado."
                issues = self._check_snippet(snip)
                self.assertTrue(
                    any(i["type"] == "ID_FORMAT_ERROR" for i in issues),
                    f"Deveria rejeitar ID inválido: {bad_id}",
                )

        valid_ids = ["EVD-001", "EVD-042", "EVD-999"]
        for good_id in valid_ids:
            with self.subTest(good_id=good_id):
                snip = f"Item {good_id} registrado com sucesso."
                issues = self._check_snippet(snip)
                self.assertEqual(
                    len(issues), 0, f"ID válido foi rejeitado: {good_id}"
                )

    def test_horizontal_table_validation(self):
        """Verifica validação de fuso horário e extensão de arquivo em tabelas de evidência."""
        valid_hash = "a" * 64
        # Sem timezone
        snip_no_tz = f"| **EVD-001** | Item | 2026-05-10 14:00 | Fonte | `arquivo.pdf` | SHA-256: `{valid_hash}` |"
        issues = self._check_snippet(snip_no_tz)
        self.assertTrue(any(i["type"] == "MISSING_TIMEZONE" for i in issues))

        # Sem extensão
        snip_no_ext = f"| **EVD-001** | Item | 2026-05-10 14:00 BRT | Fonte | Arquivo Sem Extensao | SHA-256: `{valid_hash}` |"
        issues = self._check_snippet(snip_no_ext)
        self.assertTrue(any(i["type"] == "MISSING_FILE_EXTENSION" for i in issues))

        # Válido
        snip_ok = f"| **EVD-001** | Item | 2026-05-10 14:00 BRT | Fonte | `evidencia.pdf` | SHA-256: `{valid_hash}` |"
        issues = self._check_snippet(snip_ok)
        self.assertEqual(len(issues), 0, f"Tabela válida rejeitada: {issues}")

    def test_normative_files_ignored(self):
        """Garante que CODING_STANDARDS.md e AGENTS.md são ignorados pelo linter."""
        snip = "Exemplo proibido: EVD-1 e SHA-256: `4a3b...c89d`"
        issues_coding = self._check_snippet(snip, filename="CODING_STANDARDS.md")
        self.assertEqual(len(issues_coding), 0)
        issues_agents = self._check_snippet(snip, filename="AGENTS.md")
        self.assertEqual(len(issues_agents), 0)


if __name__ == "__main__":
    unittest.main()
