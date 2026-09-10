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
  - Parte 1: [Fundamentos e Marco Legal](file:///Users/gabrielramos/Developer/personal/osint_advogados/livro/parte_1_fundamentos_e_marco_legal/) (Caps. 01–04)
  - Parte 2: [Metodologia e Evidências](file:///Users/gabrielramos/Developer/personal/osint_advogados/livro/parte_2_metodologia_investigativa_e_evidencias/) (Caps. 05–08)
  - Parte 3: [Fontes e Técnicas Operacionais](file:///Users/gabrielramos/Developer/personal/osint_advogados/livro/parte_3_fontes_de_informacao_e_tecnicas_operacionais/) (Caps. 09–15)
  - Parte 4: [Análise, Grafos e Investigação Defensiva](file:///Users/gabrielramos/Developer/personal/osint_advogados/livro/parte_4_analise_grafos_e_investigacao_defensiva/) (Caps. 16–20)
  - Parte 5: [Casos Práticos e Exercícios](file:///Users/gabrielramos/Developer/personal/osint_advogados/livro/parte_5_casos_praticos_e_caderno_exercicios/) (Caps. 21–24)
- **Casos Práticos Operacionais (7 Casos Reais Guiados)**: [casos_praticos/](file:///Users/gabrielramos/Developer/personal/osint_advogados/casos_praticos/)
- **Base Dinâmica de Ferramentas e Fontes (Sujeita a Volatilidade)**: [base_dinamica/](file:///Users/gabrielramos/Developer/personal/osint_advogados/base_dinamica/)
- **Metodologia dos 8 Boxes Didáticos**: [metodologia/](file:///Users/gabrielramos/Developer/personal/osint_advogados/metodologia/)
- **Plano de Execução e Auditoria**: [plano_execucao_detalhado.md](file:///Users/gabrielramos/Developer/personal/osint_advogados/plano_execucao_detalhado.md)
- **Matriz de Conversão da Disciplina de Pós (72h)**: [matriz_conversao_curso.md](file:///Users/gabrielramos/Developer/personal/osint_advogados/matriz_conversao_curso.md)
- **Dataset OSINT Brazuca**: [osint_brazuca_dataset/](file:///Users/gabrielramos/Developer/personal/osint_advogados/osint_brazuca_dataset/)

## ⚡ Comandos Rápidos e Linters

- **Validar integridade de evidências digitais**:
  ```bash
  python3 scripts/lint_evidencias.py --path casos_praticos
  python3 scripts/lint_evidencias.py --path livro
  ```
