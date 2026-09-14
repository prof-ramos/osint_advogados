#!/usr/bin/env python3
"""
Script de Extração Seletiva do Acervo Eduardo Belisário para OSINT Jurídico.
Extrai blocos temáticos de Prova Digital, Cadeia de Custódia, Execução e Medidas Restritas
gerando um catálogo consolidado para o Curso de 72h e suporte ao livro.
"""

import os
import re
import zipfile
import xml.etree.ElementTree as ET

W_NAMESPACE = "{http://schemas.openxmlformats.org/wordprocessingml/2006/main}"


def extract_text_from_docx(docx_path: str) -> list[str]:
    """Extrai parágrafos de texto de um arquivo docx preservando a ordem."""
    if not os.path.exists(docx_path):
        return []
    paragraphs = []
    try:
        with zipfile.ZipFile(docx_path) as z:
            xml_content = z.read("word/document.xml")
            tree = ET.fromstring(xml_content)
            for p in tree.iter(f"{W_NAMESPACE}p"):
                texts = [
                    node.text
                    for node in p.iter(f"{W_NAMESPACE}t")
                    if node.text is not None
                ]
                text = "".join(texts).strip()
                if text:
                    paragraphs.append(text)
    except Exception as e:
        print(f"Erro ao ler {docx_path}: {e}")
    return paragraphs


def filter_cpp_chain_of_custody(paragraphs: list[str]) -> list[str]:
    """Filtra blocos de cadeia de custódia (CPP 158-A a 158-F) e julgados correlatos."""
    in_block = False
    extracted = []
    for p in paragraphs:
        if re.search(r"Art\.\s*158-[A-F]", p, re.IGNORECASE):
            in_block = True
        elif in_block and re.search(r"Art\.\s*159", p, re.IGNORECASE):
            in_block = False

        if in_block:
            extracted.append(p)
    return extracted


def filter_cpc_execution_and_proofs(paragraphs: list[str]) -> list[str]:
    """Filtra blocos do CPC: arts. 139, IV; 381 a 383; 792 e 828."""
    extracted = []
    current_topic = None
    buffer = []

    for p in paragraphs:
        if "Art. 139." in p or "Art. 139 " in p:
            current_topic = "Art. 139"
            buffer = [p]
        elif current_topic == "Art. 139":
            if "Art. 140" in p:
                extracted.extend(buffer)
                current_topic = None
                buffer = []
            else:
                buffer.append(p)

        elif "Art. 381." in p or "Art. 381 " in p:
            current_topic = "Art. 381"
            buffer = [p]
        elif current_topic == "Art. 381":
            if "Art. 384" in p:
                extracted.extend(buffer)
                current_topic = None
                buffer = []
            else:
                buffer.append(p)

        elif "Art. 792." in p or "Art. 792 " in p:
            current_topic = "Art. 792"
            buffer = [p]
        elif current_topic == "Art. 792":
            if "Art. 793" in p:
                extracted.extend(buffer)
                current_topic = None
                buffer = []
            else:
                buffer.append(p)

    return extracted


def filter_mci_logs_and_cgnat(paragraphs: list[str]) -> list[str]:
    """Filtra blocos do Marco Civil: arts. 10 a 15 e art. 22."""
    extracted = []
    current_topic = None
    buffer = []

    for p in paragraphs:
        if "Art. 10." in p or "Art. 10 " in p:
            current_topic = "Art. 10"
            buffer = [p]
        elif current_topic == "Art. 10":
            if "Art. 16" in p:
                extracted.extend(buffer)
                current_topic = None
                buffer = []
            else:
                buffer.append(p)

        elif "Art. 22." in p or "Art. 22 " in p:
            current_topic = "Art. 22"
            buffer = [p]
        elif current_topic == "Art. 22":
            if "Art. 23" in p:
                extracted.extend(buffer)
                current_topic = None
                buffer = []
            else:
                buffer.append(p)

    return extracted


def filter_lgpd(paragraphs: list[str]) -> list[str]:
    """Filtra blocos da LGPD: arts. 4º e 7º."""
    extracted = []
    current_topic = None
    buffer = []

    for p in paragraphs:
        if "Art. 4º" in p or "Art. 4." in p:
            current_topic = "Art. 4"
            buffer = [p]
        elif current_topic == "Art. 4":
            if "Art. 5" in p:
                extracted.extend(buffer)
                current_topic = None
                buffer = []
            else:
                buffer.append(p)

        elif "Art. 7º" in p or "Art. 7." in p:
            current_topic = "Art. 7"
            buffer = [p]
        elif current_topic == "Art. 7":
            if "Art. 8" in p:
                extracted.extend(buffer)
                current_topic = None
                buffer = []
            else:
                buffer.append(p)

    return extracted


