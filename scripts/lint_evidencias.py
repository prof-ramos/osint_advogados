#!/usr/bin/env python3
"""
scripts/lint_evidencias.py - Linter para validação de evidências digitais em OSINT Jurídico.

Verifica:
1. Integridade e formato dos hashes SHA-256 (exatamente 64 caracteres hexadecimais, sem truncamento ou hash vazio).
2. Padrão de identificadores de evidência (estritamente EVD-\\d{3}, ex: EVD-001).
3. Especificação de fuso horário em carimbos temporais de custódia (BRT, UTC-3, UTC, Z, etc.).
4. Nomeação explícita de arquivo com extensão preservada na cadeia de custódia.
"""

import argparse
import glob
import os
import re
import sys

EMPTY_SHA256 = "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855"
EVD_ID_STRICT_PATTERN = re.compile(r"^EVD-\d{3}$")
EVD_ID_ANY_PATTERN = re.compile(r"\bEVD-[\w-]+\b")
HASH_SHA256_EXTRACT = re.compile(r"SHA-256:\s*`?([a-zA-Z0-9._-]+)`?", re.IGNORECASE)
TIMEZONE_PATTERN = re.compile(r"(BRT|UTC(?:[+-]\d{1,2})?|GMT|Z|[+-]\d{2}:?\d{2})", re.IGNORECASE)
FILE_EXT_PATTERN = re.compile(r"`[^`]+\.(pdf|png|jpe?g|mp4|html|warc|txt|json|csv|zip|eml|har|pcap|log)`", re.IGNORECASE)


def check_file(file_path: str) -> list[dict]:
    issues = []
    with open(file_path, "r", encoding="utf-8") as f:
        lines = f.readlines()

    for line_num, line in enumerate(lines, start=1):
        # 1. Checagem de identificadores EVD
        evd_matches = EVD_ID_ANY_PATTERN.findall(line)
        for evd_id in evd_matches:
            if not EVD_ID_STRICT_PATTERN.match(evd_id):
                issues.append({
                    "file": file_path,
                    "line": line_num,
                    "type": "ID_FORMAT_ERROR",
                    "detail": f"Identificador de evidência '{evd_id}' fora do padrão de 3 dígitos (deve ser EVD-\\d{{3}}, ex: EVD-001)."
                })

        # 2. Checagem de Hashes SHA-256
        hash_matches = HASH_SHA256_EXTRACT.findall(line)
        for h in hash_matches:
            clean_hash = h.strip("`").strip()
            if "..." in clean_hash or "…" in clean_hash:
                issues.append({
                    "file": file_path,
                    "line": line_num,
                    "type": "TRUNCATED_HASH",
                    "detail": f"Hash SHA-256 truncado encontrado: '{clean_hash}'. É proibido usar reticências."
                })
            elif len(clean_hash) != 64 or not all(c in "0123456789abcdefABCDEF" for c in clean_hash):
                issues.append({
                    "file": file_path,
                    "line": line_num,
                    "type": "INVALID_SHA256_FORMAT",
                    "detail": f"Hash SHA-256 com tamanho ou caracteres inválidos ({len(clean_hash)} chars): '{clean_hash}'."
                })
            elif clean_hash.lower() == EMPTY_SHA256:
                issues.append({
                    "file": file_path,
                    "line": line_num,
                    "type": "EMPTY_STRING_HASH",
                    "detail": "Hash SHA-256 corresponde à string vazia (e3b0c442...855). Deve refletir um arquivo real."
                })

        # 3. Se for uma linha de tabela de evidência horizontal (contém ID EVD e múltiplas colunas)
        if ("| **EVD-" in line or "| EVD-" in line) and line.count("|") >= 5:
            # Checar fuso horário na data da evidência
            if not TIMEZONE_PATTERN.search(line):
                issues.append({
                    "file": file_path,
                    "line": line_num,
                    "type": "MISSING_TIMEZONE",
                    "detail": "Carimbo de data/hora na matriz de evidências sem indicação explícita de fuso horário (ex: BRT, UTC-3)."
                })
            # Checar menção a arquivo preservado
            if "Arquivo" in line and not FILE_EXT_PATTERN.search(line):
                issues.append({
                    "file": file_path,
                    "line": line_num,
                    "type": "MISSING_FILE_EXTENSION",
                    "detail": "Arquivo na coluna de preservação sem extensão explícita entre crases (ex: `arquivo.pdf`)."
                })
        elif ("Data / Hora" in line or "Data/Hora" in line) and not line.strip().startswith("| ID") and not "| :---" in line:
            # Em tabelas verticais com valor de data real (ex: 2026- ou DD/MM/AAAA)
            if re.search(r"\b\d{4}[-/]\d{2}[-/]\d{2}\b|\b\d{2}/\d{2}/\d{4}\b", line) and not TIMEZONE_PATTERN.search(line):
                issues.append({
                    "file": file_path,
                    "line": line_num,
                    "type": "MISSING_TIMEZONE",
                    "detail": "Carimbo de data/hora sem indicação explícita de fuso horário (ex: BRT, UTC-3, ISO offset)."
                })

    return issues


def main():
    parser = argparse.ArgumentParser(description="Linter de Evidências Digitais e Cadeia de Custódia")
    parser.add_argument("--path", default="casos_praticos", help="Diretório ou arquivo a ser analisado")
    parser.add_argument("--strict", action="store_true", default=True, help="Retorna código de saída 1 em caso de erro")
    args = parser.parse_args()

    target_path = args.path
    if os.path.isfile(target_path):
        files = [target_path]
    elif os.path.isdir(target_path):
        files = sorted(glob.glob(os.path.join(target_path, "**", "*.md"), recursive=True))
    else:
        print(f"Erro: Caminho '{target_path}' não encontrado.")
        sys.exit(2)

    total_issues = 0
    files_with_issues = 0

    print(f"=== Linter de Evidências Digitais OSINT ===")
    print(f"Examinando {len(files)} arquivo(s) em '{target_path}'...\n")

    for fpath in files:
        issues = check_file(fpath)
        if issues:
            files_with_issues += 1
            total_issues += len(issues)
            print(f"❌ {fpath} ({len(issues)} problema(s)):")
            for issue in issues:
                print(f"   [L{issue['line']}] [{issue['type']}] {issue['detail']}")
            print()

    if total_issues == 0:
        print(f"✅ Sucesso! Todos os {len(files)} arquivo(s) passaram nas verificações de integridade de evidência.")
        sys.exit(0)
    else:
        print(f"⚠️ Foram encontrados {total_issues} problema(s) em {files_with_issues} arquivo(s).")
        if args.strict:
            sys.exit(1)


if __name__ == "__main__":
    main()
