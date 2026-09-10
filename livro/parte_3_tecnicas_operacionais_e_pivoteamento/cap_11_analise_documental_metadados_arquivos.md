# Capítulo 11: Análise Forense de Documentos e Metadados: PDFs, Planilhas e Provas Pré-constituídas

## 1. A Anatomia Invisível dos Documentos Digitais

Na instrução de litígios judiciais, a maior parte das provas pré-constituídas circula sob a forma de documentos digitalizados e arquivos eletrônicos (PDFs, planilhas Excel, apresentações e contratos escaneados).

O operador do Direito comumente atenta apenas para o texto visível impresso nas páginas do documento. Contudo, arquivos digitais contêm uma camada invisível de informações conhecida como **metadados** (*dados sobre os dados*), que registra a história técnica, a cronologia exata de criação, o autor do computador de origem, o software utilizado e eventuais adulterações posteriores.

Na investigação forense documental, a extração e o confronto dos metadados frequentemente revelam fraudes capitais, tais como **documentos antedatados**, laudos periciais encomendados e contratos simulados de cessão de direitos.

---

## 2. Metadados Críticos em Arquivos PDF e Office

| Metadado Técnico | O Que Revela | Aplicação Forense / Hipótese de Fraude |
| :--- | :--- | :--- |
| **`Author` / `Creator`** | Nome do usuário cadastrado na licença do sistema operacional ou software emissor. | Revela que o suposto "laudo independente" foi, na realidade, redigido no computador do advogado da própria parte contrária. |
| **`CreateDate` (Data de Criação)** | Momento exato em que o arquivo digital foi gerado e salvo pela primeira vez (com fuso horário UTC). | Desmascara o **contrato antedatado**: o texto declara ter sido assinado em 10/02/2021, mas o arquivo foi criado em 15/08/2026. |
| **`ModifyDate` (Data de Modificação)** | Última alteração salva no documento. | Demonstra que o documento foi adulterado após a data da notificação extrajudicial. |
| **`Producer` / `Software Application`** | Versão exata do programa gerador (ex.: *Microsoft Word 2024, Adobe Acrobat Pro DC 23.01*). | Anacronismo técnico: um contrato pretensamente assinado em 2018 gerado por versão de software que só foi lançada pela Microsoft em 2024. |
| **Histórico de Revisões e Comentários** | Versões anteriores preservadas na memória XML de arquivos `.docx` e `.xlsx`. | Recupera textos suprimidos, cláusulas excluídas e anotações internas das partes durante a negociação preliminar. |

---

## 3. Ferramental para Extração Forense de Metadados

Para realizar a extração sem alterar a integridade do vestígio e sem enviar arquivos confidenciais a sites de terceiros, o analista deve utilizar ferramentas locais de execução em linha de comando:

### 3.1. ExifTool (Referência Global em Perícia de Metadados)
O *ExifTool* (desenvolvido por Phil Harvey) é a ferramenta de padrão pericial aceita internacionalmente por peritos criminais federais e tribunais:
- **Comando de Extração Básica**:
  ```bash
  exiftool -a -u -g1 contrato_questionado.pdf
  ```
- **Comando para Extração de Metadados Específicos de Tempo**:
  ```bash
  exiftool -time:all -s contrato_questionado.pdf
  ```
- **Exportação de Relatório Pericial em Texto**:
  ```bash
  exiftool -json documento_suspeito.pdf > laudo_metadados.json
  ```

---

## 4. Assinaturas Eletrônicas sob a Lei 14.063/2020 e o Verificador do ITI

A promulgação da **Lei nº 14.063/2020** disciplinou as assinaturas eletrônicas no Brasil, classificando-as em três categorias jurídicas com forças probatórias distintas:

1. **Assinatura Eletrônica Simples**: Permite identificar o signatário mediante dados associados em formato eletrônico (ex.: assinatura em tablet com caneta touch, confirmação de código SMS ou login com senha). Possui presunção relativa de autenticidade frágil, admitindo ampla impugnação pericial.
2. **Assinatura Eletrônica Avançada**: Utiliza dados para a criação da assinatura sob o controle exclusivo do titular e opera com garantia de integridade (detecta qualquer alteração posterior no documento). É o padrão utilizado em plataformas de assinatura digital em massa (DocuSign, ClickSign, ZapSign) e no portal Gov.br (níveis Prata e Ouro).
3. **Assinatura Eletrônica Qualificada**: Realizada com utilização de **certificado digital padrão ICP-Brasil** (e-CPF / e-CNPJ). Possui **presunção legal de veracidade absoluta e integridade perante terceiros** (art. 10, § 1º, da Medida Provisória nº 2.200-2/2001).

### O Teste de Validade no Verificador do ITI:
Para checar a integridade de qualquer documento assinado com certificado digital no Brasil, acesse o **Verificador de Conformidade do Instituto Nacional de Tecnologia da Informação (ITI)** no endereço oficial `verificador.iti.gov.br`. A plataforma emite um relatório oficial em PDF atestando:
- Se a assinatura digital é válida;
- Se o certificado estava revogado ou expirado na data da assinatura;
- Se o carimbo de tempo (*timestamp*) atesta a integridade do arquivo.

---

## 5. Boxes Didáticos do Capítulo

> [!NOTE]
> ### 🧪 Verificação: A Armadilha do PDF Otimizado por Scanner
> Cuidado: Quando um documento impresso antigo é digitalizado em um scanner de mesa moderno, os metadados do PDF refletirão a data e a marca do scanner utilizado para digitalizar o papel, e **não a data em que o documento original foi redigido**. O anacronismo só comprova fraude se o documento for um arquivo originariamente digital (*born digital*), e não cópia escaneada de documento físico.

> [!NOTE]
> ### 📦 Preservação: A Proteção do Arquivo Original em Mídia Somente-Leitura
> Antes de executar qualquer comando de análise ou abrir o arquivo em softwares leitores de PDF, crie uma cópia exata do arquivo e converta o original para permissão de somente-leitura (`chmod 444 documento.pdf` no Linux/macOS). Isso impede que a simples abertura do arquivo atualize o metadado de último acesso, preservando a higidez do vestígio para a perícia judicial.

> [!WARNING]
> ### ⚖️ Limite Jurídico: O Crime de Falsidade Ideológica e Perícia Grafotécnica
> A comprovação inequívoca por perícia de metadados de que um documento juntado aos autos foi forjado ou antedatado autoriza a instauração de incidente de arguição de falsidade documental (art. 430 do CPC) e o encaminhamento compulsório de cópias ao Ministério Público para apuração dos crimes de uso de documento falso (art. 304 do CP) e estelionato processual.