def format_markdown_section(title: str, paragraphs: list[str]) -> str:
    md = [f"\n## {title}\n"]
    for p in paragraphs:
        if p.startswith("#Atenção") or p.startswith("# Jurisprudência") or p.startswith("# Súmula"):
            md.append(f"\n> [!NOTE]\n> ### {p}\n")
        elif re.search(r"^\([A-Z0-9\-/]+\)", p):  # Banca/Concurso
            md.append(f"\n#### 📝 {p}\n")
        elif p.startswith("BL:") or p.startswith("Gabarito:"):
            md.append(f"> **{p}**\n")
        else:
            md.append(f"{p}\n")
    return "\n".join(md)


def main():
    base_path = "/tmp/belisa_eval/03_organizado_por_materia"
    if not os.path.exists(base_path):
        print(f"Diretório {base_path} não encontrado!")
        return

    output_dir = "curso"
    os.makedirs(output_dir, exist_ok=True)
    output_file = os.path.join(output_dir, "banco_questoes_e_jurisprudencia_osint.md")

    content = [
        "# Banco Didático de Questões e Jurisprudência Aplicada ao OSINT Jurídico",
        "",
        "> **Origem e Curadoria**: Extração seletiva do acervo *Eduardo Belisário* (Legislação Grifada e Concursos de Carreiras Jurídicas de Estado), filtrada e adaptada para a disciplina de OSINT Jurídico, Investigação Defensiva e Prova Digital.",
        "> **Finalidade**: Alimentar o caderno de exercícios práticos, quizzes e aprofundamento jurisprudencial do curso de 72h e capítulos do manual.",
        "",
        "---"
    ]

    # 1. CPP - Prova Digital e Cadeia de Custódia
    cpp_file = os.path.join(base_path, "direito_processual_penal/legislacao_grifada/cpp_atualiz_01_de_julho.docx")
    if os.path.exists(cpp_file):
        print("Processando CPP...")
        cpp_p = extract_text_from_docx(cpp_file)
        cpp_filtered = filter_cpp_chain_of_custody(cpp_p)
        content.append(format_markdown_section("1. Cadeia de Custódia da Prova Digital (CPP, Arts. 158-A a 158-F)", cpp_filtered))

    # 2. CPC - Execução, Medidas Atípicas e Produção Antecipada
    cpc_file = os.path.join(base_path, "direito_processual_civil/legislacao_grifada/cpc_de_2015_atualiz_29_de_junho.docx")
    if os.path.exists(cpc_file):
        print("Processando CPC...")
        cpc_p = extract_text_from_docx(cpc_file)
        cpc_filtered = filter_cpc_execution_and_proofs(cpc_p)
        content.append(format_markdown_section("2. Processo Civil: Medidas Atípicas, Produção Antecipada e Fraude à Execução", cpc_filtered))

    # 3. Marco Civil da Internet
    mci_file = os.path.join(base_path, "direito_administrativo/legislacao_grifada/marco_civil_da_internet_lei_12965.docx")
    if os.path.exists(mci_file):
        print("Processando Marco Civil da Internet...")
        mci_p = extract_text_from_docx(mci_file)
        mci_filtered = filter_mci_logs_and_cgnat(mci_p)
        content.append(format_markdown_section("3. Marco Civil da Internet: Guarda de Logs, Quebra de Sigilo e CGNAT (Lei 12.965/2014)", mci_filtered))

    # 4. LGPD
    lgpd_file = os.path.join(base_path, "direito_constitucional_dh_internacional/legislacao_grifada/lei_geral_de_protecao_de_dados_pessoais_lei_13_709.docx")
    if os.path.exists(lgpd_file):
        print("Processando LGPD...")
        lgpd_p = extract_text_from_docx(lgpd_file)
        lgpd_filtered = filter_lgpd(lgpd_p)
        content.append(format_markdown_section("4. LGPD: Exceções à Proteção de Dados e Tratamento para Exercício Regular de Direitos (Lei 13.709/2018)", lgpd_filtered))

    with open(output_file, "w", encoding="utf-8") as f:
        f.write("\n".join(content))

    print(f"Arquivo gerado com sucesso em {output_file} ({os.path.getsize(output_file)} bytes).")


if __name__ == "__main__":
    main()
