#!/usr/bin/env python3
"""
tests/test_doctrinal_structure.py - Testes de integridade dogmática, 24 capítulos e boxes pedagógicos.
"""

import glob
import os
import re
import unittest

REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
LIVRO_DIR = os.path.join(REPO_ROOT, "livro")


class TestDoctrinalStructure(unittest.TestCase):
    """Verifica a presença dos 24 capítulos, acórdãos vinculantes e formatação dos boxes didáticos."""

    def test_twenty_four_chapters_exist(self):
        """O livro deve conter exatamente 24 capítulos (cap_01 a cap_24) mais a apresentação."""
        all_chapters = glob.glob(os.path.join(LIVRO_DIR, "**", "cap_*.md"), recursive=True)
        self.assertEqual(len(all_chapters), 24, f"Esperados 24 capítulos, encontrados: {len(all_chapters)}")

        sumario_path = os.path.join(LIVRO_DIR, "00_sumario_e_apresentacao.md")
        self.assertTrue(os.path.isfile(sumario_path), "Arquivo 00_sumario_e_apresentacao.md deve existir.")

    def test_alert_boxes_syntax(self):
        """Verifica se todos os alertas GitHub (> [!NOTE], etc.) possuem sintaxe válida sem quebra."""
        alert_pattern = re.compile(r"^>\s*\[!(NOTE|TIP|IMPORTANT|WARNING|CAUTION)\]")
        all_md = glob.glob(os.path.join(LIVRO_DIR, "**", "*.md"), recursive=True)

        for fpath in all_md:
            rel = os.path.relpath(fpath, REPO_ROOT)
            with open(fpath, "r", encoding="utf-8") as f:
                in_alert = False
                for line_num, line in enumerate(f, start=1):
                    if alert_pattern.match(line):
                        in_alert = True
                    elif in_alert:
                        if line.strip() == "":
                            in_alert = False
                        elif not line.startswith(">"):
                            self.fail(
                                f"Linha quebrada dentro de alerta no arquivo {rel}:{line_num}: '{line.strip()}'"
                            )

    def test_jurisprudence_presence_in_key_chapters(self):
        """Garante a permanência de precedentes fundamentais nos capítulos aprofundados."""
        key_checks = {
            "cap_04_prova_digital_cadeia_custodia_mesmidade.md": ["828.054", "Pacote Anticrime", "158-A"],
            "cap_16_localizacao_devedores_execucao.md": ["REsp 2.026.925/SP", "Tema 1137", "ADI 5941"],
            "cap_17_investigacao_patrimonial_rastreamento_bens.md": ["Tema 769", "REsp 1.666.542/SP"],
            "cap_18_fraude_contra_credores_ocultacao_patrimonial.md": ["Súmula 375", "Tema 243", "Art. 792"],
            "cap_19_direito_familia_execucao_alimentos.md": ["1.834.120", "Teoria da Aparência"],
            "cap_20_ilicitos_ciberneticos_atribuicao_redes.md": ["1.784.156", "CGNAT", "99.735"],
            "cap_21_due_diligence_compliance_risco.md": ["Tema 01", "Súmula 440", "1.146"],
            "cap_22_quando_osint_e_insuficiente_medidas_judiciais.md": ["381", "SNIPER", "SISBAJUD"],
        }

        for fname, terms in key_checks.items():
            matches = glob.glob(os.path.join(LIVRO_DIR, "**", fname), recursive=True)
            self.assertTrue(len(matches) > 0, f"Arquivo {fname} não encontrado.")
            with open(matches[0], "r", encoding="utf-8") as f:
                content = f.read()
            for t in terms:
                self.assertIn(t, content, f"Termo '{t}' ausente em {fname}")


if __name__ == "__main__":
    unittest.main()
