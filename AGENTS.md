# AGENTS.md

Guia de navegação e mapa da arquitetura do repositório **OSINT Jurídico**.

## 🧭 Ponteiros de Navegação

- **Modelo de Domínio e Vocabulário Controlado**: [CONTEXT.md](file:///Users/gabrielramos/Developer/personal/osint_advogados/CONTEXT.md)
  *Consulte antes de introduzir novos termos ou alterar definições conceituais (Dado Bruto vs. Fato Verificado vs. Indício).*
- **Padrões de Código e Evidência Forense**: [CODING_STANDARDS.md](file:///Users/gabrielramos/Developer/personal/osint_advogados/CODING_STANDARDS.md)
  *Regras estritas de cadeia de custódia, hashes SHA-256, IDs EVD-XXX e formato de casos práticos.*
- **Decisões Arquiteturais (ADRs)**: [docs/adr/](file:///Users/gabrielramos/Developer/personal/osint_advogados/docs/adr/)
  *Ver [ADR-0001](file:///Users/gabrielramos/Developer/personal/osint_advogados/docs/adr/0001-separacao-ebook-perene-e-base-dinamica.md) sobre separação entre livro perene e base dinâmica.*
- **Manual Completo de OSINT (24 Capítulos)**: [livro/](file:///Users/gabrielramos/Developer/personal/osint_advogados/livro/)
  - Parte 1: [Fundamentos e Regime Jurídico](file:///Users/gabrielramos/Developer/personal/osint_advogados/livro/parte_1_fundamentos_e_regime_juridico/) (Caps. 01–04)
  - Parte 2: [Metodologia e Evidências](file:///Users/gabrielramos/Developer/personal/osint_advogados/livro/parte_2_metodologia_investigativa_e_evidencias/) (Caps. 05–07)
  - Parte 3: [Técnicas Operacionais e Pivoteamento](file:///Users/gabrielramos/Developer/personal/osint_advogados/livro/parte_3_tecnicas_operacionais_e_pivoteamento/) (Caps. 08–15)
  - Parte 4: [Aplicações Jurídicas Práticas](file:///Users/gabrielramos/Developer/personal/osint_advogados/livro/parte_4_aplicacoes_juridicas_praticas/) (Caps. 16–22)
  - Parte 5: [Casos Práticos e Caderno de Exercícios](file:///Users/gabrielramos/Developer/personal/osint_advogados/livro/parte_5_casos_praticos_e_caderno_exercicios/) (Caps. 23–24)
- **Casos Práticos Operacionais (7 Casos Reais Guiados)**: [casos_praticos/](file:///Users/gabrielramos/Developer/personal/osint_advogados/casos_praticos/)
- **Base Dinâmica de Ferramentas e Fontes (Sujeita a Volatilidade)**: [base_dinamica/](file:///Users/gabrielramos/Developer/personal/osint_advogados/base_dinamica/)
- **Dataset OSINT Brazuca**: [osint_brazuca_dataset/](file:///Users/gabrielramos/Developer/personal/osint_advogados/osint_brazuca_dataset/)
- **Suíte Instrucional e Docência (72h)**: [curso/](file:///Users/gabrielramos/Developer/personal/osint_advogados/curso/)
  - [Planos de Aula (Geral e Módulos 01–05)](file:///Users/gabrielramos/Developer/personal/osint_advogados/curso/planos_de_aula/)
  - [Roteiros de Gravação](file:///Users/gabrielramos/Developer/personal/osint_advogados/curso/roteiros_gravacao/)
  - [Caderno de Exercícios](file:///Users/gabrielramos/Developer/personal/osint_advogados/curso/exercicios/)
  - [Templates de Slides Marp](file:///Users/gabrielramos/Developer/personal/osint_advogados/curso/slides/)
- **Suíte de Testes Automatizados**: [tests/](file:///Users/gabrielramos/Developer/personal/osint_advogados/tests/)
- **Pipeline Editorial e Compilação (Markdown, HTML, EPUB 3)**: [scripts/build_ebook.py](file:///Users/gabrielramos/Developer/personal/osint_advogados/scripts/build_ebook.py) e [dist/](file:///Users/gabrielramos/Developer/personal/osint_advogados/dist/)
- **Portal de Documentação Web**: [mkdocs.yml](file:///Users/gabrielramos/Developer/personal/osint_advogados/mkdocs.yml) e [docs/](file:///Users/gabrielramos/Developer/personal/osint_advogados/docs/)

## ⚡ Comandos Rápidos e Makefile

O repositório conta com um `Makefile` na raiz para unificar o fluxo de trabalho:

```bash
# Executar ciclo completo (lint, testes, links e compilação do e-book)
make all

# Validar integridade forense das evidências (casos práticos e livro)
make lint

# Executar a suíte de testes unitários automatizados (15 testes)
make test

# Validar a sintaxe e higidez de links
make check-links

# Compilar os artefatos de publicação (Markdown, HTML print-ready e EPUB 3)
make build-ebook

# Limpar artefatos de build
make clean
```
