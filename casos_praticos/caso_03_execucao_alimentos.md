# Estudo de Caso Prático 03: Ação de Alimentos e Sinais Exteriores de Riqueza

## 1. Cenário Fático e Mandato Investigativo

- **Cliente**: Mariana S. Representando o filho menor Gabriel S. B. (7 anos).
- **Caso**: Ação Revisional de Alimentos / Cumprimento de Sentença sob Rito da Prisão (Proc. nº 0019876-55.2025.8.26.0002 - 3ª Vara de Família de Santo Amaro/SP).
- **Alvo**: Bruno Ferreira Brandão, genitor da criança.
- **Problema Jurídico**: O alimentante ofereceu alimentos provisórios de apenas 30% do salário mínimo, alegando desemprego involuntário desde 2024 e dependência financeira da genitora idosa. Junta aos autos carteira de trabalho digital sem anotações ativas.
- **Pergunta Investigativa**: *Qual é a real capacidade econômico-financeira de Bruno Ferreira Brandão e quais fontes de renda, ativos e atividade econômica ele desenvolve na atualidade?*
- **Base Legal (LGPD)**: Art. 7º, VI, c/c Art. 14, § 1º, da Lei 13.709/2018 (exercício regular de direitos no melhor interesse da criança).

---

## 2. Ponto de Partida e Identificadores Iniciais (*Seeds*)

- **Nome Completo**: Bruno Ferreira Brandão.
- **CPF**: `***.821.308-**`.
- **Último Emprego Formal**: Gerente Comercial em concessionária de veículos (desligado em 2024).
- **Redes Sociais Conhecidas**: Instagram fechado / privado.

---

## 3. Cadeia Lógica de Pivoteamento

```
[Nome + CPF Parcial]
       │
       ▼ (Receita Federal / QSA)
[Nenhuma empresa ativa no CPF]
       │
       ▼ (Google Dorking: "Bruno Brandão" + "Motors" OR "Carros" OR "Consultoria")
[Localizada página pública no Facebook: "Brandão Prime Car Selection"]
       │
       ▼ (Análise de Contato da Página: Número de Telefone Celular)
[(11) 98765-4321]
       │
       ▼ (Consulta de Chave Pix em Ambiente de Checkout Bancário - Telefone)
[Chave Pix cadastrada em nome de "BFB Intermediações e Veículos Eireli"]
       │
       ▼ (Receita Federal - Cartão CNPJ por Razão Social "BFB Intermediações")
[CNPJ 48.912.345/0001-90 - Titular: Helena Ferreira Brandão (mãe idosa de 74 anos)]
       │
       ▼ (INPI - Consulta de Marcas)
[Marca mista "Brandão Prime" depositada por Bruno Ferreira Brandão como procurador legal com plenos poderes]
       │
       ▼ (Análise de Stories e Destaques Públicos da Loja de Veículos)
[Vídeos semanais do alimentante conduzindo Porsche Macan e anunciando veículos de luxo como "proprietário e curador"]
       │
       ▼ (Diário Oficial do Município de São Bernardo do Campo)
[Contrato de locação comercial do galpão da concessionária assinado por Bruno como fiador e administrador de fato]
```

---

## 4. Diário de Buscas e Execução Operacional

| Data/Hora | Fonte Consultada | Termo de Busca | Resultado Bruto | Análise / Decisão |
| :--- | :--- | :--- | :--- | :--- |
| 2026-09-07 10:00 | Redes Sociais Abertas | `"Brandão Prime Car Selection"` | Perfil profissional comercial aberto no Instagram com 45 mil seguidores. | Identificar canal de vendas e contatos cadastrados. |
| 2026-09-07 10:45 | WhatsApp Business | `(11) 98765-4321` | Catálogo de veículos à venda (média de R$ 250.000 a R$ 600.000 por unidade). | Preservar catálogo comercial com fotos e preços. |
| 2026-09-07 11:30 | Receita Federal (QSA) | `BFB Intermediações` | Sócia formal: Helena Ferreira Brandão (mãe de 74 anos aposentada pelo INSS com 1 salário mínimo). | **Interposição de incapaz/idosa**: a mãe não tem experiência com veículos de luxo. |
| 2026-09-07 14:00 | INPI | `Brandão Prime` | Processo de registro de marca nº 931234567. Requerente: BFB Intermediações; Procurador com poderes totais: Bruno Ferreira Brandão. | Prova documental inequívoca da gestão e domínio econômico da marca. |
| 2026-09-07 15:30 | YouTube / Podcasts | `"Bruno Brandão" "veículos"` | Entrevista concedida em julho de 2026 a canal de automobilismo: afirma faturar R$ 800 mil mensais em comissões de intermediação. | Gravação e degravação pericial do trecho com hash SHA-256. |

