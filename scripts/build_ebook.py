#!/usr/bin/env python3
"""
scripts/build_ebook.py - Pipeline de compilação editorial do manual OSINT Jurídico.

Gera:
1. dist/osint_juridico_manual_completo.md (Monólito Markdown com metadados e sumário)
2. dist/osint_juridico_manual.html (Versão HTML diagramada para leitura e impressão PDF)
3. dist/osint_juridico_manual.epub (E-book no padrão EPUB 3)
"""

import argparse
import html
import os
import re
import sys
import zipfile
from typing import Dict, List, Tuple

REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
LIVRO_DIR = os.path.join(REPO_ROOT, "livro")

ORDERED_PARTS: List[Tuple[str, str]] = [
    ("Apresentação e Sumário", "00_sumario_e_apresentacao.md"),
    ("Parte 1: Fundamentos e Regime Jurídico", "parte_1_fundamentos_e_regime_juridico"),
    ("Parte 2: Metodologia Investigativa e Evidências", "parte_2_metodologia_investigativa_e_evidencias"),
    ("Parte 3: Técnicas Operacionais e Pivoteamento", "parte_3_tecnicas_operacionais_e_pivoteamento"),
    ("Parte 4: Aplicações Jurídicas Práticas", "parte_4_aplicacoes_juridicas_praticas"),
    ("Parte 5: Casos Práticos e Caderno de Exercícios", "parte_5_casos_praticos_e_caderno_exercicios"),
]


def get_ordered_chapter_files() -> List[Tuple[str, str]]:
    """Retorna lista ordenada de tuplas (secao_nome, caminho_absoluto_arquivo)."""
    ordered_files: List[Tuple[str, str]] = []

    # 00
    apresentacao = os.path.join(LIVRO_DIR, "00_sumario_e_apresentacao.md")
    if os.path.isfile(apresentacao):
        ordered_files.append(("Apresentação", apresentacao))

    # Partes 1 a 5
    for part_title, part_dir in ORDERED_PARTS[1:]:
        full_part_path = os.path.join(LIVRO_DIR, part_dir)
        if os.path.isdir(full_part_path):
            chapters = sorted(
                [f for f in os.listdir(full_part_path) if f.startswith("cap_") and f.endswith(".md")]
            )
            for c in chapters:
                ordered_files.append((part_title, os.path.join(full_part_path, c)))

    return ordered_files


def clean_markdown_content(raw_text: str) -> str:
    """Normaliza o markdown para compilação contínua."""
    lines = raw_text.splitlines()
    cleaned = []
    for line in lines:
        cleaned.append(line)
    return "\n".join(cleaned).strip()


def build_markdown_monolith(ordered_files: List[Tuple[str, str]], output_path: str) -> str:
    """Concatena os capítulos em um documento Markdown completo com capa e metadados."""
    header = """---
title: "OSINT Aplicado ao Direito Brasileiro"
subtitle: "Investigação em Fontes Abertas, Prova Digital e Estratégia Processual"
author: "Prof. Gabriel Ramos"
date: "2026"
version: "2.0.0"
language: "pt-BR"
rights: "Licença Acadêmica e Profissional — MIT"
---

# OSINT Aplicado ao Direito Brasileiro
### Investigação em Fontes Abertas, Prova Digital e Estratégia Processual

**Autor**: Prof. Gabriel Ramos  
**Edição**: 2026 — Edição Reconstruída e Auditada  
**Jurisdição**: Brasil 🇧🇷 (CPC, CPP, LGPD, Marco Civil da Internet e Provimento 188/2018 CFOAB)

---

<div style="page-break-after: always;"></div>

"""
    sections = [header]
    current_part = ""

    for part_title, file_path in ordered_files:
        if part_title != current_part and not part_title.startswith("Apresentação"):
            current_part = part_title
            sections.append(f"\n\n<div style=\"page-break-before: always;\"></div>\n\n# {part_title}\n\n---\n")

        with open(file_path, "r", encoding="utf-8") as f:
            content = clean_markdown_content(f.read())
            sections.append(f"\n\n<div style=\"page-break-before: always;\"></div>\n\n{content}")

    monolith = "\n".join(sections)
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(monolith)

    return monolith


