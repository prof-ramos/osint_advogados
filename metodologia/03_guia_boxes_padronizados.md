# Guia Editorial: Os 8 Boxes Padronizados de Aprendizagem

## 1. Finalidade Pedagógica e Operacional dos Boxes

Para garantir uma leitura dinâmica, visualmente identificável e diretamente aplicável à prática da advocacia, todos os capítulos do livro e estudos de caso utilizam **8 componentes visuais padronizados (boxes)**.

Cada box cumpre um propósito cognitivo estrito, evitando digressões e fornecendo orientações práticas imediatas para a tomada de decisão do advogado.

---

## 2. Catálogo e Semântica dos 8 Boxes

### 1. ⚖️ Limite Jurídico
- **Propósito**: Alerta o leitor sobre barreiras normativas intransponíveis, riscos de violação à LGPD, nulidade de prova ou tipificação penal (ex.: art. 154-A do CP, violação de sigilo profissional).
- **Quando usar**: Sempre que uma técnica técnica estiver próxima da fronteira da ilicitude (ex.: tentar acessar áreas restritas por senha, usar bases vazadas, simular identidade para obter dados confidenciais).
- **Formato Markdown**:
  ```markdown
  > [!WARNING]
  > ### ⚖️ Limite Jurídico: Proibição de Uso de Dados Vazados
  > A utilização de credenciais extraídas de vazamentos (data breaches) para acessar sistemas privados constitui crime de invasão de dispositivo informático (art. 154-A do CP). A prova obtida é ilícita (art. 5º, LVI, da CF) e contamina todas as evidências derivadas.
  ```

---

### 2. 🔎 Pivô
- **Propósito**: Demonstra exatamente qual novo identificador técnico ou cadastral pode ser extraído do resultado atual para alimentar a próxima rodada de consultas.
- **Quando usar**: Após a apresentação do resultado de uma busca em fonte primária ou registro público.
- **Formato Markdown**:
  ```markdown
  > [!TIP]
  > ### 🔎 Pivô: Da Razão Social ao CPF dos Sócios
  > Ao consultar o CNPJ da empresa na REDESIM/Receita Federal, extraia o Quadro de Sócios e Administradores (QSA). Os nomes dos sócios e seus CPFs parciais (formato `***.123.456-**`) servem como novos identificadores para buscas na Junta Comercial e no sistema de processos dos Tribunais.
  ```

---

### 3. 🚩 Sinal de Atenção (*Red Flag*)
- **Propósito**: Aponta anomalias operacionais, societárias ou financeiras que costumam indicar tentativa de ocultação patrimonial, blindagem abusiva ou fraude a credores.
- **Quando usar**: Ao analisar alterações contratuais, endereços inconsistentes, procurações com poderes amplos ou criação súbita de holdings familiares.
- **Formato Markdown**:
  ```markdown
  > [!IMPORTANT]
  > ### 🚩 Sinal de Atenção: Sócia Recém-Emancipada com Capital Milionário
  > A cessão gratuita de quotas sociais de empresa operacional lucrativa para descendente de 18 anos recém-completados, sem capacidade financeira autônoma, é forte indício de doação inoficiosa e fraude à execução.
  ```

---

### 4. ⚠️ Não Conclua Ainda!
- **Propósito**: Freia o ímpeto conclusivo precipitado do analista, demonstrando por que uma simples correlação não é suficiente para demonstrar autoria, titularidade ou culpa.
- **Quando usar**: Em situações propensas ao erro de homonímia, usernames coincidentes em redes sociais distintas ou compartilhamento de endereços corporativos (ex.: coworkings).
- **Formato Markdown**:
  ```markdown
  > [!CAUTION]
  > ### ⚠️ Não Conclua Ainda: O Risco do Endereço em Coworking
  > Encontrar o mesmo endereço cadastral para duas empresas não comprova confusão patrimonial se o local for um edifício de escritórios compartilhados (*virtual office*). É indispensável verificar se ambas dividem telefone, funcionários, procuradores ou contas bancárias.
  ```

---

### 5. 🧪 Verificação e Triangulação
- **Propósito**: Prescreve o teste prático de validação cruzada que deve ser executado para conferir se a informação encontrada é autêntica e confiável.
- **Quando usar**: Quando o dado foi obtido de fonte secundária ou carece de corroboração independente.
- **Formato Markdown**:
  ```markdown
  > [!NOTE]
  > ### 🧪 Verificação: Desambiguação de Homônimo via Filiação
  > Ao localizar processo judicial envolvendo nome idêntico ao do alvo, confronte o nome da mãe, data de nascimento ou profissão com as informações constantes do Cadastro Nacional de Eleitores ou contrato societário formal.
  ```

---

### 6. 📦 Preservação Forense
- **Propósito**: Ensina passo a passo como registrar o dado para que ele seja aceito como vestígio autêntico e íntegro perante o magistrado.
- **Quando usar**: Imediatamente após a descoberta de qualquer vestígio digital volátil ou página web passível de remoção.
- **Formato Markdown**:
  ```markdown
  > [!NOTE]
  > ### 📦 Preservação: Captura com Hash SHA-256 e Cabeçalho HTTP
  > Não se limite a salvar como imagem JPEG. Exporte a página como arquivo WARC ou PDF estruturado, salve o código-fonte HTML integral e gere imediatamente o código hash SHA-256 via terminal (`shasum -a 256 arquivo.html`), anexando ao diário de buscas.
  ```

---

### 7. 🏛️ Medida Judicial Necessária
- **Propósito**: Estabelece o ponto exato em que a pesquisa em fontes abertas atingiu seu limite instrutório legal e a postulação judicial coercitiva se torna obrigatória.
- **Quando usar**: Quando a continuidade da apuração exige quebra de sigilo bancário, fiscal, registros de conexão de provedores ou busca e apreensão.
- **Formato Markdown**:
  ```markdown
  > [!IMPORTANT]
  > ### 🏛️ Medida Judicial: Requisição de Registros via Marco Civil
  > A identificação do usuário anônimo por trás de um perfil falso no Instagram exige ajuizamento de ação com pedido liminar baseado no art. 22 da Lei 12.965/2014, pleiteando o fornecimento dos registros de acesso à aplicação (IP, porta lógica, data e fuso UTC).
  ```

---

### 8. 🇧🇷 Fonte Brasileira Relevante
- **Propósito**: Aponta o órgão governamental, cartório ou registro público oficial brasileiro adequado para obtenção daquele dado primário específico.
- **Quando usar**: Na transição entre o problema investigativo e as bases públicas brasileiras.
- **Formato Markdown**:
  ```markdown
  > [!TIP]
  > ### 🇧🇷 Fonte Brasileira: Registro de Imóveis do Brasil (ONR / SREI)
  > No Brasil, a pesquisa de titularidade imobiliária unificada por CPF/CNPJ em âmbito nacional deve ser realizada prioritariamente pelo Serviço de Atendimento Eletrônico Compartilhado (SAEC) do Operador Nacional do Sistema de Registro Eletrônico de Imóveis (ONR).
  ```
