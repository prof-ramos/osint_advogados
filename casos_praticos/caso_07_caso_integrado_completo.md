# Estudo de Caso Prático 07: Caso Integrado Multivetorial (Desafio Completo)

## 1. Cenário Fático e Mandato Investigativo

- **Cliente**: Sindicato dos Trabalhadores em Transportes Rodoviários de Cargas.
- **Caso**: Execução Trabalhista Reunida / Pedido de Extensão de Responsabilidade por Grupo Econômico e Fraude à Execução (Autos nº 0010450-89.2024.5.02.0014 - 14ª Vara do Trabalho de São Paulo).
- **Alvo Principal**: Grupo Econômico oculto controlado por **Valdemar Alcântara Nogueira**.
- **Problema Jurídico**: A empresa devedora originária (`LogSul Transportes Rodoviários Ltda.`) encerrou subitamente suas atividades operacionais, deixando mais de 80 motoristas desamparados e passivo de R$ 3.500.000,00. As buscas no BACENJUD/SISBAJUD e RENAJUD restaram zeradas. O sócio ostensivo nos autos alega falência fática sem patrimônio remanescente.
- **Pergunta Investigativa**: *A partir dos únicos três dados iniciais conhecidos, é possível reconstruir a cadeia societária real, localizar o patrimônio operacional desviado (frotas de caminhões e galpões) e demonstrar a existência de grupo econômico fraudulento apto a responder pela execução?*
- **Base Legal**: Art. 2º, § 2º, da CLT (Grupo Econômico por Coordenação); Art. 50 do Código Civil c/c Art. 133 do CPC (Desconsideração da Personalidade Jurídica).

---

## 2. As Únicas Informações Iniciais Disponibilizadas (*Seeds*)

1. **Nome**: Valdemar Alcântara Nogueira.
2. **Telefone Celular**: `(11) 97123-4567`.
3. **Empresa Conhecida**: `LogSul Transportes Rodoviários Ltda.`

---

## 3. Diagrama Completo da Cadeia de Pivoteamento

```
                    [DADOS INICIAIS]
     Nome: Valdemar Nogueira | Tel: (11) 97123-4567 | LogSul Transportes
                               │
            ┌──────────────────┴──────────────────┐
            ▼                                     ▼
   (Consulta CNPJ LogSul)               (Consulta Chave Pix Celular)
   CNPJ 12.345.678/0001-99              Nome: Valdemar A. Nogueira
   Sede: Santos/SP                      Banco: Banco Inter
   Status: Inapta (Omissão de Declarações)
            │                                     │
            ▼ (JUCESP - Histórico)                ▼ (Busca Reversa WhatsMyName/Sync)
   Valdemar retirou-se da sociedade     WhatsApp Business com Logo:
   6 meses antes do fechamento.         "TransNorte Logística Integrada"
   Cessão de cotas para ex-motorista.             │
            │                                     ▼
            └──────────────────────► ┌────────────────────────────────────┐
                                     │ (Consulta REDESIM: TransNorte)     │
                                     │ CNPJ 51.987.123/0001-44            │
                                     │ Abertura: 30 dias após saída       │
                                     │ da LogSul. Sede: Campinas/SP       │
                                     │ Sócios: Esposa e Filho (20 anos)   │
                                     └────────────────────────────────────┘
                                                      │
                                                      ▼
                                     ┌────────────────────────────────────┐
                                     │ (Registro.br / DNS TransNorte)     │
                                     │ Domínio: transnortelog.com.br      │
                                     │ E-mail do Titular:                 │
                                     │ valdemar@transnortelog.com.br      │
                                     └────────────────────────────────────┘
                                                      │
                                                      ▼
                                     ┌────────────────────────────────────┐
                                     │ (ANTT - Registro Nacional de       │
                                     │ Transportadores Rodoviários - RNTRC)│
                                     │ Frota: 42 cavalos mecânicos        │
                                     │ Caminhões que pertenciam à LogSul  │
                                     │ transferidos em bloco sem ônus!    │
                                     └────────────────────────────────────┘
                                                      │
                                                      ▼
                                     ┌────────────────────────────────────┐
                                     │ (SAEC / ONR - Pesquisa Imobiliária)│
                                     │ Galpão Logístico em Paulínia/SP    │
                                     │ Registrado em nome de Holding      │
                                     │ Patrimonial da Família Nogueira    │
                                     └────────────────────────────────────┘
```

