# Capítulo 07: O Sistema de Evidências: Matriz Padronizada de 12 Campos e Redação do Relatório de Inteligência

## 1. O Relatório de Inteligência como Instrumento de Persuasão Racional

No direito processual brasileiro, vigora o princípio da persuasão racional do juiz (art. 371 do CPC e art. 155 do CPP). O magistrado aprecia a prova livremente, mas deve motivar as razões de seu convencimento com base nos elementos concretos constantes dos autos.

Juízes e desembargadores enfrentam acervos com milhares de processos e não possuem tempo hábil para ler petições prolixas, confusas ou ilustradas com dezenas de prints desconexos colados no corpo do texto. 

O **Relatório de Inteligência em Fontes Abertas (RIFA)** é a peça que organiza o caos informacional:
- Apresenta os achados em ordem lógica e cronológica;
- Classifica a força de cada elemento pela Matriz de 12 Campos;
- Traduz dados técnicos de internet em conceitos processualmente inteligíveis;
- Blinda o material contra alegações de quebra de cadeia de custódia mediante hashes verificáveis.

---

## 2. A Estrutura Padrão do Relatório Forense (RIFA)

Um relatório profissional de OSINT jurídico divide-se em 8 seções obrigatórias:

```
┌─────────────────────────────────────────────────────────────┐
│ 1. MANDATO, ESCOPO E IDENTIFICAÇÃO DO CASO                 │
├─────────────────────────────────────────────────────────────┤
│ 2. RESUMO EXECUTIVO DOS FATOS RELEVANTES                    │
├─────────────────────────────────────────────────────────────┤
│ 3. METODOLOGIA APLICADA E BASES CONSULTADAS                 │
├─────────────────────────────────────────────────────────────┤
│ 4. LINHA DO TEMPO FÁTICA E CRONOLOGIA DE EVENTOS            │
├─────────────────────────────────────────────────────────────┤
│ 5. ANÁLISE DE VÍNCULOS E GRAFOS SOCIETÁRIOS/PATRIMONIAIS   │
├─────────────────────────────────────────────────────────────┤
│ 6. A MATRIZ CONSOLIDADA DE EVIDÊNCIAS (12 CAMPOS)           │
├─────────────────────────────────────────────────────────────┤
│ 7. LIMITAÇÕES CONHECIDAS E HIPÓTESES ALTERNATIVAS           │
├─────────────────────────────────────────────────────────────┤
│ 8. CONCLUSÃO, SUGESTÕES PROCESSUAIS E ANEXO DE CUSTÓDIA     │
└─────────────────────────────────────────────────────────────┘
```

---

## 3. Aplicação da Matriz de Evidências de 12 Campos no Corpo do Relatório

Em vez de narrar os fatos de forma romanceada, cada proposição relevante da petição deve fazer referência direta ao ID da Matriz de Evidências. Veja o exemplo de redação forense:

> *"Conforme demonstrado no documento **EVD-003**, o executado alienou o imóvel residencial matrícula nº 45.890 em favor da holding de sua filha apenas 60 dias após sua citação válida nesta execução (fls. 45), caracterizando a hipótese objetiva de fraude à execução prevista no art. 792, IV, do CPC. A higidez da certidão e o código hash correspondente constam da tabela anexa à presente manifestação."*

### A Tabela Resumo para Inserção na Petição:
| ID | Descrição do Fato | Fonte Primária | Data / Hora | Classificação Probatória | Código Hash SHA-256 (64 dígitos) |
| :---: | :--- | :--- | :--- | :--- | :--- |
| **EVD-001** | Saída formal da sociedade | JUCESP (Alt. 05) | 10/08/2025 14:30 BRT | Fato Verificado | `907e86903a2270d7454e891f6c5f54bbb71db25cfa7d45264a2382bff56e7ced` |
| **EVD-002** | Veículo em posse contínua | DETRAN / Infração | 15/01/2026 08:45 BRT | Indício Forte | `1b5243641b69f0af980805be18a1db2e697418f10b34cf08270a798d5c369da7` |
| **EVD-003** | Doação após citação | 5º RGI / Matrícula | 14/11/2024 16:10 BRT | Fato Verificado | `b4ad9cc5e4fa8fa194291f6d439f95ad1f768aa82a661ea93628aa12401ab3cc` |

---

## 4. Visualização de Vínculos e Grafos sem Violação à LGPD

A inclusão de diagramas relacionais (grafos) é uma das técnicas mais eficazes para demonstrar grupos econômicos, confusão patrimonial e interposição de pessoas ("laranjas"). No entanto, o advogado deve respeitar dois limites cruciais:

1. **Minimização de Dados de Terceiros**: Se no contrato social constam sócios minoritários ou testemunhas que não possuem qualquer relação com a fraude apurada, seus nomes completos e CPFs devem ser anonimizados ou suprimidos do grafo.
2. **Vedação ao Doxxing Processual**: Informações estritamente íntimas de familiares (como escolas de filhos menores, placas de veículos de terceiros ou fotos de residências particulares) não devem ser exibidas publicamente na peça principal, devendo ser requerida a juntada sob **segredo de justiça / sigilo documental** (art. 189 do CPC).

---

## 5. Boxes Didáticos do Capítulo

> [!NOTE]
> ### 📦 Preservação: A Certidão de Conformidade dos Hashes
> Ao concluir o relatório, elabore um documento anexo denominado **Certidão de Conformidade e Custódia Digital**, assinado com certificado digital ICP-Brasil pelo advogado ou perito assistente, relacionando:
> - Nome de cada arquivo salvo;
> - Tamanho exato em bytes;
> - Código Hash SHA-256;
> - Data/hora oficial da captura (fuso Brasília).
> Esse anexo confere presunção de autenticidade documental imediata na distribuição da petição inicial.

> [!WARNING]
> ### ⚖️ Limite Jurídico: O Dever de Urbanidade na Redação do Relatório
> O art. 44 do Código de Ética e Disciplina da OAB impõe ao advogado o dever de tratar o público, os colegas e as partes com urbanidade e linguagem técnica desapaixonada. Jamais utilize termos injuriosos no relatório (como "estelionatário", "golpista" ou "ladrão"), a menos que haja sentença penal condenatória transitada em julgado. Utilize termos técnico-jurídicos rigorosos: *"indícios veementes de confusão patrimonial"*, *"tipologia compatível com interposição fraudulenta de pessoa"*, *"negócio jurídico aparente"*.

> [!TIP]
> ### 🔎 Pivô: O Resumo Executivo para Decisão Liminar
> Juízes costumam decidir pedidos de tutela de urgência (arresto, bloqueio de bens) nas primeiras páginas da petição. Coloque logo após a qualificação das partes um **Quadro Sinótico de Evidências** de uma página com os principais pivôs encontrados. Isso eleva substancialmente as chances de deferimento de liminar *inaudita altera parte*.
