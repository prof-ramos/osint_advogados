# Estudo de Caso Prático 01: Devedor Não Localizado e Citação Frustrada

## 1. Cenário Fático e Mandato Investigativo

- **Cliente**: Empresa Alfa Distribuidora de Medicamentos Ltda.
- **Caso**: Ação de Execução de Título Extrajudicial (Proc. nº 1002345-88.2025.8.26.0100 - 15ª Vara Cível de São Paulo).
- **Alvo**: Rodrigo de Castro Mendonça, devedor principal de nota promissória no valor de R$ 380.000,00.
- **Problema Jurídico**: O executado esquiva-se sistematicamente de oficiais de justiça. Diligências por AR retornaram negativas com a mensagem "Mudou-se". As consultas ordinárias no SISBAJUD e INFOJUD restaram infrutíferas quanto a endereços residenciais atualizados.
- **Pergunta Investigativa**: *Qual é o endereço contemporâneo real de residência ou atividade profissional de Rodrigo de Castro Mendonça onde a citação judicial possa ser consumada com eficácia?*
- **Base Legal (LGPD)**: Art. 7º, VI, da Lei 13.709/2018 (exercício regular de direitos em processo judicial).

---

## 2. Ponto de Partida e Identificadores Iniciais (*Seeds*)

- **Nome Completo**: Rodrigo de Castro Mendonça.
- **CPF**: `***.412.898-**` (obtido da nota promissória executada).
- **Último Endereço Conhecido**: Rua Oscar Freire, 1200, Apto 42, Jardins, São Paulo/SP (infrutífero).
- **Profissão Declarada**: Consultor de Negócios.

---

## 3. Cadeia Lógica de Pivoteamento

```
[Nome + CPF Parcial]
       │
       ▼ (JUCESP - Consulta de Sócios)
[Identificação de Empresa Ativa: Mendonça Consultoria Estratégica EIRELI]
       │
       ▼ (Receita Federal / Cartão CNPJ)
[Endereço Cadastral: Edifício Comercial em Barueri/SP - Sala 504]
       │
       ▼ (Diário Oficial do Município de Barueri - Alvarás)
[Alvará cancelado por encerramento de atividades fáticas há 1 ano]
       │
       ▼ (Dorking Web: Nome + "Mendonça" + "Podcast" / "Palestra")
[Entrevista em Podcast do Setor Imobiliário realizada há 3 semanas]
       │
       ▼ (Análise de Metadados / Descrição do Vídeo)
[Menção: "Diretor de Operações da Construtora Horizon Sul em Florianópolis/SC"]
       │
       ▼ (Junta Comercial de Santa Catarina - JUCESC)
[Horizon Empreendimentos Ltda. - Filial Florianópolis - Sócio Administrador]
       │
       ▼ (Consulta Processual Pública - TJSC)
[Ação Cível Recente onde o alvo foi intimado pessoalmente no Condomínio Jurerê Imperial]
```

---

## 4. Diário de Buscas e Execução Operacional

| Data/Hora | Fonte Consultada | Parâmetro / Termo de Busca | Resultado Bruto | Decisão do Analista |
| :--- | :--- | :--- | :--- | :--- |
| 2026-09-08 09:15 | JUCESP Online | `Rodrigo de Castro Mendonça` | CNPJ 34.123.456/0001-88 (Mendonça Consultoria) | Extrair CNPJ e consultar situação na Receita Federal. |
| 2026-09-08 09:40 | Receita Federal (REDESIM) | `34.123.456/0001-88` | Endereço em Barueri/SP. Situação: Ativa. | Diligência local revelou que o escritório foi desocupado. |
| 2026-09-08 10:20 | Google Avançado | `"Rodrigo de Castro Mendonça" OR "Rodrigo Mendonça"` | Localizado link do YouTube: "Podcast ImobTalks #42". | Analisar vídeo e créditos. |
| 2026-09-08 11:00 | YouTube (Canal ImobTalks) | Transcrição do vídeo aos 14min30s | Alvo declara expressamente residir em Florianópolis há 8 meses. | Direcionar buscas para JUCESC e TJSC. |
| 2026-09-08 14:10 | JUCESC | `Horizon Empreendimentos` | Empresa registrada em Florianópolis, sócio: Rodrigo C. Mendonça. | Obter endereço da sede operacional. |
| 2026-09-08 15:30 | TJSC - Consulta Unificada | `Rodrigo de Castro Mendonça` | Processo 5001298-44.2026.8.24.0023: Certidão de citação cumprida com sucesso em 15/07/2026 no endereço residencial: Av. dos Búzios, 850, Bloco B, Jurerê Internacional, Florianópolis/SC. | Validar contemporaneidade e anexar aos autos da execução. |

