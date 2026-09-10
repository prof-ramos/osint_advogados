# Estudo de Caso Prático 06: Empresa Suspeita e Due Diligence Societária

## 1. Cenário Fático e Mandato Investigativo

- **Cliente**: Construtora e Incorporadora Metrópole S/A.
- **Caso**: Auditoria Prévia de Integridade e *Due Diligence* para Contratação de Fornecedor Crítico de Concreto e Fundações (Contrato estimado em R$ 22.000.000,00).
- **Alvo**: TerraFirme Fundações e Serviços de Engenharia Ltda.
- **Problema Jurídico**: A empresa apresentou proposta comercial 30% inferior à média de mercado. O setor de *procurement* solicita aprovação do departamento jurídico. Há suspeita de que a empresa seja sociedade "noteira" (emissora de notas fiscais sem capacidade operacional real), utilizada para fraudes tributárias ou lavagem de dinheiro, o que acarretaria responsabilidade solidária trabalhista e tributária para a contratante (Lei Anticorrupção nº 12.846/2013 e art. 135 do CTN).
- **Pergunta Investigativa**: *A empresa TerraFirme Fundações possui capacidade econômico-operacional comprovada, patrimônio próprio e idoneidade societária, ou apresenta tipologias características de empresa de fachada?*
- **Base Legal (LGPD)**: Art. 7º, II (cumprimento de obrigação legal) c/c Art. 7º, IX (legítimo interesse na gestão de risco corporativo).

---

## 2. Ponto de Partida e Identificadores Iniciais (*Seeds*)

- **Razão Social**: TerraFirme Fundações e Serviços de Engenharia Ltda.
- **CNPJ**: `41.987.654/0001-33`.
- **Endereço Informado na Proposta**: Rua das Indústrias, 450 - Galpão 3, Betim/MG.
- **Sócios Indicados no Contrato Social**: Wagner de Oliveira (90%) e Carlos Alberto Pinto (10%).

---

## 3. Cadeia Lógica de Pivoteamento e Investigação Corporativa

```
[CNPJ da TerraFirme Fundações]
       │
       ▼ (Receita Federal - Cartão CNPJ / REDESIM)
[Data de Abertura: há apenas 7 meses | Capital Social: R$ 50.000,00]
       │
       ▼ (Junta Comercial de Minas Gerais - JUCEMG)
[Alteração Contratual nº 01 protocolada há 60 dias: Aumento súbito de capital para R$ 10.000.000,00]
       │
       ▼ (Exame da Integralização na Certidão de Inteiro Teor)
[Capital integralizado mediante "Títulos da Dívida Pública / Apólices de 1902" de idoneidade nula]
       │
       ▼ (Geolocalização / Google Street View / Imagens Aéreas Recentes)
[Endereço do "Galpão 3": Terreno baldio cercado de mato, sem maquinário ou edificação]
       │
       ▼ (Consulta QSA / Pesquisa dos CPFs dos Sócios)
[Sócio Wagner de Oliveira: Beneficiário do Bolsa Família e sem histórico profissional prévio]
       │
       ▼ (Portal da Transparência da CGU - CEIS / CNEP)
[O endereço de e-mail cadastrado na RFB pertence a operador investigado na Operação Desmonte]
       │
       ▼ (Tribunal de Justiça de Minas Gerais - TJMG)
[Mais de 40 execuções fiscais contra empresas anteriores ligadas ao mesmo e-mail contábil]
```

---

## 4. Diário de Buscas e Execução Operacional

| Data/Hora | Fonte Consultada | Parâmetro de Busca | Resultado Bruto | Análise de Risco |
| :--- | :--- | :--- | :--- | :--- |
| 2026-09-05 09:00 | REDESIM / RFB | `41.987.654/0001-33` | CNAE 43.91-6-00 (Obras de fundações). Capital: R$ 10 mi. | Empresa muito nova para o porte do contrato. |
| 2026-09-05 10:15 | Google Street View / Satélite | `Rua das Indústrias, 450, Betim/MG` | O imóvel é um lote desocupado. Não há caminhões, tratores ou betoneiras no local. | **Ausência de capacidade operacional física.** |
| 2026-09-05 11:30 | Portal da Transparência / CADÚNICO | `Wagner de Oliveira` | Inscrição ativa em programas de transferência de renda até 2025. | Típico perfil de sócio ostensivo "laranja". |
| 2026-09-05 14:00 | JUCEMG | `TerraFirme Fundações` | Integralização de capital com papéis podres (apólices da dívida agrária prescritas). | Fraude contábil evidente para simular solidez. |
| 2026-09-05 16:00 | WHOIS / Registro.br | Domínio `terrafirmefundacoes.com.br` | Registrado em nome de escritório contábil envolvido em constituição de empresas de fachada. | Vínculo com organização especializada em blindagem. |

