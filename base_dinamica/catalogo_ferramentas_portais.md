# Catálogo Vivo de Ferramentas, APIs e Portais Operacionais (Base Dinâmica)

> [!NOTE]
> **Aviso de Governança Editorial**: Este documento constitui o repositório volátil complementar do livro *OSINT Aplicado ao Direito Brasileiro*. Para evitar a obsolescência do conteúdo perene do livro, URLs dinâmicas, softwares de terceiros e procedimentos de instalação de scripts são mantidos e atualizados neste repositório digital.

---

## 1. Ferramentas de Investigação Web e Dorking

| Ferramenta | Tipo / Plataforma | Modelo de Custo | Finalidade Forense Principal | Requisitos de Acesso | Alternativa de Contingência |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Google Search Operators** | Motor de Busca Web | Gratuito | Pesquisa direcionada por tipos de arquivo (`filetype:pdf`), domínios governamentais (`site:gov.br`) e termos literais. | Nenhum (apenas navegador). | Bing Advanced Operators, DuckDuckGo, Yahoo Search. |
| **DorkSearch** | Interface Web Especializada | Gratuito | Gerador e repositório de buscas parametrizadas para localizar painéis expostos e diretórios abertos. | Navegador web. | Google Hacking Database (GHDB) da Exploit-DB. |
| **Wayback Machine (Internet Archive)** | Repositório Histórico Global | Gratuito / Doações | Visualização de versões pretéritas de websites, páginas corporativas desativadas e políticas de privacidade antigas. | Acesso web via `archive.org`. | Archive.today (`archive.ph`), Google Cache histórico. |
| **Archive.today** | Serviço de Preservação Web | Gratuito | Gravação estática de páginas com geração de link permanente, contornando bloqueios de javascript e paywalls leves. | Acesso web via `archive.is` / `archive.ph`. | Perma.cc, Wayback Machine. |

---

## 2. Ferramentas de Investigação de Identidade e Perfis Digitais

| Ferramenta | Tipo / Plataforma | Modelo de Custo | Finalidade Forense Principal | Requisitos de Acesso | Alternativa de Contingência |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Sherlock Project** | Script Python CLI (Open Source) | Gratuito | Busca automatizada de existência de determinado *username* em mais de 400 redes sociais e plataformas simultaneamente. | Python 3.9+, Git, Terminal local. | Blackbird OSINT, WhatsMyName.app. |
| **WhatsMyName Web** | Aplicação Web / API | Gratuito | Varredura ágil de *usernames* sem necessidade de linha de comando ou instalação local de dependências. | Navegador web (`whatsmyname.app`). | Sherlock CLI, Maigret CLI. |
| **Holehe** | Script Python CLI | Gratuito | Verifica se determinado endereço de e-mail possui cadastro ativo em dezenas de serviços (Twitter, LinkedIn, Instagram, etc.) sem disparar notificações. | Python 3.8+, Terminal local. | Epieos.com, Hunter.io. |
| **Epieos** | Motor Web de OSINT de E-mail | Gratuito com planos Pro | Pesquisa reversa de endereço de e-mail identificando conta Google associada, ID do Google Maps e resenhas públicas. | Navegador web (`epieos.com`). | Holehe CLI. |

---

## 3. Investigação Corporativa, Societária e Econômica

| Portal / Sistema | Entidade Gestora | Modelo de Acesso | Saída Probatória Relevante | Restrições / Requisitos |
| :--- | :--- | :--- | :--- | :--- |
| **REDESIM / Portal Gov.br** | Governo Federal / Receita Federal | Público / Login Gov.br | Emissão de Comprovante de Inscrição no CNPJ e Consulta de Quadro de Sócios e Administradores (QSA). | CPF para login gov.br. |
| **Portais das Juntas Comerciais** (JUCESP, JUCERJA, JUCEMG, etc.) | Governos Estaduais | Gratuito para busca; Pago para certidão oficial | Ficha cadastral simplificada, contratos sociais arquivados, atas de assembleia e alterações de capital. | Cadastro estadual e recolhimento de DARE/emolumento. |
| **Dados Abertos do CNPJ** | Receita Federal do Brasil | Gratuito (Download bruto) | Dataset completo de todas as empresas e sócios do Brasil, permitindo cruzamento relacional em banco de dados local. | Conhecimento em SQLite/PostgreSQL/Python para manipulação de arquivos de grande volume. |
| **Portal da Transparência da CGU** | Controladoria-Geral da União | Gratuito | Consulta ao CEIS (empresas inidôneas), CNEP (empresas punidas sob Lei Anticorrupção) e contratos federais. | Público e irrestrito. |
| **Sistema Integrado de Informações de Comércio Exterior (SISCOMEX)** | MDIC / Receita Federal | Consulta de dados agregados pública | Verificação de histórico e autorização de operações de importação e exportação de bens. | Dados individualizados exigem requerimento ou processo judicial. |

---

## 4. Investigação Imobiliária, Cartorária e Notarial

| Sistema Integrador | Abrangência | Órgão Regulador | Finalidade Investigativa | Como Operar |
| :--- | :--- | :--- | :--- | :--- |
| **SAEC / ONR (registradores.onr.org.br)** | Nacional (Todos os estados) | CNJ / Operador Nacional de Imóveis | Pesquisa de Bens por CPF/CNPJ em cartórios de registro de imóveis de todo o Brasil e pedido de certidão digital. | Cadastro e compra de créditos/emolumentos oficiais. |
| **CENSEC (censec.org.br)** | Nacional | Colégio Notarial do Brasil / CNJ | Central Notarial de Serviços Compartilhados: pesquisa de escrituras, procurações públicas e testamentos. | Módulos públicos parciais; acesso integral restrito a autoridades e partes com legitimidade. |
| **GeoSampa / Portais Municipais de Geoinformação** | Municipal (Exemplo São Paulo) | Prefeituras Municipais | Mapeamento cadastral imobiliário, consulta de IPTU, zoneamento urbano e imagens aéreas históricas. | Acesso público livre. |

---

## 5. Ferramentas de Preservação Técnica e Pericial

| Ferramenta | Tipo | Padrão Criptográfico | Diferencial Jurídico em Juízo |
| :--- | :--- | :--- | :--- |
| **SingleFile** | Extensão de Navegador (Chrome/Firefox) | Arquivo único HTML auto-contido | Salva a página web inteira em um arquivo `.html` único com todas as imagens embutidas em Base64, permitindo auditoria de código-fonte. |
| **OpenSSL / Terminal shasum** | Binário nativo de SO | Algoritmos SHA-256 / SHA-512 | Geração instantânea e universalmente aceita de hash para comprovar a imutabilidade do arquivo digital juntado aos autos. |
| **Plataformas Forenses Certificadas (Verifact, etc.)** | SaaS Forense Especializado | Hash SHA-256 + Metadados + Carimbo ICP-Brasil | Relatório pericial estruturado com espelhamento de rotas de rede, registro WHOIS e validação de carimbo de tempo reconhecido judicialmente. |
| **Wireshark** | Analisador de Pacotes de Rede | Captura PCAP com checksum | Registro detalhado de tráfego de rede para perícias de conexões e respostas de servidores remotos. |