def render_simple_markdown_to_html(md_text: str) -> str:
    """Converte Markdown estruturado para HTML semântico com estilização dos 8 boxes didáticos."""
    lines = md_text.splitlines()
    html_lines = []
    in_code_block = False
    in_alert_block = False
    alert_type = ""
    in_table = False

    for line in lines:
        stripped = line.strip()

        # Fenced code blocks
        if stripped.startswith("```"):
            if in_code_block:
                html_lines.append("</code></pre>")
                in_code_block = False
            else:
                lang = stripped[3:].strip()
                html_lines.append(f'<pre class="code-block {lang}"><code>')
                in_code_block = True
            continue

        if in_code_block:
            html_lines.append(html.escape(line))
            continue

        # Page breaks
        if "page-break" in stripped:
            html_lines.append('<div class="page-break"></div>')
            continue

        # Horizontal rule
        if stripped in ("---", "***", "___"):
            html_lines.append("<hr />")
            continue

        # Headers
        if stripped.startswith("# "):
            html_lines.append(f"<h1>{html.escape(stripped[2:])}</h1>")
            continue
        elif stripped.startswith("## "):
            html_lines.append(f"<h2>{html.escape(stripped[3:])}</h2>")
            continue
        elif stripped.startswith("### "):
            html_lines.append(f"<h3>{html.escape(stripped[4:])}</h3>")
            continue
        elif stripped.startswith("#### "):
            html_lines.append(f"<h4>{html.escape(stripped[5:])}</h4>")
            continue

        # Alerts (> [!NOTE], etc.)
        alert_match = re.match(r"^>\s*\[!(NOTE|TIP|IMPORTANT|WARNING|CAUTION)\]", stripped)
        if alert_match:
            alert_type = alert_match.group(1).lower()
            html_lines.append(f'<div class="admonition alert-{alert_type}">')
            in_alert_block = True
            continue

        if in_alert_block:
            if stripped.startswith(">"):
                alert_line = stripped[1:].strip()
                if alert_line.startswith("### "):
                    html_lines.append(f'<div class="alert-title">{html.escape(alert_line[4:])}</div>')
                else:
                    html_lines.append(f"<p>{html.escape(alert_line)}</p>")
                continue
            elif stripped == "":
                html_lines.append("</div>")
                in_alert_block = False
            else:
                html_lines.append("</div>")
                in_alert_block = False

        # Tables
        if "|" in stripped and stripped.startswith("|"):
            if not in_table:
                html_lines.append('<div class="table-container"><table>')
                in_table = True
            if ":---" in stripped or "---:" in stripped:
                continue
            cols = [c.strip() for c in stripped.strip("|").split("|")]
            html_lines.append("<tr>" + "".join(f"<td>{html.escape(c)}</td>" for c in cols) + "</tr>")
            continue
        elif in_table:
            html_lines.append("</table></div>")
            in_table = False

        if stripped:
            html_lines.append(f"<p>{html.escape(stripped)}</p>")
        else:
            html_lines.append("")

    if in_table:
        html_lines.append("</table></div>")
    if in_alert_block:
        html_lines.append("</div>")

    return "\n".join(html_lines)