---

## 5. Matriz de Evidências

| ID | Fato Investigado | Informação Encontrada | Fonte | Data | Tipo | Confiabilidade | Corroboração | Limitação | Classificação | Preservação | Utilidade Jurídica |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **EVD-05** | Atividade empresarial ativa e gestão de fato. | O alimentante é o gestor exclusivo e detentor de procuração com plenos poderes da empresa Brandão Prime Car Selection. | INPI e Junta Comercial de SP. | 2026-09-07 | Primária | Alta | Corroborado por vídeos públicos de atendimento ao cliente e catálogo do WhatsApp. | A empresa formal está no CNPJ da genitora. | Fato Verificado (Gestão de fato demonstrada documentalmente). | Certidão oficial do INPI e contrato social da JUCESP com hash SHA-256. | Desconstituir a tese de "desempregado sem renda" perante o juízo de família. |
| **EVD-06** | Capacidade econômica real e sinais exteriores de riqueza. | Declaração voluntária de faturamento e exibição contínua de veículos esportivos e viagens internacionais de luxo em eventos do setor. | Entrevista em vídeo no YouTube e perfil comercial aberto. | 2026-09-07 | Secundária | Alta (Admissão pública contra si) | Corroborado pelo volume de vendas públicas documentado na rede social. | O faturamento da loja não se confunde integralmente com o lucro líquido pessoal. | Indício Forte de rendimentos superiores a R$ 40.000,00 mensais. | Vídeo preservado em MP4, transcrição notarial/pericial e cálculo de hash SHA-256. | Fixação de pensão alimentícia compatível com a Teoria da Aparência. |

---

## 6. Boxes de Aprendizagem Aplicados

> [!NOTE]
> ### 🧪 Verificação: A Teoria da Aparência no Direito de Família
> O Superior Tribunal de Justiça (STJ) firmou jurisprudência uníssona no sentido de que, em matéria de alimentos, aplica-se a **Teoria da Aparência**. Quando o alimentante oculta suas rendas sob a capa de pessoas jurídicas ou alega desemprego formal, o juiz pode fixar os alimentos com base nos sinais exteriores de riqueza, tais como padrão de moradia, viagens de lazer, veículos utilizados e porte da atividade comercial ostentada (STJ, REsp 1.832.222/SP).

> [!CAUTION]
> ### ⚠️ Não Conclua Ainda: Faturamento Bruto ≠ Renda Líquida
> Cuidado para não pedir alimentos com base no faturamento de intermediação de veículos de luxo. A comissão de revenda de automóveis opera com margens de 3% a 8%. Apresente os dados ao juiz como indicativo de alta liquidez e capacidade de custeio, requerendo alternativamente a apuração de lucros mediante quebra judicial do sigilo fiscal da empresa da genitora.

---

## 7. Desfecho Jurídico e Aplicação Prática

A genitora instruiu a petição inicial da Ação de Alimentos com o relatório de inteligência OSINT, demonstrando a fraude da alegação de desemprego e o controle fático da empresa de intermediação de veículos de luxo.

O magistrado da 3ª Vara de Família de Santo Amaro:
1. Rejeitou a proposta de 30% do salário mínimo;
2. Fixou os **alimentos provisórios em 5 salários mínimos mensais** (R$ 7.560,00);
3. Determinou a expedição de ofício ao Banco Central (SISBAJUD) e à Receita Federal para quebra do sigilo fiscal da empresa individual em nome da mãe do alimentante, visando apurar a distribuição de lucros disfarçada.