---

## 5. Matriz de Evidências

| ID | Fato Investigado | Informação Encontrada | Fonte | Data | Tipo | Confiabilidade | Corroboração | Limitação | Classificação | Preservação | Utilidade Jurídica |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **EVD-11** | Inexistência de capacidade operacional instalada. | O endereço declarado como sede e parque de máquinas é um terreno baldio sem atividade industrial. | Plataformas de Imagens Georreferenciadas e Diligência Local. | 2026-09-05 | Primária / Técnica | Alta | Corroborado por consulta de IPTU municipal de lote vago. | Imagens de satélite têm defasagem temporal de semanas ou meses. | Fato Verificado (Inexistência física no local indicado). | Fotografias georreferenciadas com dados EXIF preservados e certidão imobiliária municipal. | Subsidiar parecer de veto absoluto à contratação. |
| **EVD-12** | Fraude na composição do capital social e interposição de pessoa. | Sócio majoritário de R$ 9 milhões é beneficiário de programa social e o capital foi inflado com títulos públicos prescritos sem cotação. | JUCEMG e Portal da Transparência. | 2026-09-05 | Primária Oficial | Alta (Documento Registral) | Corroborado pelo histórico cadastral da Receita Federal. | A verificação da prescrição das apólices decorre de jurisprudência pacífica do STJ. | Fato Verificado (Uso de títulos nulos e desproporção do sócio). | Certidão de Inteiro Teor da Junta Comercial com selo digital. | Afastar responsabilidade da diretoria por omissão de compliance (Lei 12.846/13). |

---

## 6. Boxes de Aprendizagem Aplicados

> [!IMPORTANT]
> ### 🚩 Sinal de Atenção: Aumento Súbito de Capital com Títulos da Dívida Antiga
> A integralização de capital social de empresas recém-criadas mediante "Títulos da Dívida Pública do Século XIX ou início do Século XX" (ex.: apólices da Estrada de Ferro Madeira-Mamoré ou bônus da dívida externa do Império) é uma conhecida fraude contábil para forjar robustez financeira fictícia em licitações e cadastros de grandes empresas. O STJ e o STF já pacificaram que esses títulos estão integralmente prescritos e possuem valor econômico nulo.

> [!TIP]
> ### 🔎 Pivô: O E-mail e Telefone do Contador no Cartão CNPJ
> Ao emitir o Comprovante de Situação Cadastral no CNPJ, observe atentamente o campo "Endereço Eletrônico" e "Telefone". Comumente, fraudadores utilizam o mesmo e-mail contábil para registrar dezenas de empresas de fachada. Consultar esse e-mail em motores de busca e bases abertas frequentemente revela uma verdadeira teia de empresas fantasmas irmãs.

---

## 7. Desfecho Jurídico e Parecer de Compliance

Com base no relatório de inteligência OSINT, o departamento jurídico da Construtora Metrópole emitiu **Parecer Conclusivo de Não-Conformidade (Veto de Contratação)**, alertando a diretoria executiva para os seguintes riscos:
1. Risco de responsabilização objetiva administrativa e civil por contratação de empresa inidônea (Lei Anticorrupção);
2. Risco de autuação da Receita Federal por glosa de créditos tributários decorrentes de notas fiscais inidôneas emitidas por empresa sem estrutura operacional (Súmula 509 do STJ);
3. Risco de execução fiscal solidária por fraude societária.

A contratação foi imediatamente cancelada, protegendo a companhia de um passivo potencial estimado em dezenas de milhões de reais.