def build_html_book(md_content: str, output_path: str) -> None:
    """Gera um arquivo HTML completo e diagramado para impressão em PDF de alta qualidade."""
    body_content = render_simple_markdown_to_html(md_content)

    html_doc = f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>OSINT Aplicado ao Direito Brasileiro</title>
    <style>
        :root {{
            --font-main: 'Segoe UI', -apple-system, BlinkMacSystemFont, Roboto, Helvetica, Arial, sans-serif;
            --font-code: 'SFMono-Regular', Consolas, 'Liberation Mono', Menlo, monospace;
            --color-text: #1a202c;
            --color-bg: #ffffff;
            --color-border: #e2e8f0;
            --color-primary: #1e3a8a;
            --color-secondary: #0d9488;
        }}
        @page {{
            size: A4;
            margin: 2.5cm 2cm 2.5cm 2cm;
            @bottom-right {{
                content: counter(page);
                font-family: var(--font-main);
                font-size: 9pt;
            }}
        }}
        body {{
            font-family: var(--font-main);
            color: var(--color-text);
            background-color: var(--color-bg);
            line-height: 1.65;
            font-size: 11pt;
            margin: 0 auto;
            max-width: 860px;
            padding: 2rem 1rem;
        }}
        h1 {{
            color: var(--color-primary);
            font-size: 24pt;
            border-bottom: 2px solid var(--color-primary);
            padding-bottom: 0.3em;
            margin-top: 2em;
            page-break-before: always;
        }}
        h2 {{
            color: #2b6cb0;
            font-size: 16pt;
            border-bottom: 1px solid var(--color-border);
            padding-bottom: 0.2em;
            margin-top: 1.5em;
        }}
        h3 {{
            color: #2d3748;
            font-size: 13pt;
            margin-top: 1.2em;
        }}
        .page-break {{
            page-break-before: always;
            break-before: page;
        }}
        table {{
            width: 100%;
            border-collapse: collapse;
            margin: 1.5em 0;
            font-size: 9.5pt;
        }}
        th, td {{
            border: 1px solid var(--color-border);
            padding: 8px 12px;
            text-align: left;
        }}
        tr:nth-child(even) {{
            background-color: #f7fafc;
        }}
        /* Estilização dos 8 Boxes Pedagógicos */
        .admonition {{
            border-left: 4px solid #4a5568;
            background-color: #f8fafc;
            padding: 1rem 1.25rem;
            margin: 1.5em 0;
            border-radius: 0 6px 6px 0;
        }}
        .alert-title {{
            font-weight: bold;
            font-size: 11pt;
            margin-bottom: 0.5rem;
            color: #2d3748;
        }}
        .alert-note {{ border-color: #3b82f6; background-color: #eff6ff; }}
        .alert-tip {{ border-color: #10b981; background-color: #ecfdf5; }}
        .alert-important {{ border-color: #8b5cf6; background-color: #f5f3ff; }}
        .alert-warning {{ border-color: #f59e0b; background-color: #fffbeb; }}
        .alert-caution {{ border-color: #ef4444; background-color: #fef2f2; }}
        pre.code-block {{
            background-color: #1e293b;
            color: #f8fafc;
            padding: 1rem;
            border-radius: 6px;
            font-family: var(--font-code);
            font-size: 9pt;
            overflow-x: auto;
        }}
        code {{
            font-family: var(--font-code);
            background-color: #edf2f7;
            padding: 2px 4px;
            border-radius: 4px;
            font-size: 0.9em;
        }}
    </style>
</head>
<body>
    {body_content}
</body>
</html>
"""
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(html_doc)


def build_epub_book(ordered_files: List[Tuple[str, str]], output_path: str) -> None:
    """Gera um arquivo EPUB 3 estruturado e validado utilizando apenas a biblioteca padrão."""
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    with zipfile.ZipFile(output_path, "w") as z:
        # 1. mimetype (deve ser o primeiro arquivo e descompactado)
        z.writestr("mimetype", "application/epub+zip", compress_type=zipfile.ZIP_STORED)

        # 2. META-INF/container.xml
        container_xml = """<?xml version="1.0" encoding="UTF-8"?>
<container version="1.0" xmlns="urn:oasis:names:tc:opendocument:xmlns:container">
    <rootfiles>
        <rootfile full-path="OEBPS/content.opf" media-type="application/oebps-package+xml"/>
    </rootfiles>
</container>"""
        z.writestr("META-INF/container.xml", container_xml)

        manifest_items = []
        spine_items = []
        chapters_data = []

        for idx, (part_title, file_path) in enumerate(ordered_files, start=1):
            ch_id = f"chapter_{idx:02d}"
            ch_filename = f"{ch_id}.xhtml"
            with open(file_path, "r", encoding="utf-8") as f:
                md_content = clean_markdown_content(f.read())
            html_body = render_simple_markdown_to_html(md_content)

            xhtml_content = f"""<?xml version="1.0" encoding="utf-8"?>
<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml" xmlns:epub="http://www.idpf.org/2007/ops" xml:lang="pt-BR">
<head>
    <title>{html.escape(part_title)}</title>
    <style>
        body {{ font-family: sans-serif; line-height: 1.5; padding: 1em; }}
        h1 {{ color: #1e3a8a; }}
        h2 {{ color: #2b6cb0; }}
        .admonition {{ border-left: 4px solid #3b82f6; background-color: #f0f9ff; padding: 0.8em; margin: 1em 0; }}
        pre {{ background: #f1f5f9; padding: 0.5em; overflow: auto; }}
        table {{ border-collapse: collapse; width: 100%; }}
        td, th {{ border: 1px solid #cbd5e1; padding: 4px 8px; }}
    </style>
</head>
<body>
    {html_body}
</body>
</html>"""
            z.writestr(f"OEBPS/{ch_filename}", xhtml_content)
            manifest_items.append(f'<item id="{ch_id}" href="{ch_filename}" media-type="application/xhtml+xml"/>')
            spine_items.append(f'<itemref idref="{ch_id}"/>')
            chapters_data.append((ch_id, ch_filename, part_title))

        # 3. OEBPS/content.opf
        manifest_xml = "\n        ".join(manifest_items)
        spine_xml = "\n        ".join(spine_items)
        content_opf = f"""<?xml version="1.0" encoding="utf-8"?>
<package xmlns="http://www.idpf.org/2007/opf" version="3.0" unique-identifier="pub-id">
    <metadata xmlns:dc="http://purl.org/dc/elements/1.1/">
        <dc:identifier id="pub-id">urn:uuid:osint-advogados-manual-2026</dc:identifier>
        <dc:title>OSINT Aplicado ao Direito Brasileiro</dc:title>
        <dc:creator>Gabriel Ramos</dc:creator>
        <dc:language>pt-BR</dc:language>
        <dc:date>2026</dc:date>
    </metadata>
    <manifest>
        <item id="ncx" href="toc.ncx" media-type="application/x-dtbncx+xml"/>
        {manifest_xml}
    </manifest>
    <spine toc="ncx">
        {spine_xml}
    </spine>
</package>"""
        z.writestr("OEBPS/content.opf", content_opf)

        # 4. OEBPS/toc.ncx (compatibilidade e-readers)
        nav_points = []
        for order, (ch_id, ch_filename, part_title) in enumerate(chapters_data, start=1):
            nav_points.append(f"""    <navPoint id="navPoint-{order}" playOrder="{order}">
        <navLabel><text>{html.escape(part_title)}</text></navLabel>
        <content src="{ch_filename}"/>
    </navPoint>""")
        toc_ncx = f"""<?xml version="1.0" encoding="UTF-8"?>
<ncx xmlns="http://www.daisy.org/z3986/2005/ncx/" version="2005-1">
    <head>
        <meta name="dtb:uid" content="urn:uuid:osint-advogados-manual-2026"/>
        <meta name="dtb:depth" content="1"/>
        <meta name="dtb:totalPageCount" content="0"/>
        <meta name="dtb:maxPageNumber" content="0"/>
    </head>
    <docTitle><text>OSINT Aplicado ao Direito Brasileiro</text></docTitle>
    <navMap>
    {"\n".join(nav_points)}
    </navMap>
</ncx>"""
        z.writestr("OEBPS/toc.ncx", toc_ncx)


def main() -> None:
    parser = argparse.ArgumentParser(description="Pipeline de Compilação do E-book OSINT Jurídico")
    parser.add_argument("--outdir", default="dist", help="Diretório de saída dos artefatos")
    parser.add_argument("--formats", default="md,html,epub", help="Formatos a gerar (md, html, epub)")
    args = parser.parse_args()

    out_dir = os.path.join(REPO_ROOT, args.outdir)
    os.makedirs(out_dir, exist_ok=True)
    formats = [f.strip().lower() for f in args.formats.split(",")]

    ordered_files = get_ordered_chapter_files()
    print("=== Pipeline de Compilação do E-book OSINT Jurídico ===")
    print(f"Capítulos localizados: {len(ordered_files)}")
    print(f"Diretório de destino: {out_dir}\n")

    # 1. Monólito Markdown
    md_path = os.path.join(out_dir, "osint_juridico_manual_completo.md")
    print(f"⏳ Compilando monólito Markdown em '{md_path}'...")
    md_content = build_markdown_monolith(ordered_files, md_path)
    print(f"✅ Markdown gerado ({os.path.getsize(md_path)} bytes).")

    # 2. HTML Print-ready
    if "html" in formats:
        html_path = os.path.join(out_dir, "osint_juridico_manual.html")
        print(f"⏳ Diagramando versão HTML print-ready em '{html_path}'...")
        build_html_book(md_content, html_path)
        print(f"✅ HTML gerado ({os.path.getsize(html_path)} bytes).")

    # 3. EPUB 3
    if "epub" in formats:
        epub_path = os.path.join(out_dir, "osint_juridico_manual.epub")
        print(f"⏳ Compilando arquivo EPUB em '{epub_path}'...")
        build_epub_book(ordered_files, epub_path)
        print(f"✅ EPUB gerado ({os.path.getsize(epub_path)} bytes).")

    print("\n🎉 Compilação editorial concluída com sucesso!")


if __name__ == "__main__":
    main()
