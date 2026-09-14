# OSINT Jurídico Brasileiro

Contexto metodológico e normativo para a prática de investigação em fontes abertas, preservação de evidências digitais e atuação probatória estratégica perante os tribunais brasileiros.

## Language

### Epistemologia e Prova

**Dado Bruto**:
O elemento alfanumérico, textual ou binário isolado, sem juízo de valor ou contextualização interpretativa.
_Avoid_: Fato, prova, evidência

**Fato Verificado**:
A constatação objetiva atestada por certidão com fé pública, registro imutável ou documento primário oficial.
_Avoid_: Suposição, alegação, certeza moral

**Indício**:
A circunstância fática conhecida e provada que, por indução lógica, autoriza concluir a existência de outro fato desconhecido (art. 239 do CPP).
_Avoid_: Mera suspeita, palpite, fofoca

**Inferência Analítica**:
A dedução lógica fundamentada nas regras de experiência comum que conecta múltiplos indícios convergentes a uma tese fática.
_Avoid_: Conclusão definitiva, certeza matemática

**Hipótese Investigativa**:
A proposição fática preliminar que orienta a busca, sujeita a confirmação ou refutação por novas diligências.
_Avoid_: Veredito, juízo de culpa

**Mesmidade**:
A garantia técnica e matemática de que o vestígio digital apresentado em juízo é idêntico ao coletado na fonte de origem.
_Avoid_: Semelhança, cópia aproximada

### Investigação e Fontes

**Pivô**:
A técnica de extrair um novo identificador a partir do resultado de uma consulta para alimentar a busca seguinte.
_Avoid_: Pulo, atalho, salto aleatório

**Identificador Inicial (Seed)**:
O dado primário de partida confirmado documentalmente (ex.: nome, CPF, CNPJ, telefone, placa, domínio).
_Avoid_: Chute, pista informal

**Fonte Primária Oficial**:
Base de dados pública ou repositório mantido diretamente por órgão do Estado com presunção de autenticidade (Planalto, Tribunais, Receita Federal, Juntas Comerciais, Cartórios).
_Avoid_: Blog, portal agregador, notícia de jornal

**Investigação Defensiva**:
Complexo de diligências investigatórias lícitas conduzidas privativamente pelo advogado em benefício de seu constituinte (Provimento nº 188/2018 do CFOAB).
_Avoid_: Investigação paralela clandestina, espionagem privada

**Beneficiário Final**:
A pessoa natural que, em última análise, possui, controla ou influencia significativamente uma entidade jurídica ou patrimônio sob custódia (IN RFB nº 2.119/2022).
_Avoid_: Dono informal, patrão

### Governança Probatória e Arquitetura

**Cadeia de Custódia Probatória**:
O conjunto de todos os procedimentos formais utilizados para manter e documentar a história cronológica do vestígio coletado em fontes digitais (art. 158-A do CPP).
_Avoid_: Coleta informal, print solto, captura desregrada

**Matriz de Evidências**:
Tabela analítica estruturada de custódia que correlaciona cada ID probatório (`EVD-XXX`) ao seu registro temporal com fuso horário UTC-3, hash criptográfico SHA-256 e inferência lógica aplicável.
_Avoid_: Anotação preliminar, relatório desestruturado

**Base Dinâmica**:
Repositório complementar de ferramentas, APIs, portais e scripts voláteis desacoplado do livro perene para prevenir a obsolescência técnica precoce da obra doutrinária (ADR-0001).
_Avoid_: Livro estático desatualizado, catálogo misturado com doutrina

**Compilação Editorial**:
Pipeline automatizado de consolidação que valida e compila os 24 capítulos sequenciais nos formatos Markdown monólito, HTML estruturado para impressão e EPUB 3 com validação semântica.
_Avoid_: Cópia manual, diagramação não reprodutível

