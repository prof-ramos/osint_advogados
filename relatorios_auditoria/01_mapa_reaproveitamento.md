# Relatório de Auditoria: Fase 1 — Desmontagem Controlada da Ementa Acadêmica

## 1. Contexto e Diagnóstico do Material Original

O material de partida (`disciplina_original.md`) foi estruturado originalmente no formato de uma disciplina acadêmica de pós-graduação *lato sensu* com carga horária de 72 horas, dividida em 12 módulos. 

Embora o conteúdo programático traga temas de alta relevância jurídica (como cadeia de custódia, Provimento 188/2018 do CFOAB e interface com a LGPD), sua arquitetura pedagógica é inadequada para um livro técnico e manual prático:
1. **Linguagem prescritiva de PPC**: Foco em objetivos de aprendizagem discente e competências institucionais em vez de procedimentos operacionais e análise jurídica substantiva.
2. **Artificialidade modular**: Divisões de 4h/6h/8h criam silos artificiais (ex.: separar ferramentas em um módulo de 4h e preservação em outro de 8h, quando na prática forense a preservação é concomitante à descoberta).
3. **Falta de densidade operacional**: As técnicas de busca, pivoteamento e análise de vínculos aparecem apenas como tópicos genéricos, desprovidos de fluxogramas analíticos e protocolos de verificação.
4. **Resíduos acadêmicos formais**: Carga horária, critérios percentuais de avaliação (10% a 20%), provas integradoras e requisitos de pré-matrícula que poluem o texto.

---

## 2. Mapa de Reaproveitamento e Classificação Editorial

A tabela a seguir decompõe sistematicamente todas as seções e módulos do documento original, definindo a destinação precisa de cada bloco segundo os critérios: **Manter**, **Reescrever**, **Fundir**, **Expandir**, **Remover**, **Transformar em Box**, **Transformar em Caso Prático** ou **Transformar em Material Complementar**.

