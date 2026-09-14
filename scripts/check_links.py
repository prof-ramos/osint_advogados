#!/usr/bin/env python3
"""
scripts/check_links.py - Auditoria e validação de higidez de links na Base Dinâmica e Datasets.

Verifica:
1. Sintaxe de links Markdown [texto](url).
2. Protocolos válidos (https://, http://, file://, mailto:).
3. Links vazios ou âncoras quebradas.
4. Opcionalmente (--online), efetua checagem HTTP HEAD/GET de vivacidade com timeout.
"""

import argparse
import glob
import json
import os
import re
import sys
import urllib.request
import urllib.error
from typing import Any, Dict, List, Tuple

MD_LINK_PATTERN: re.Pattern = re.compile(r"\[([^\]]+)\]\(([^)]+)\)")
VALID_SCHEMES: Tuple[str, ...] = ("https://", "http://", "file://", "mailto:", "#", "../", "./")


def extract_links_from_file(file_path: str) -> List[Dict[str, Any]]:
    """Extrai todos os links markdown de um arquivo com número de linha e texto âncora."""
    links: List[Dict[str, Any]] = []
    with open(file_path, "r", encoding="utf-8") as f:
        for line_num, line in enumerate(f, start=1):
            matches = MD_LINK_PATTERN.findall(line)
            for text, url in matches:
                url_clean = url.strip()
                links.append({
                    "file": file_path,
                    "line": line_num,
                    "text": text.strip(),
                    "url": url_clean,
                })
    return links


def validate_link_syntax(link_info: Dict[str, Any]) -> List[Dict[str, Any]]:
    """Valida a estrutura do link (sintaxe, protocolo, formato)."""
    issues: List[Dict[str, Any]] = []
    url = link_info["url"]

    if not url:
        issues.append({
            "file": link_info["file"],
            "line": link_info["line"],
            "type": "EMPTY_URL",
            "detail": f"Link com texto '{link_info['text']}' possui URL vazia.",
        })
        return issues

    if not any(url.startswith(scheme) for scheme in VALID_SCHEMES):
        issues.append({
            "file": link_info["file"],
            "line": link_info["line"],
            "type": "UNKNOWN_SCHEME",
            "detail": f"URL '{url}' não inicia com esquema conhecido (https, http, file, etc.).",
        })

    if " " in url:
        issues.append({
            "file": link_info["file"],
            "line": link_info["line"],
            "type": "SPACE_IN_URL",
            "detail": f"URL '{url}' contém espaços em branco não codificados.",
        })

    return issues


def check_url_online(url: str, timeout: int = 5) -> Tuple[bool, int, str]:
    """Verifica se uma URL HTTP(S) responde com código 2xx ou 3xx."""
    if not url.startswith(("http://", "https://")):
        return True, 200, "Skipped (non-http)"

    req = urllib.request.Request(
        url,
        headers={"User-Agent": "OSINT-Juridico-LinkChecker/1.0 (+https://github.com/prof-ramos/osint_advogados)"},
        method="HEAD",
    )
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            return True, resp.status, "OK"
    except urllib.error.HTTPError as e:
        # Alguns servidores rejeitam HEAD com 403/405; tentar GET
        if e.code in (403, 405):
            try:
                get_req = urllib.request.Request(
                    url,
                    headers={"User-Agent": "OSINT-Juridico-LinkChecker/1.0"},
                    method="GET",
                )
                with urllib.request.urlopen(get_req, timeout=timeout) as resp:
                    return True, resp.status, "OK"
            except Exception as e2:
                return False, getattr(e2, "code", 0), str(e2)
        return False, e.code, str(e)
    except Exception as e:
        return False, 0, str(e)


def main() -> None:
    parser = argparse.ArgumentParser(description="Auditor e Validador de Links da Base Dinâmica")
    parser.add_argument("--path", default="base_dinamica", help="Diretório ou arquivo markdown a verificar")
    parser.add_argument("--online", action="store_true", help="Realiza checagem HTTP ativa (requer conexão)")
    parser.add_argument("--timeout", type=int, default=5, help="Timeout em segundos para checagem online")
    parser.add_argument("--format", choices=["text", "json"], default="text", help="Formato da saída")
    args = parser.parse_args()

    target = args.path
    if os.path.isfile(target):
        files = [target]
    elif os.path.isdir(target):
        files = sorted(glob.glob(os.path.join(target, "**", "*.md"), recursive=True))
    else:
        print(f"Erro: Caminho '{target}' não encontrado.", file=sys.stderr)
        sys.exit(2)

    total_links = 0
    syntax_issues: List[Dict[str, Any]] = []
    online_failures: List[Dict[str, Any]] = []

    for fpath in files:
        file_links = extract_links_from_file(fpath)
        total_links += len(file_links)

        for l in file_links:
            # Validação estrutural
            issues = validate_link_syntax(l)
            syntax_issues.extend(issues)

            # Validação online opcional
            if args.online and not issues and l["url"].startswith(("http://", "https://")):
                alive, status, msg = check_url_online(l["url"], timeout=args.timeout)
                if not alive:
                    online_failures.append({
                        "file": l["file"],
                        "line": l["line"],
                        "url": l["url"],
                        "status": status,
                        "error": msg,
                    })

    if args.format == "json":
        out = {
            "target": target,
            "total_files": len(files),
            "total_links": total_links,
            "syntax_issues_count": len(syntax_issues),
            "syntax_issues": syntax_issues,
            "online_failures_count": len(online_failures),
            "online_failures": online_failures,
        }
        print(json.dumps(out, indent=2, ensure_ascii=False))
        sys.exit(1 if syntax_issues or online_failures else 0)

    print("=== Auditor de Links da Base Dinâmica ===")
    print(f"Arquivos inspecionados: {len(files)}")
    print(f"Links encontrados: {total_links}\n")

    if syntax_issues:
        print(f"❌ Problemas de sintaxe encontrados ({len(syntax_issues)}):")
        for iss in syntax_issues:
            print(f"   [{iss['file']}:{iss['line']}] [{iss['type']}] {iss['detail']}")
        print()

    if args.online and online_failures:
        print(f"⚠️ Falhas de conexão HTTP ({len(online_failures)}):")
        for f in online_failures:
            print(f"   [{f['file']}:{f['line']}] {f['url']} (Status: {f['status']}, Erro: {f['error']})")
        print()

    if not syntax_issues and (not args.online or not online_failures):
        print("✅ Todos os links inspecionados são válidos e bem formatados!")
        sys.exit(0)
    else:
        sys.exit(1)


if __name__ == "__main__":
    main()
