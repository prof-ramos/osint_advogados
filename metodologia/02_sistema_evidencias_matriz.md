# Sistema de Evidências: Matriz Padronizada de 12 Campos e Escala de Certeza Probatória

## 1. O Desafio Probatório na Advocacia Digital

Em juízo, dados brutos não convencem juízes; **evidências estruturadas e auditáveis sim**. Apresentar capturas de tela desorganizadas em uma petição inicial ou contestação transmite amadorismo e facilita a impugnação da parte adversa por quebra de cadeia de custódia, ausência de contexto ou indução a erro.

O **Sistema de Evidências** do OSINT Jurídico fundamenta-se em dois pilares:
1. **A Matriz Padronizada de 12 Campos**: Instrumento que cataloga cada elemento investigativo individualmente antes de sua redação na peça jurídica.
2. **A Escala Epistemológica de Certeza**: Critério rigoroso para graduar a força do achado probatório, impedindo conclusões precipitadas.

---

## 2. A Matriz de Evidências de 12 Campos

Toda investigação forense conduzida segundo este manual deve consolidar seus resultados na seguinte matriz:

| Campo nº | Nome do Campo | Descrição e Requisito Forense |
| :---: | :--- | :--- |
| **1** | **ID da Evidência** | Identificador sequencial único (ex.: `EVD-001`, `EVD-002`) referenciado no corpo do relatório e nos anexos. |
| **2** | **Fato Investigado** | A alegação fática controvertida vinculada à causa de pedir (ex.: *"Transferência da administração da empresa Beta para interposta pessoa"*). |
| **3** | **Informação Encontrada** | Síntese descritiva e objetiva do dado bruto obtido na fonte, sem juízo de valor ou adjetivações. |
| **4** | **Fonte de Origem** | Denominação exata do órgão emissor, portal oficial, cartório ou sistema (ex.: *Junta Comercial do Estado de São Paulo - JUCESP*). |
| **5** | **Data e Hora da Coleta** | Momento exato em que a consulta foi realizada, com indicação de fuso horário oficial de Brasília (ex.: *2026-09-10 14:32 BRT*). |
| **6** | **Tipo de Fonte** | Classificação: **Primária** (órgão oficial com fé pública/registro) ou **Secundária** (notícia de imprensa, portal comercial agregador). |
| **7** | **Grau de Confiabilidade** | Avaliação técnica da integridade da base: **Alta** (certidão oficial/diário oficial), **Média** (plataforma institucional) ou **Baixa** (post em rede social aberta). |
| **8** | **Corroboração Cruzada** | Indicação de fontes independentes que confirmam o mesmo dado (ex.: *"Confirmado pelo Diário Oficial do Município e pelo QSA da Receita Federal"*). |
| **9** | **Limitações Conhecidas** | Restrições intrínsecas ao dado (ex.: *"Documento não indica filiação; risco residual de homônimo até confirmação de CPF"*). |
| **10** | **Classificação Epistemológica** | Enquadramento formal: **Fato Verificado**, **Indício Convergente** ou **Inferência Analítica**. |
| **11** | **Método de Preservação e Hash** | Nome do arquivo original salvo em repositório seguro e seu correspondente código hash **SHA-256**, carimbo de tempo ou número de ata notarial. |
| **12** | **Utilidade Jurídica Específica** | A finalidade processual imediata da evidência (ex.: *"Subsidiar pedido de arresto cautelar com base no art. 301 do CPC"*). |

---

## 3. Modelo Operacional Preenchido

A título exemplificativo, veja como um achado societário é transposto para a matriz:

```markdown
| Campo | Registro |
| :--- | :--- |
| **ID** | EVD-004 |
| **Fato Investigado** | Blindagem patrimonial e ocultação da condição de sócio de fato do Executado Carlos Eduardo Ramos. |
| **Informação Encontrada** | Alteração contratual nº 08 da empresa Delta Empreendimentos Imobiliários Ltda., onde a filha de 19 anos do executado integraliza R$ 5.000.000,00 em cotas com imóveis residenciais. |
| **Fonte** | Junta Comercial do Estado do Rio de Janeiro (JUCERJA) - Certidão de Inteiro Teor. |
| **Data / Hora** | 2026-09-10T11:20:00-03:00 |
| **Tipo de Fonte** | Primária Oficial. |
| **Confiabilidade** | Alta (Documento público registrado com selo digital de autenticidade). |
| **Corroboração** | Corroborado pela declaração de bens no inventário da família e pelo histórico de matrículas no RGI do Rio de Janeiro. |
| **Limitações** | O documento comprova a transmissão das cotas e imóveis, mas não audita a origem financeira dos recursos da donatária. |
| **Classificação** | Fato verificado (a doação e alteração societária) + Indício forte de ocultação (disparidade patrimonial com a idade da sócia formal). |
| **Preservação** | Arquivo `20260910_JUCERJA_Delta_Alt08.pdf` (Hash SHA-256: `7f83b1657ff1fc53b92dc18148a1d65dfc2d4b1fa3d677284addd200126d9069`). |
| **Utilidade Jurídica** | Instruir pedido de desconsideração da personalidade jurídica (CPC, art. 50 do CC) e decretação de indisponibilidade de bens. |
```

---

## 4. A Escala Epistemológica de Certeza Probatória

Para evitar que o investigador cometa a falácia da generalização apressada ou afirme mais do que os autos sustentam, o manual adota uma escala de 6 níveis de certeza:

```
[NÍVEL 1: FATO DIRETAMENTE PROVADO]
  └── Documento primário com fé pública incontestável ou registro digital imutável.
      Exemplo: Certidão de óbito, ata notarial, certidão de casamento, registro da Junta Comercial.

[NÍVEL 2: INDÍCIO FORTE / CONVERGENTE]
  └── Vários dados independentes apontam para a mesma conclusão inequívoca, sem contradições lógicas.
      Exemplo: Devedor utiliza carro de luxo registrado em nome da empresa do irmão, reside no imóvel da empresa e posta rotineiramente com o veículo há 2 anos.

[NÍVEL 3: INDÍCIO FRACO / CIRCUNSTANCIAL]
  └── Aponta para uma plausibilidade, mas comporta outras explicações perfeitamente razoáveis.
      Exemplo: Devedor compareceu a um evento corporativo promovido pela empresa executada.

[NÍVEL 4: INFERÊNCIA ANALÍTICA]
  └── Dedução lógica obtida a partir do cruzamento de premissas conhecidas.
      Exemplo: Se a empresa A e a empresa B possuem o mesmo procurador bancário e operam no mesmo galpão, infere-se a existência de grupo econômico de fato.

[NÍVEL 5: HIPÓTESE EM ABERTO]
  └── Possibilidade fática plausível que carece de corroboração ou depende de quebra judicial de sigilo.
      Exemplo: Suspeita de que o executado utiliza contas correntes de interposta pessoa para movimentar receitas de consultoria.

[NÍVEL 6: INFORMAÇÃO INCONCLUSIVA / DESCARTADA]
  └── Dado com dúvida insanável de homonímia, fonte de baixa confiabilidade ou contradição fática insuperável.
```