| Seção / Módulo Original | Conteúdo Original | Classificação | Destinação na Nova Arquitetura do E-book | Racional Técnico-Jurídico |
| :--- | :--- | :--- | :--- | :--- |
| **Título, Natureza e Carga Horária** | Pós-graduação lato sensu, 72 horas, pré-requisitos | **Remover** | Descartado integralmente | Estrutura puramente administrativa/acadêmica incompatível com manual profissional. |
| **Justificativa** | Expansão de fontes abertas, CF/88 art. 5º, LGPD, LAI, CPC, CPP, Provimento 188 | **Reescrever & Expandir** | `Parte 1: Cap. 01 (Investigação OSINT no Direito Brasileiro)` | Converter justificativa acadêmica em manifesto profissional sobre a necessidade da investigação defensiva e contenciosa orientada a dados. |
| **Objetivo Geral e Específicos** | Capacitar profissionais, formular perguntas, mapear fontes | **Fundir & Reescrever** | `Parte 2: Cap. 05 (Ciclo Investigativo em 10 Etapas)` | Transformar objetivos didáticos em diretrizes metodológicas para a formulação do mandato investigativo. |
| **Competências Técnicas, Éticas e de Comunicação** | Taxonomia de competências (conhecimento, habilidade, atitude) | **Fundir & Transformar em Box** | Distribuído em boxes `⚖️ Limite Jurídico` e `⚠️ Não Conclua Ainda` | Eliminar jargão de PPC (ex.: "desenvolver a capacidade de...") e converter em balizas práticas de atuação. |
| **Módulo 1: Fundamentos de OSINT Jurídico (4h)** | Conceitos, diferença de espionagem, jornalismo, e-discovery | **Reescrever & Fundir** | `Parte 1: Cap. 01` | Estabelecer a demarcação conceitual entre OSINT lícito, perícia técnica judicial e quebra ilegal de sigilo. |
| **Módulo 2: Constituição, LGPD e Ética (8h)** | CF art. 5º, LGPD arts. 7º e 9º, LAI, sigilo | **Reescrever & Expandir** | `Parte 1: Cap. 02 (Regime Jurídico da Investigação em Fontes Abertas)` | Superar a visão rasa restrita aos arts. 7º e 9º da LGPD; incorporar arts. 4º, 6º, 10, 11 e aprofundar bases de exercício regular de direitos e legítimo interesse. |
| **Módulo 3: Fontes Abertas Brasileiras (6h)** | Diários oficiais, juntas comerciais, tribunais, registros | **Expandir & Mapear** | `Parte 3: Caps. 08, 09, 10` e dataset estruturado | O módulo original era apenas uma lista genérica; agora é desdobrado por entidades (Pessoas Naturais, PJs, Domínios) articuladas com o OSINT Brazuca. |
| **Módulo 4: Planejamento Investigativo e Diário de Buscas (4h)** | Escopo, pergunta, diário de buscas com data/consulta | **Expandir & Padronizar** | `Parte 2: Cap. 05` e Matriz de Evidências | O diário de buscas passa a ser elemento de auditabilidade e repetibilidade com modelo formal preenchível. |
| **Módulo 5: Verificação, Triangulação e Análise (6h)** | Testes de autenticidade, vieses, separação fato/inferência | **Manter & Expandir** | `Parte 2: Cap. 06 (Separação Epistemológica: Fato, Indício, Inferência e Hipótese)` | É o coração da epistemologia da prova indiciária; será expandido com matrizes de probabilidade e graus de confiança. |
| **Módulo 6: Preservação de Evidência Digital (8h)** | Hash, print, ata notarial (CPC 384), reprodução mecânica (CPC 422) | **Reescrever & Expandir** | `Parte 1: Cap. 04 (Prova Digital, Cadeia de Custódia e Mesmidade)` e `Parte 3: Cap. 11` | Desmistificar o print screen simples, confrontar ata notarial com plataformas técnicas de preservação auditável e hash criptográfico. |
| **Módulo 7: Prova Digital, CPP e Jurisprudência (8h)** | CPP arts. 158-A a 158-F, art. 563, STJ Informativo 878, Portaria CNJ 391/2025 | **Reescrever & Expandir** | `Parte 1: Cap. 04` | Contextualizar jurisprudência recente do STJ sobre nulidade e contaminação probatória; tratar a Portaria CNJ 391/2025 como ato regulatório preparatório, não norma acabada. |
| **Módulo 8: Investigação Defensiva (4h)** | Provimento 188/2018 CFOAB, paridade de armas, limites éticos | **Expandir & Detalhar** | `Parte 1: Cap. 03 (Investigação Defensiva nos Termos do Provimento 188/2018)` | Roteiro prático para instauração do Procedimento Investigatório Defensivo (PID), formalização de achados e limites penais (violação de sigilo / estelionato digital). |
| **Módulo 9: OSINT Corporativo, Due Diligence e Compliance (6h)** | Antecedentes societários, sanções, CVM, CADE, TCU, Bacen | **Reescrever & Expandir** | `Parte 4: Cap. 21 (Due Diligence, Compliance e Avaliação Reputacional)` | Substituir o viés de curso genérico por fluxogramas de triagem societária, identificação de beneficiário final e conflito de interesses. |
| **Módulo 10: Relatórios Jurídicos e Visualização (6h)** | Estrutura de relatório, matriz de evidências, grafos e linhas do tempo | **Expandir & Padronizar** | `Parte 2: Cap. 07 (Sistema de Evidências, Grafos e Redação do Relatório Pericial)` | Fornecer a Matriz Padronizada de 12 campos e modelos de peças para juntada processual. |
| **Módulo 11: Ferramentas Seguras e Gestão de Dados (4h)** | Navegadores seguros, ferramentas locais, SaaS sob LGPD | **Transformar em Material Complementar** | `base_dinamica/catalogo_ferramentas_portais.md` | Evitar obsolescência do livro: ferramentas dinâmicas vão para a base complementar; princípios de segurança permanecem no livro. |
| **Módulo 12: Projeto Final de OSINT Jurídico (8h)** | Caso fictício integrado com apresentação oral | **Transformar em Caso Prático** | `casos_praticos/caso_07_caso_integrado_completo.md` e `Parte 5: Cap. 24` | Convertido em simulado investigativo forense completo com peças e contraditório. |
| **Metodologia de Ensino (Aulas, slides)** | Expositiva dialogada, debate | **Remover** | Revertido em pedagogia textual do livro (texto direto, caixas didáticas) | Elimina a mecânica de sala de aula. |
| **Matriz e Instrumentos de Avaliação** | Critérios percentuais (10% problema, 15% fontes, 20% preservação) | **Reescrever & Transformar em Checklist** | `metodologia/02_sistema_evidencias_matriz.md` | O critério de nota é convertido em checklist de controle de qualidade e validade jurídica da prova antes da juntada. |
| **Bibliografia Básica e Complementar** | Normas, links de blogs, artigos pontuais | **Auditar & Reestruturar** | `relatorios_auditoria/03_auditoria_referencias.md` | Saneamento das fontes, expurgo de URLs quebradas ou links secundários fracos e promoção de fontes oficiais primárias (Nível A). |

---

## 3. Diretrizes de Transição Estrutural

1. **Eliminação dos "Módulos"**: O livro não conterá "módulos de X horas". A divisão agora é em **Partes Temáticas Orgânicas** e **Capítulos Substantivos**.
2. **Inclusão das Lacunas Operacionais**: O material original era forte em enunciados jurídicos, mas carente em procedimentos técnicos detalhados (ex.: dorking, análise de DNS, busca reversa de imagem, histórico de quadros societários, investigação patrimonial em cartórios de notas e imóveis). Estes pontos foram alçados a capítulos inteiros na nova estrutura.
3. **Isolamento de Componentes Voláteis**: Nenhuma ferramenta ou link que possa expirar em 6 meses figurará como núcleo do texto teórico do livro. Todas as ferramentas e portais operacionais são catalogados na base complementar dinâmica, permitindo atualizações contínuas sem exigir nova edição da obra.
