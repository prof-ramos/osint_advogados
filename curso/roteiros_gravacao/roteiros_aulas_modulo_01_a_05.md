# Roteiros Operacionais de Gravação em Vídeo: Módulos 01 a 05

> **Estrutura Padrão de Gravação de Cada Bloco (20 a 30 min)**:
> 1. **Gancho de Impacto (00:00 - 02:00)**: Problema prático real do contencioso.
> 2. **Fundamento Dogmático (02:00 - 10:00)**: Artigo de lei, precedentes do STJ/STF e separação epistemológica.
> 3. **Demonstração em Tela / Screencast (10:00 - 20:00)**: Operação prática na fonte primária oficial ou ferramenta.
> 4. **Compliance Drop / Pílula de Alerta (20:00 - 25:00)**: O que NÃO fazer (riscos de ilicitude, LGPD e nulidade).
> 5. **Fechamento e Missão do Aluno (25:00 - 30:00)**: Atividade prática para a matriz de evidências.

---

## 🎬 Roteiro M1.4: Prova Digital, Cadeia de Custódia e a Jurisprudência do STJ

### 1. Gancho de Impacto (Câmera Principal - Plano Médio)
> *"Você juntou no processo um print screen de uma conversa de WhatsApp em que o devedor confessa ter ocultado três apartamentos. O juiz abre prazo e o advogado da contraparte alega nulidade por quebra da cadeia de custódia. Resultado? O magistrado desentranha o print com base no Informativo 811 do STJ e você perde a penhora. Por que isso acontece? Porque em juízo, a tela do celular do seu cliente não tem valor de prova sem comprovação matemática de mesmidade."*

### 2. Fundamento Dogmático (Câmera + Slide 1)
- Explicar os arts. 158-A a 158-F do CPP e a aplicação subsidiária ao CPC (arts. 369 e 422).
- Citar os precedentes do STJ:
  - **RHC 99.735/SC**: Vulnerabilidade e possibilidade de adulteração em prints de WhatsApp.
  - **AgRg no HC 828.054/RN (Info 811 - 2024)**: Inadmissibilidade de extração por simples captura de tela quando inexiste código hash.
  - **EDcl no HC 945.157/SC (2024)**: A ressalva de prints colhidos diretamente pela vítima no aparelho e confirmados em audiência.

### 3. Screencast Operacional (Captura de Tela + Câmera PiP)
- Abrir o terminal do macOS / Linux / PowerShell.
- Demonstrar o cálculo de hash de um arquivo de captura:
  ```bash
  shasum -a 256 contrato_social_jucesp.pdf
  ```
- Alterar 1 caractere em um arquivo texto e reexecutar o comando, mostrando que o hash se transforma integralmente (efeito avalanche).
- Demonstrar como documentar o hash na Matriz de Evidências no campo 11.

### 4. Pílula de Compliance ⚖️
> *"Atenção: A ata notarial não transforma uma mentira em verdade. O tabelião apenas atesta o que viu na tela. Se a página era clonada ou o diálogo era forjado, a ata notarial não impedirá a nulidade. A única blindagem pericial definitiva é a preservação técnica com cálculo de hash e documentação de metadados."*

### 5. Fechamento e Chamada para Ação
> *"Sua missão no laboratório de hoje: pegar o documento digital do Caso Prático 01, calcular o hash SHA-256 no seu terminal e preencher os 12 campos da Matriz de Evidências. Vejo você na próxima aula!"*

---

## 🎬 Roteiro M3.2: Desambiguação de Pessoas Naturais e Triangulação Societária

### 1. Gancho de Impacto (Câmera Principal)
> *"Você pesquisou o nome do seu devedor no Google e encontrou uma empresa com capital de 10 milhões de reais. Peticiou pedindo a penhora das cotas. Três semanas depois descobre que penhorou os bens de um homônimo absoluto que nunca ouviu falar do seu cliente. Como evitar o erro mais fatal da investigação digital?"*

### 2. Fundamento Dogmático
- O princípio epistemológico da desambiguação: Nome $\neq$ Pessoa Física.
- Exigência de 3 âncoras independentes para validação de homonímia: Nome Completo + CPF (mesmo com dígitos mascarados pela LGPD) + Nome da Mãe / Data de Nascimento / Município de Domicílio Eleitoral.

### 3. Screencast Operacional
- Demonstração no portal da Receita Federal (Emissão de Comprovante de Situação Cadastral).
- Consulta a diários oficiais via Google Dorking para localização de filiação e identificadores derivados:
  `"Nome do Alvo" AND ("CPF" OR "RG" OR "filiação" OR "nascido em") filetype:pdf`
- Triangulação com a base aberta de dados CNPJ da Receita e consulta à Junta Comercial estadual.

### 4. Pílula de Compliance ⚖️
> *"Nunca utilize painéis clandestinos de vazamento de dados ('puxa-dados' via Telegram ou APIs piratas). Além de configurar crime de invasão de dispositivo ou receptação de dados ilícitos, qualquer evidência originada de base vazada será considerada prova ilícita por derivação (art. 157 do CPP) e contaminará todo o seu processo."*

---

## 🎬 Roteiro M4.7: Transição de OSINT para Medidas Judiciais e o SNIPER

### 1. Gancho de Impacto
> *"Você esgotou as fontes abertas, mapeou que o executado ostenta uma vida de milionário nas redes sociais, mas não há um único centavo no SISBAJUD. O que fazer agora? OSINT é apenas a primeira metade do caminho: os indícios colhidos em fontes abertas servem para convencer o juiz a quebrar sigilos e ativar sistemas que a advocacia não tem acesso direto."*

### 2. Fundamento Dogmático
- CPC art. 381: Produção Antecipada de Provas sem valoração de mérito (STJ REsp 1.774.913/SP).
- O dever de cooperação judiciária (CPC arts. 6º e 67 a 69) e a Resolução nº 350/2020 do CNJ.
- O Sistema Nacional de Investigação Patrimonial e Recuperação de Ativos (SNIPER/CNJ).
- Medidas atípicas do art. 139, IV do CPC e os parâmetros vinculantes do Tema 1137 do STJ e ADI 5941 do STF.

### 3. Screencast Operacional
- Demonstração do fluxograma de peticionamento: Indício OSINT $\to$ Nexo de Ocultação $\to$ Pedido Específico de Interoperabilidade Judicial.
- Exibição de modelo de minuta com pedido subsidiário de ativação do módulo Teimosinha do SISBAJUD (30 dias) e expedição de ofício via SNIPER.
