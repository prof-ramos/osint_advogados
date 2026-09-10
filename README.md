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
├── plano_execucao_detalhado.md               # Plano de execução mestre consolidado
├── matriz_conversao_curso.md                 # Fase 12: Mapeamento direto Livro -> Curso/Aulas/Workshops
│
├── relatorios_auditoria/                     # Fases 1, 2 e 3 (Ciclos 1 e 2)
│   ├── 01_mapa_reaproveitamento.md           # Desmontagem crítica da ementa acadêmica de 72h
│   ├── 02_auditoria_juridica.md              # Auditoria integral: LGPD, Prova Digital, Prov. 188 e Marco Civil
│   └── 03_auditoria_referencias.md           # Saneamento bibliográfico classificado em 4 níveis (A, B, C, D)
│
├── metodologia/                              # Fases 4, 8 e 11 (Ciclo 3)
│   ├── 01_metodologia_10_etapas.md           # O Ciclo Investigativo em 10 Etapas
│   ├── 02_sistema_evidencias_matriz.md       # Matriz Padronizada de 12 Campos e Escala de Certeza
│   └── 03_guia_boxes_padronizados.md         # Catálogo dos 8 boxes pedagógicos (⚖️, 🔎, 🚩, ⚠️, 🧪, 📦, 🏛️, 🇧🇷)
│
├── osint_brazuca_dataset/                    # Fase 6: Integração Metodológica com o OSINT Brazuca
│   ├── protocolo_validacao_fontes.md         # Protocolo operacional de 11 passos para admissão de fontes
│   └── mapeamento_fontes_brazuca.md          # Dataset estruturado por Entradas (Inputs) e Retornos (Outputs)
│
├── base_dinamica/                            # Fase 10: Isolamento do Conteúdo Volátil
│   ├── catalogo_ferramentas_portais.md       # URLs vivas, ferramentas, APIs, custos e contingências
│   └── checklist_verificacao_links.md        # Protocolo trimestral de manutenção e auditoria de links
│
├── casos_praticos/                           # Fase 9: Sete Estudos de Caso Fictícios Completos
│   ├── caso_01_devedor_nao_localizado.md     # Caso 1: Rastreamento de domicílio contemporâneo
│   ├── caso_02_devedor_aparentemente_insolvente.md # Caso 2: Holding familiar e fraude à execução
│   ├── caso_03_execucao_alimentos.md         # Caso 3: Teoria da Aparência e sinais de riqueza
│   ├── caso_04_perfil_anonimo_redes.md       # Caso 4: Atribuição digital e rito do Marco Civil
│   ├── caso_05_publicacao_apagada_preservacao.md # Caso 5: Preservação descentralizada e prova de confissão
│   ├── caso_06_empresa_suspeita_societario.md# Caso 6: Due diligence societária e empresas noteiras
│   └── caso_07_caso_integrado_completo.md    # Caso 7: Desafio integrado multivetorial (3 seeds)
│
└── livro/                                    # O LIVRO COMPLETO (E-book Perene - 24 Capítulos)
    ├── 00_sumario_e_apresentacao.md          # Sumário geral e manifesto da obra
    ├── parte_1_fundamentos_e_regime_juridico/
    │   ├── cap_01_investigacao_osint_direito_brasileiro.md
    │   ├── cap_02_regime_juridico_lgpd_lai_marco_civil.md
    │   ├── cap_03_investigacao_defensiva_provimento_188.md
    │   └── cap_04_prova_digital_cadeia_custodia_mesmidade.md
    ├── parte_2_metodologia_investigativa_e_evidencias/
    │   ├── cap_05_ciclo_investigativo_10_etapas.md
    │   ├── cap_06_separacao_epistemologica_fato_inferencia_hipotese.md
    │   └── cap_07_sistema_matriz_evidencias_relatorio.md
    ├── parte_3_tecnicas_operacionais_e_pivoteamento/
    │   ├── cap_08_pesquisa_web_avancada_dorking.md
    │   ├── cap_09_investigacao_identidade_pessoas_naturais.md
    │   ├── cap_10_investigacao_societaria_pessoas_juridicas.md
    │   ├── cap_11_analise_documental_metadados_arquivos.md
    │   ├── cap_12_redes_sociais_atribuicao_comportamento.md
    │   ├── cap_13_imagens_videos_geolocalizacao_satelite.md
    │   ├── cap_14_web_historica_infraestrutura_digital.md
    │   └── cap_15_analise_vinculos_grafos_relacoes.md
    ├── parte_4_aplicacoes_juridicas_praticas/
    │   ├── cap_16_localizacao_devedores_execucao.md
    │   ├── cap_17_investigacao_patrimonial_rastreamento_bens.md
    │   ├── cap_18_fraude_contra_credores_ocultacao_patrimonial.md
    │   ├── cap_19_direito_familia_execucao_alimentos.md
    │   ├── cap_20_ilicitos_ciberneticos_atribuicao_redes.md
    │   ├── cap_21_due_diligence_compliance_risco.md
    │   └── cap_22_quando_osint_e_insuficiente_medidas_judiciais.md
    └── parte_5_casos_praticos_e_caderno_exercicios/
        ├── cap_23_estudos_de_caso_guiados.md
        └── cap_24_laboratorio_integrado_simulacao_contraditorio.md
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

1. **Para Estudo e Redação de Peças**: Navegue pelos capítulos perenes em [`livro/`](file:///Users/gabrielramos/Developer/personal/osint_advogados/livro/) para fundamentação dogmática e doutrinária.
2. **Para Consultas e Ferramentas Práticas**: Acesse a [`base_dinamica/`](file:///Users/gabrielramos/Developer/personal/osint_advogados/base_dinamica/) e o [`osint_brazuca_dataset/`](file:///Users/gabrielramos/Developer/personal/osint_advogados/osint_brazuca_dataset/) para identificar portais e parâmetros de busca por tipo de entrada (CPF, CNPJ, Placa, Matrícula, etc.).
3. **Para Capacitação e Treinamento**: Utilize os roteiros de simulação em [`casos_praticos/`](file:///Users/gabrielramos/Developer/personal/osint_advogados/casos_praticos/) e a [`matriz_conversao_curso.md`](file:///Users/gabrielramos/Developer/personal/osint_advogados/matriz_conversao_curso.md).

---

## ⚖️ Licença e Governança

Conteúdo técnico e jurídico licenciado sob termos acadêmicos e profissionais para uso em procedimentos judiciais, advocacia e formação continuada.