---

## 4. Diário de Buscas Forense Passo a Passo

### Rodada 1: Esgotamento das Seeds
- **Passo 1.1 (Telefone via Pix)**: Simulação de transferência Pix no internet banking informando a chave telefone `(11) 97123-4567`.
  - *Retorno*: Titular: **Valdemar Alcântara Nogueira**; CPF Parcial: `***.554.898-**`; Instituição: Banco Inter.
  - *Resultado*: Confirmação inequívoca de que o número de telefone está ativo e vinculado diretamente ao CPF do alvo.
- **Passo 1.2 (JUCESP - LogSul Transportes)**: Emissão de Ficha Cadastral Simplificada da empresa originária.
  - *Retorno*: A empresa teve seu capital transferido integralmente para João dos Santos (ex-motorista da própria empresa) em janeiro de 2024, sem qualquer contraprestação financeira comprovada.

### Rodada 2: Descoberta da Nova Empresa Operacional
- **Passo 2.1 (WhatsApp Business / Redes)**: Verificação do perfil do WhatsApp associado ao telefone `(11) 97123-4567`.
  - *Retorno*: Imagem corporativa e catálogo de serviços da **TransNorte Logística Integrada**. O e-mail de contato indicado é `diretoria@transnortelog.com.br`.
- **Passo 2.2 (Registro.br / WHOIS)**: Consulta ao domínio `transnortelog.com.br`.
  - *Retorno*: CNPJ titular: `51.987.123/0001-44` (TransNorte Logística e Transportes Ltda.). Responsável pelo contato técnico: `Valdemar A. Nogueira`.

### Rodada 3: Mapeamento da Fraude e Rastreamento da Frota
- **Passo 3.1 (Receita Federal / QSA da TransNorte)**:
  - *Retorno*: Sede em Campinas/SP; Sócios no QSA: Silvana Meireles Nogueira (esposa) e Felipe Meireles Nogueira (filho de 20 anos). Valdemar figura formalmente apenas como "Diretor Técnico / Procurador".
- **Passo 3.2 (ANTT - Consulta Pública de Transportadores de Carga)**:
  - *Retorno*: A TransNorte possui RNTRC ativo com 42 veículos pesados cadastrados.
  - *Cruzamento Crítico*: Consultando placas de 5 veículos da frota antiga da LogSul localizados em fotos de diários de bordo antigos, constatou-se que **todos os 5 caminhões foram transferidos diretamente da LogSul para a TransNorte** nas semanas que antecederam o fechamento fraudulento da primeira.

### Rodada 4: Rastreamento do Imóvel Sede
- **Passo 4.1 (Cartório de Registro de Imóveis de Paulínia/SP via SAEC)**:
  - *Retorno*: Matrícula nº 18.230: Galpão de 10.000 m² utilizado como pátio de triagem da TransNorte.
  - *Proprietário Registrado*: `VAN Participações e Empreendimentos Imobiliários Ltda.` (Holding patrimonial onde Valdemar é titular de 99% das cotas sociais).

---

## 5. Matriz de Evidências

