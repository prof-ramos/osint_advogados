# Capítulo 08: Pesquisa Web Avançada e Dorking Aplicado a Registros e Repositórios

## 1. O Motor de Busca como Instrumento Pericial

A grande maioria dos usuários da internet utiliza os motores de busca (Google, Bing, DuckDuckGo) de forma ingênua, inserindo palavras isoladas e contentando-se com os primeiros três resultados retornados pelo algoritmo comercial. Para a advocacia investigativa, o buscador não é um catálogo de compras, mas um **indexador global de documentos e bancos de dados públicos**.

A técnica conhecida como **Google Dorking** (ou *Advanced Search Operators*) consiste no emprego de comandos avançados de filtragem sintática para forçar o motor de busca a retornar arquivos específicos, diretórios abertos e páginas governamentais que não aparecem nas buscas ordinárias.

---

## 2. Operadores Fundamentais para a Advocacia Brasileira

A tabela a seguir consolida os principais operadores booleanos e estruturais aplicados ao contexto jurídico e aos registros públicos brasileiros:

| Operador Sintático | Função e Efeito no Motor de Busca | Exemplo Forense Aplicado | Utilidade Processual Imediata |
| :--- | :--- | :--- | :--- |
| `""` (Aspas duplas) | **Busca Literal Exata**: Restringe os resultados à correspondência exata da expressão, na mesma ordem e grafia. | `"Carlos Eduardo Silveira Ramos"` | Elimina homônimos com grafias parciais e nomes intercalados. |
| `site:` | **Restrição de Domínio**: Limita a busca a um domínio ou extensão governamental específica. | `site:jus.br "12.345.678/0001-90"` | Localiza todos os processos judiciais do país onde a empresa é citada. |
| `filetype:` / `ext:` | **Formato de Arquivo**: Retorna exclusivamente arquivos digitais no formato indicado (PDF, XLS, DOC, CSV). | `site:gov.br filetype:pdf "contrato de prestação"` | Localiza contratos administrativos e aditivos na íntegra. |
| `intext:` / `allintext:` | **Texto no Corpo da Página**: Exige que as palavras apareçam obrigatoriamente no corpo do texto da página. | `intext:"sócio retirante" intext:"São Paulo"` | Identifica publicações societárias em jornais e atas comerciais. |
| `intitle:` / `allintitle:` | **Texto no Título da Página**: Busca termos presentes na tag `<title>` do HTML. | `intitle:"diário oficial" "exoneração"` | Localiza portarias e atos de pessoal publicados em imprensa oficial. |
| `inurl:` / `allinurl:` | **Termo na Estrutura da URL**: Identifica caminhos de diretórios e parâmetros de navegação. | `inurl:transparencia filetype:xls` | Encontra planilhas de pagamentos de fornecedores municipais. |
| `-` (Hífen / Operador NOT) | **Exclusão de Termos**: Remove dos resultados as páginas que contenham a palavra especificada. | `"João da Silva" -futebol -musica` | Desambigua alvos públicos de homônimos famosos (jogadores, artistas). |
| `OR` / `\|` (Booleano OU) | **Alternância**: Busca páginas que contenham pelo menos um dos termos informados. | `"Mendonça Engenharia" OR "Mendonça Fundações"` | Mapeia variações de nomes corporativos de um mesmo grupo econômico. |
| `..` (Intervalo Numérico) | **Faixa de Valores ou Anos**: Pesquisa números contidos no intervalo indicado. | `"pregão eletrônico" 2024..2026` | Delimita licitações e contratações dentro de um período temporal estrito. |

---

## 3. Dorks Jurídicas Estratégicas para Aplicação Imediata

### 3.1. Dork para Rastreamento de Contratos Públicos e Diários Oficiais:
```text
site:gov.br filetype:pdf ("CNPJ_DO_DEVEDOR" OR "NOME_EMPRESARIAL") ("valor global" OR "empenho")
```
*Finalidade*: Localiza pagamentos de entes públicos devidos à empresa devedora, permitindo pleitear a **penhora no rosto dos autos** ou bloqueio de faturas na repartição pública competente antes do repasse ao devedor.

### 3.2. Dork para Localização de Declaração de Bens e Candidaturas:
```text
site:tse.jus.br intext:"declaração de bens" "NOME_COMPLETO_DO_ALVO"
```
*Finalidade*: Extrai a declaração juramentada de patrimônio apresentada à Justiça Eleitoral, discriminando imóveis, veículos, contas bancárias e cotas de empresas com valores históricos.

### 3.3. Dork para Localização de Decisões Judiciais e Penhoras Anteriores:
```text
site:jus.br ("desconsideração da personalidade jurídica" OR "fraude à execução") "NOME_DO_SÓCIO"
```
*Finalidade*: Identifica se o alvo já foi condenado por confusão patrimonial em outras varas cíveis ou trabalhistas, servindo como forte indício de reiterada má-fé processual.

---

## 4. O Uso do Cache e Ferramentas de Arquivamento

Quando uma página foi alterada recentemente ou removida do ar pelo investigado, o motor de busca frequentemente armazena uma cópia estática transitória:
- **Google Cache**: Digitar na barra de endereços `cache:https://url-do-site.com` para visualizar a versão gravada pelo robô do buscador antes da exclusão.
- **Wayback Machine**: Para histórico de longo prazo, submeta a URL alvo no portal `web.archive.org`.

---

## 5. Boxes Didáticos do Capítulo

> [!TIP]
> ### 🔎 Pivô: Da Ata Notarial Digital ao Número de Matrícula
> Ao localizar uma publicação de edital de intimação ou leilão extrajudicial via dorking (`site:com.br filetype:pdf "leilão" "NOME_DO_ALVO"`), examine os anexos do edital: eles quase sempre exibem o número exato da **matrícula do imóvel e o cartório de registro de imóveis competente**, economizando semanas de pesquisas registrais.

> [!WARNING]
> ### ⚖️ Limite Jurídico: Proibição de Dorking para Intrusão (Google Hacking)
> O uso de operadores avançados para localizar documentos públicos indexados é perfeitamente lícito. Contudo, utilizar dorks para descobrir senhas de servidores expostas em arquivos `.env` ou chaves privadas de bancos de dados para ingressar em sistemas sem autorização configura ilícito penal (art. 154-A do CP) e ilícito ético-disciplinar perante o TED da OAB.

> [!NOTE]
> ### 🧪 Verificação: O Risco de Indexação Truncada
> O Google indexa apenas os primeiros megabytes de arquivos PDF muito extensos. Caso encontre um relatório ou diário oficial extenso de 500 páginas onde o nome do alvo aparece, **faça sempre o download do PDF completo e use o comando `Ctrl+F` localmente**, pois menções secundárias no final do documento podem não ter sido capturadas pelo snippet da busca.
