# Estudo de Caso Prático 02: Devedor Aparentemente Insolvente e Ocultação Patrimonial

## 1. Cenário Fático e Mandato Investigativo

- **Cliente**: Banco Fomento Comercial S/A.
- **Caso**: Cumprimento de Sentença (Proc. nº 0045123-11.2024.8.19.0001 - 22ª Vara Cível do Rio de Janeiro).
- **Alvo**: Marcos Aurélio Silveira, avalista de cédula de crédito bancário inadimplida no montante de R$ 1.850.000,00.
- **Problema Jurídico**: Todas as tentativas de constrição judicial direta restaram infrutíferas: SISBAJUD retornou saldo de R$ 142,30; RENAJUD não localizou veículos registrados no CPF; certidão negativa de bens imóveis no município do Rio de Janeiro. O executado alega insolvência absoluta em impugnação.
- **Pergunta Investigativa**: *O devedor Marcos Aurélio Silveira possui patrimônio imobiliário, societário ou móvel registrado em nome de interpostas pessoas (físicas ou jurídicas), mantendo o domínio e o proveito econômico de fato?*
- **Base Legal (LGPD)**: Art. 7º, VI, da Lei 13.709/2018 (exercício regular de direitos em processo judicial).

---

## 2. Ponto de Partida e Identificadores Iniciais (*Seeds*)

- **Nome Completo**: Marcos Aurélio Silveira.
- **CPF**: `***.789.207-**`.
- **Cônjuge**: Beatriz Vasconcelos Silveira (casamento sob regime de comunhão parcial de bens em 2012).
- **Filha**: Larissa Vasconcelos Silveira (nascida em 2005, estudante).

---

## 3. Cadeia Lógica de Pivoteamento

```
[CPF do Devedor]
       │
       ▼ (Receita Federal / QSA - Histórico)
[Sócio retirante da empresa MAS Engenharia Ltda. há 18 meses]
       │
       ▼ (JUCERJA - Alteração Contratual nº 12)
[Cessão de quotas para a filha Larissa (à época com 18 anos recém-completados)]
       │
       ▼ (JUCERJA - Busca de Empresas por Larissa Vasconcelos Silveira)
[Constituição da empresa "LVS Participações e Administração de Bens Ltda."]
       │
       ▼ (Receita Federal - Cartão CNPJ LVS Participações)
[Capital Social: R$ 4.200.000,00 integralizado com imóveis residenciais]
       │
       ▼ (SAEC / ONR - Pesquisa de Imóveis no CNPJ da LVS Participações)
[Matrícula 45.890 - 5º RGI do Rio de Janeiro: Cobertura Duplex na Barra da Tijuca]
       │
       ▼ (Certidão de Matrícula Inteiro Teor)
[Imóvel transferido por Marcos Aurélio para a holding 2 meses após a citação na execução original]
       │
       ▼ (Redes Sociais Públicas / LinkedIn / Instagram)
[Devedor posta do interior da cobertura; figurando como gestor de projetos da empresa da filha]
```

---

## 4. Diário de Buscas e Execução Operacional

| Data/Hora | Fonte Consultada | Termo de Busca | Resultado Bruto | Análise / Decisão |
| :--- | :--- | :--- | :--- | :--- |
| 2026-09-08 14:00 | JUCERJA | `Marcos Aurélio Silveira` | Localizada saída da MAS Engenharia e constituição de holding familiar pela filha Larissa. | Requerer certidão de inteiro teor da holding. |
| 2026-09-08 15:10 | JUCERJA | `LVS Participações Ltda.` | Contrato social registra integralização de capital mediante conferência de bens imóveis de Marcos Aurélio. | Imóveis saíram do CPF do devedor e foram para a PJ da filha. |
| 2026-09-08 16:30 | SAEC / ONR | `CNPJ 55.432.109/0001-02` | Apontamento de 2 imóveis no 5º RGI e 9º RGI do Rio de Janeiro. | Solicitar certidão de inteiro teor das matrículas. |
| 2026-09-09 10:00 | 5º RGI do Rio de Janeiro | Matrícula 45.890 | R-07/45.890: Alienação do imóvel por Marcos Aurélio e esposa em favor da LVS Participações em 14/11/2024. A citação na execução ocorreu em 15/09/2024. | **Fraude à execução caracterizada** (alienação posterior à citação válida). |

---

## 5. Matriz de Evidências

| ID | Fato Investigado | Informação Encontrada | Fonte | Data | Tipo | Confiabilidade | Corroboração | Limitação | Classificação | Preservação | Utilidade Jurídica |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **EVD-03** | Esvaziamento patrimonial fraudulento. | Transferência de imóvel duplex de R$ 3,5 mi para holding da filha 60 dias após citação válida. | 5º RGI do Rio de Janeiro (Matrícula 45.890, R-07). | 2026-09-09 | Primária | Alta (Fé Pública Registral) | Corroborado pelo contrato social na JUCERJA e data de citação nos autos. | A certidão comprova a transmissão, mas não atesta por si só o consilium fraudis subjetivo. | Fato Verificado (Alienação formal após citação). | Certidão em PDF com assinatura digital PAdES ICP-Brasil do registrador. | Pedido de declaração de ineficácia do negócio jurídico por fraude à execução (art. 792, IV, do CPC). |
| **EVD-04** | Confusão patrimonial e grupo familiar de fachada. | A sócia da holding é estudante sem renda declarada, enquanto o devedor mantém a posse e administração real dos bens. | Junta Comercial (JUCERJA) e declarações públicas em redes profissionais. | 2026-09-09 | Primária e Secundária | Alta | Corroborado pelo comprovante de residência do próprio devedor nos autos. | Capacidade financeira da filha pode ser objeto de contestação. | Indício Forte de interposição fraudulenta de pessoa ("laranja"). | Contrato social integral + prints de perfil público preservados com hash SHA-256. | Pedido de desconsideração inversa da personalidade jurídica (art. 50 do Código Civil). |

---

## 6. Boxes de Aprendizagem Aplicados

> [!IMPORTANT]
> ### 🚩 Sinal de Atenção: Sucessão Patrimonial para Herdeiros Recém-Emancipados
> A transmissão de cotas sociais ou imóveis para filhos de 18 ou 19 anos no exato momento em que avolumam execuções cíveis contra o patriarca é a tipologia clássica de blindagem patrimonial fraudulenta. O juiz cível reconhece a simulação quando confrontada com a evidente falta de capacidade econômico-financeira do donatário.

> [!WARNING]
> ### ⚖️ Limite Jurídico: Sigilo Fiscal e Bancário da Filha
> A existência de indício de interposição não autoriza o credor a requerer, de plano, a quebra de sigilo bancário de terceiros sem a prévia instauração do Incidente de Desconsideração da Personalidade Jurídica (IDPJ) ou demonstração inequívoca de fraude. O pedido deve centrar-se na ineficácia da alienação do imóvel registrado.

---

## 7. Desfecho Jurídico e Aplicação Prática

O credor peticionou nos autos da execução comprovando, mediante o cruzamento da certidão de citação com a certidão de matrícula imobiliária, que a alienação do imóvel ocorreu **após a citação válida em demanda executiva capaz de reduzi-lo à insolvência**. 

O juiz da 22ª Vara Cível acolheu o pedido liminarmente, declarando a **ineficácia da transferência do imóvel perante a execução** (art. 792, § 1º, do CPC) e determinando a averbação da penhora diretamente na matrícula nº 45.890 do 5º RGI, assegurando a garantia integral do crédito de R$ 1.850.000,00.