| ID | Fato Investigado | Informação Encontrada | Fonte | Data | Tipo | Confiabilidade | Corroboração | Limitação | Classificação | Preservação | Utilidade Jurídica |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **EVD-013** | Sucessão empresarial fraudulenta de fato. | Transferência de frota de 42 caminhões da LogSul para a recém-criada TransNorte, mantendo o mesmo corpo gerencial e clientes. | ANTT (RNTRC) e JUCESP. | 2026-09-04 14:00 BRT | Primária Oficial | Alta (Registro de Trânsito) | Corroborado pelo domínio na internet em nome do devedor e pelo WhatsApp pessoal. | A certidão da ANTT comprova o cadastro, mas não audita eventuais contratos de gaveta. | Fato Verificado (Migração física e documental dos ativos). | Arquivo `ANTT_Certidao_Frota_TransNorte.pdf` (Hash SHA-256: `de926c0565800fda809105ec780b8aedc81ce25f63c22e3cd89e1e30a9e2049c`). | Reconhecimento de sucessão fraudulenta e responsabilidade solidária (art. 448 da CLT). |
| **EVD-014** | Confusão patrimonial e uso de interposta pessoa. | O devedor administra de fato a empresa da esposa e filho, utilizando o galpão de sua holding para as operações do grupo. | Registro.br, Receita Federal e Registro de Imóveis. | 2026-09-04 16:30 BRT | Primária e Técnica | Alta | Corroborado pelas declarações em redes profissionais e procuração bancária outorgada ao alvo. | Não houve acesso às contas bancárias (depende de SISBAJUD). | Indício Forte / Fato Indiciário Conclusivo. | Arquivo `CRI_Paulinia_Matricula_18230_certidao.pdf` (Hash SHA-256: `550001278783039e7b6b52b52236b2f070567fadec89662024cb099e1432289c`). | Desconsideração inversa da personalidade jurídica e inclusão da holding e da nova empresa no polo passivo. |

---

## 6. Boxes de Aprendizagem Aplicados

> [!TIP]
> ### 🔎 Pivô: O Registro de Domínio (.br) como Prova de Gestão Oculta
> Muitos devedores têm o cuidado de colocar a nova empresa no nome da esposa ou dos filhos, mas cometem o erro elementar de **cadastrar o próprio nome, CPF ou e-mail pessoal como responsável técnico ou administrativo pelo domínio do site corporativo no Registro.br**. A consulta pública WHOIS revela essa titularidade, desmascarando a alegação de que o devedor "não possui qualquer vínculo com o novo negócio".

> [!IMPORTANT]
> ### 🏛️ Medida Judicial: Bloqueio Imediato via RENAJUD e Averbação Premonitória
> Diante do risco iminente de alienação da frota transferida, a petição deve cumular o pedido de reconhecimento de grupo econômico com **tutela cautelar de arresto e bloqueio de circulação e transferência via RENAJUD** de todos os 42 caminhões registrados no CNPJ da sucessora (CPC, art. 301), além da averbação da execução na matrícula do galpão logístico (art. 828 do CPC).

---

## 7. Desfecho Jurídico e Execução Efetiva

Instruída com o relatório completo de inteligência OSINT e com a Matriz de Evidências, a entidade sindical protocolizou Incidente de Desconsideração da Personalidade Jurídica e Reconhecimento de Grupo Econômico Fraudulento perante a 14ª Vara do Trabalho de São Paulo.

O magistrado do Trabalho:
1. Deferiu medida liminar inaudita altera parte determinando a inserção imediata de restrição de transferência via RENAJUD sobre todos os 42 caminhões da TransNorte;
2. Determinou a indisponibilidade do galpão industrial da VAN Participações via Central Nacional de Indisponibilidade de Bens (CNIB);
3. Incluiu a TransNorte, a VAN Participações e o sócio de fato Valdemar Alcântara Nogueira no polo passivo da execução.

Diante do bloqueio integral de sua infraestrutura operacional, o grupo econômico procurou o sindicato em 48 horas e celebrou **Acordo Judicial Homologado** prevendo o pagamento integral dos R$ 3.500.000,00 devidos aos trabalhadores em 12 parcelas mensais garantidas por hipoteca judiciária sobre o galpão.