---

## 5. Matriz de Evidências

| ID | Fato Investigado | Informação Encontrada | Fonte | Data | Tipo | Confiabilidade | Corroboração | Limitação | Classificação | Preservação | Utilidade Jurídica |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **EVD-001** | Mudança de domicílio do devedor. | Declaração pública de que transferiu residência definitiva para Florianópolis/SC. | Podcast ImobTalks no YouTube. | 2026-09-08 11:00 BRT | Secundária | Média | Corroborada por dados da JUCESC e TJSC. | Depoimento verbal autodeclaratório. | Indício Forte de mudança de comarca. | Arquivo `20260908_imobtalks_ep42_cut.mp4` (Hash SHA-256: `7b436edaa4bca2620df83bc13dd46c267daefab2b15ac3046221b43e070f4872`). | Justificar expedição de Carta Precatória para Florianópolis. |
| **EVD-002** | Endereço residencial contemporâneo efetivo. | Certidão de Oficial de Justiça do TJSC atestando citação pessoal de Rodrigo de Castro Mendonça em julho de 2026. | TJSC - Autos 5001298-44.2026.8.24.0023. | 2026-09-08 15:30 BRT | Primária | Alta (Fé Pública) | Corroborado pelo condomínio e pelo contrato social na JUCESC. | Certidão tem 60 dias de antiguidade. | Fato Verificado (Fé pública de Oficial de Justiça). | Arquivo `TJSC_5001298_mandado_cumprido.pdf` (Hash SHA-256: `5d12bcd3499e94e57524b3e05fab6425b9099238e8aa74c208590fd979004a22`). | Indicar endereço exato para cumprimento do mandado de citação e penhora. |

---

## 6. Boxes de Aprendizagem Aplicados

> [!TIP]
> ### 🔎 Pivô: Processos Judiciais de Terceiros como Fonte de Endereço
> Muitas vezes, o devedor que se oculta em uma ação está litigando ativamente como autor em outro tribunal (ex.: ação de cobrança, divórcio, disputa comercial ou dano moral contra companhia aérea). A consulta processual pública nos tribunais onde ele desenvolve atividades econômicas frequentemente revela petições recentes com qualificação completa e certidões de citação válidas.

> [!CAUTION]
> ### ⚠️ Não Conclua Ainda: A Confirmação do Oficial de Justiça é Necessária
> Embora o podcast indique que o alvo reside em Florianópolis, o endereço fornecido em vídeo pode ser informal ou transitório. A única evidência que confere segurança processual plena para o juiz expedir carta precatória é a certidão de outro oficial de justiça ou o documento arquivado na Junta Comercial.

---

## 7. Desfecho Jurídico e Aplicação Prática

Com base no relatório de inteligência instruído com as certidões da JUCESC e a cópia da certidão do oficial de justiça do TJSC, a parte credora protocolizou petição informando o novo domicílio do devedor e requerendo a expedição urgente de **Carta Precatória Citatória** com ordem expressa de arresto executivo de bens (art. 830 do CPC) caso o devedor não seja encontrado no local para pagamento em 3 dias. A citação foi consumada no endereço apontado em menos de 15 dias.
