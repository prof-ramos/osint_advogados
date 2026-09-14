# OSINT Aplicado ao Direito Brasileiro: Investigação em Fontes Abertas, Prova Digital e Estratégia Processual

[![GitHub license](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Status](https://img.shields.io/badge/Status-Completo%20%26%20Auditado-brightgreen.svg)]()
[![Jurisdição](https://img.shields.io/badge/Jurisdição-Brasil%20🇧🇷-green.svg)]()
[![Padrão](https://img.shields.io/badge/Padrão-Cadeia%20de%20Custódia%20CPP%2FCPC-orange.svg)]()

> **Manual prático, juridicamente rigoroso e tecnicamente operacional de inteligência em fontes abertas aplicada ao Direito brasileiro.**

Este repositório consolida o projeto de revisão e reconstrução integral do material de OSINT Jurídico, superando o antigo formato de ementa de disciplina de pós-graduação e estabelecendo um manual definitivo para a advocacia contenciosa, consultiva e criminal, além de servir como matriz para cursos, workshops e laboratórios práticos.

---

## 🏛️ Princípios Estruturantes da Obra

1. **Separação Epistemológica Rigorosa**:
   `Dado Encontrado` $\neq$ `Fato Verificado` $\neq$ `Indício` $\neq$ `Correlação` $\neq$ `Inferência` $\neq$ `Hipótese` $\neq$ `Conclusão Proporcional`. Nenhuma correlação estatística ou digital é tratada automaticamente como prova conclusiva.
2. **Cadeia Lógica de Pivoteamento**:
   `Dado Inicial` $\to$ `Fonte Primária` $\to$ `Resultado Bruto` $\to$ `Identificador Derivado` $\to$ `Nova Fonte` $\to$ `Triangulação` $\to$ `Validação de Homonímia` $\to$ `Preservação Técnica` $\to$ `Conclusão Proporcional`.
3. **Hierarquia Oficial de Fontes**:
   - **Nível A**: Fontes Primárias Oficiais (Planalto, STF, STJ, CNJ, CFOAB, ANPD, Receita Federal, Tribunais e Juntas Comerciais).
   - **Nível B**: Produção Técnico-Científica e Jurimétrica.
   - **Nível C**: Doutrina Especializada Reconhecida.
   - **Nível D**: Fontes Comunitárias e Operacionais (ex.: OSINT Brazuca, scripts no GitHub) — utilizadas exclusivamente para descoberta de caminhos e ferramentas, **nunca como fundamento de validade jurídica**.
4. **Foco Estrito no Contexto Brasileiro**:
   Operacionalização sob o Código de Processo Civil (CPC), Código de Processo Penal (CPP - Cadeia de Custódia), Lei Geral de Proteção de Dados (LGPD), Marco Civil da Internet (Lei 12.965/14) e Provimento 188/2018 do CFOAB (Investigação Defensiva).

---

## 📂 Arquitetura do Repositório

```
osint_advogados/
├── README.md                                 # Apresentação executiva e índice geral do projeto
├── CONTEXT.md                                # Modelo de domínio e vocabulário controlado estrito
├── AGENTS.md                                 # Mapa de navegação minimalista para agentes de IA
├── CODING_STANDARDS.md                       # Padrões de evidência forense e regras de revisão
├── Makefile                                  # Automação de tarefas (lint, test, build-ebook, clean)
├── mkdocs.yml                                # Configuração do portal web interativo (MkDocs Material)
├── plano_execucao_detalhado.md               # Plano de execução mestre consolidado
├── matriz_conversao_curso.md                 # Mapeamento direto Livro -> Curso/Aulas/Workshops
│
├── .github/workflows/                        # Automação de CI/CD via GitHub Actions
│   ├── lint_evidencias.yml                   # Validação contínua de evidências e testes unitários
│   └── deploy_docs.yml                       # Build e deploy automático no GitHub Pages
│
├── docs/                                     # Portal de documentação e ADRs
│   ├── index.md                              # Página inicial do portal web
│   └── adr/0001-separacao-ebook-perene...    # Decisão de separação: Perene vs. Dinâmico
│
├── scripts/                                  # Ferramental operacional e editorial
│   ├── lint_evidencias.py                    # Linter de evidências com saída texto/JSON
│   ├── check_links.py                        # Validador de higidez de links (offline/online)
│   ├── build_ebook.py                        # Pipeline editorial para Markdown, HTML e EPUB
│   └── extrair_acervo_belisario.py           # Pipeline de extração de questões e jurisprudência
│
├── tests/                                    # Suíte de testes unitários automatizados (unittest)
│   ├── test_linter.py                        # Testes unitários do motor do linter forense
│   ├── test_corpus_evidence.py               # Varredura de integridade em 100% do acervo
│   ├── test_doctrinal_structure.py           # Verificação dos 24 capítulos e precedentes
│   └── test_ci_workflow.py                   # Validação estrutural do GitHub Actions
│
├── curso/                                    # Estrutura Instrucional Completa (72h)
│   ├── planos_de_aula/                       # Planos de ensino geral e detalhados por módulo
│   ├── roteiros_gravacao/                    # Scripts operacionais para gravação em vídeo
│   ├── exercicios/                           # Caderno de exercícios com gabaritos comentados
│   ├── slides/                               # Templates modernos de slides em Marp/Reveal
│   └── banco_questoes_e_jurisprudencia_osint.md # Banco de questões de concurso comentadas
│
├── relatorios_auditoria/                     # Fases 1, 2 e 3 (Ciclos 1 e 2)
│   ├── 01_mapa_reaproveitamento.md           # Desmontagem crítica da ementa acadêmica de 72h
│   ├── 02_auditoria_juridica.md              # Auditoria integral: LGPD, Prova Digital e Prov. 188
│   └── 03_auditoria_referencias.md           # Saneamento bibliográfico em 4 níveis (A, B, C, D)
│
├── metodologia/                              # Fases 4, 8 e 11 (Ciclo 3)
│   ├── 01_metodologia_10_etapas.md           # O Ciclo Investigativo em 10 Etapas
│   ├── 02_sistema_evidencias_matriz.md       # Matriz Padronizada de 12 Campos e Escala de Certeza
│   └── 03_guia_boxes_padronizados.md         # Catálogo dos 8 boxes pedagógicos (⚖️, 🔎, 🚩, etc.)
│
├── osint_brazuca_dataset/                    # Fase 6: Integração com o OSINT Brazuca
│   ├── protocolo_validacao_fontes.md         # Protocolo operacional de 11 passos para admissão
│   └── mapeamento_fontes_brazuca.md          # Dataset estruturado por Inputs e Outputs
│
├── base_dinamica/                            # Fase 10: Isolamento do Conteúdo Volátil
│   ├── catalogo_ferramentas_portais.md       # URLs vivas, ferramentas, APIs e contingências
│   └── checklist_verificacao_links.md        # Protocolo trimestral de manutenção de links
│
├── casos_praticos/                           # Fase 9: Sete Estudos de Caso Fictícios Completos
│   ├── caso_01_devedor_nao_localizado.md     # Caso 1: Rastreamento de domicílio contemporâneo
│   ├── caso_02_devedor_aparentemente_insolvente.md # Caso 2: Holding familiar e fraude à execução
│   ├── caso_03_execucao_alimentos.md         # Caso 3: Teoria da Aparência e sinais de riqueza
│   ├── caso_04_perfil_anonimo_redes.md       # Caso 4: Atribuição digital e rito do Marco Civil
│   ├── caso_05_publicacao_apagada_preservacao.md # Caso 5: Preservação descentralizada
│   ├── caso_06_empresa_suspeita_societario.md# Caso 6: Due diligence societária e empresas noteiras
│   └── caso_07_caso_integrado_completo.md    # Caso 7: Desafio integrado multivetorial
│
└── livro/                                    # O LIVRO COMPLETO (E-book Perene - 24 Capítulos)
    ├── 00_sumario_e_apresentacao.md          # Sumário geral e manifesto da obra
    ├── parte_1_fundamentos_e_regime_juridico/  (Caps. 01 a 04 - com Info 811 STJ)
    ├── parte_2_metodologia_investigativa_e_evidencias/ (Caps. 05 a 07)
    ├── parte_3_tecnicas_operacionais_e_pivoteamento/ (Caps. 08 a 15)
    ├── parte_4_aplicacoes_juridicas_praticas/ (Caps. 16 a 22 - Precedentes STJ/STF/TST)
    └── parte_5_casos_praticos_e_caderno_exercicios/ (Caps. 23 e 24)
```

---

## 📊 A Matriz Padronizada de Evidências (12 Campos)

Todas as investigações documentadas nos capítulos e estudos de caso utilizam a matriz de controle de higidez:

| Campo | Finalidade Forense |
| :--- | :--- |
| **1. ID da Evidência** | Código identificador único sequencial (ex.: `EVD-001`). |
| **2. Fato Investigado** | Alegação fática controvertida vinculada à causa de pedir. |
| **3. Informação Encontrada** | Síntese descritiva do dado bruto obtido na fonte. |
| **4. Fonte de Origem** | Denominação oficial do órgão ou base consultada. |
| **5. Data e Hora da Coleta** | Registro temporal exato com fuso de Brasília (UTC-3). |
| **6. Tipo de Fonte** | Primária Oficial ou Secundária. |
| **7. Grau de Confiabilidade** | Alta, Média ou Baixa. |
| **8. Corroboração Cruzada** | Fontes independentes que sustentam o mesmo fato. |
| **9. Limitações Conhecidas** | Restrições intrínsecas ao dado e riscos de homonímia. |
| **10. Classificação Epistemológica** | Fato Provado, Indício Forte/Fraco ou Inferência. |
| **11. Preservação e Hash** | Nome do arquivo original e hash **SHA-256** de 64 caracteres. |
| **12. Utilidade Jurídica** | Finalidade processual direta (penhora, arresto, citação). |

---

## 📦 Como Usar Este Repositório

1. **Para Estudo e Redação de Peças**: Navegue pelos capítulos em [`livro/`](file:///Users/gabrielramos/Developer/personal/osint_advogados/livro/) para fundamentação dogmática e doutrinária (Capítulos 04, 16, 17, 18, 19, 20, 21 e 22 contêm precedentes vinculantes comentados do STJ/STF/TST e minutas prontas para petição).
2. **Para Consultas e Ferramentas Práticas**: Acesse a [`base_dinamica/`](file:///Users/gabrielramos/Developer/personal/osint_advogados/base_dinamica/) e o [`osint_brazuca_dataset/`](file:///Users/gabrielramos/Developer/personal/osint_advogados/osint_brazuca_dataset/) para identificar portais por tipo de entrada (CPF, CNPJ, Placa, Matrícula, etc.).
3. **Para Capacitação e Docência**: Utilize os planos de aula, roteiros de gravação, caderno de exercícios e slides em [`curso/`](file:///Users/gabrielramos/Developer/personal/osint_advogados/curso/).
4. **Para Compilar o Livro**: Execute `make build-ebook` para gerar os formatos Markdown completo, HTML diagramado e EPUB 3 em `dist/`.

---

## ⚡ Automação, Governança e Makefile

O repositório conta com automação completa via `Makefile`:

```bash
# Executar todos os linters, testes e compilação do e-book
make all

# Validar integridade forense das evidências (casos práticos e livro)
make lint

# Executar a suíte de testes unitários automatizados (15 testes)
make test

# Validar a higidez dos links da base dinâmica
make check-links

# Compilar o e-book (Markdown, HTML print-ready e EPUB 3)
make build-ebook
```

---

## 🗺️ Roadmap de Evolução e Entregas Concluídas

Todas as metas mapeadas no planejamento foram 100% implementadas e auditadas:

- ✅ **[Issue #1](https://github.com/prof-ramos/osint_advogados/issues/1)**: `feat(livro)`: Aprofundamento jurisprudencial no Lote 2 da Parte 4 (Caps. 19, 20 e 21 - Família, Cibernético e Due Diligence).
- ✅ **[Issue #2](https://github.com/prof-ramos/osint_advogados/issues/2)**: `feat(livro)`: Aprofundamento jurisprudencial no Lote 3 da Parte 4 (Cap. 22 - Medidas Judiciais, SNIPER e Provas).
- ✅ **[Issue #3](https://github.com/prof-ramos/osint_advogados/issues/3)**: `ci`: Pipeline de GitHub Actions para validação contínua de evidências e testes (`.github/workflows/lint_evidencias.yml`).
- ✅ **[Issue #4](https://github.com/prof-ramos/osint_advogados/issues/4)**: `build(ebook)`: Pipeline de compilação editorial nos formatos Markdown monólito, HTML diagramado e EPUB 3 (`scripts/build_ebook.py`).
- ✅ **[Issue #5](https://github.com/prof-ramos/osint_advogados/issues/5)**: `docs(web)`: Portal web interativo de documentação com MkDocs Material e deploy contínuo no GitHub Pages (`.github/workflows/deploy_docs.yml`).
- ✅ **[Issue #6](https://github.com/prof-ramos/osint_advogados/issues/6)**: `course`: Planos de ensino de 72h, roteiros de gravação, caderno de exercícios e slides Marp (`curso/`).

---

## ⚖️ Licença e Governança

Conteúdo técnico e jurídico licenciado sob termos acadêmicos e profissionais para uso em procedimentos judiciais, advocacia e formação continuada.
