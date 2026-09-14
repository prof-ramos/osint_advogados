# Caderno de Exercícios Práticos e Laboratórios Forenses

> **Material Didático Oficial**: Baseado nos 7 Estudos de Caso Reais Simulados do projeto OSINT Jurídico.  
> **Objetivo**: Fixação prática de coleta, preservação com hash SHA-256, triangulação contra homonímia e redação de minutas processuais.

---

## 📝 Exercício 1: Rastreamento de Domicílio Contemporâneo (Caso Prático 01)

### Enunciado do Problema:
O executado Roberto Silveira Meirelles esquiva-se de citações judiciais há 18 meses. O oficial de justiça certificou por três vezes que o réu "mudou-se para local incerto e não sabido". O cliente contratou seu escritório para descobrir o domicílio contemporâneo real do devedor sem recorrer a bases ilícitas ou vazadas.

### Tarefas do Aluno:
1. Identificar no mínimo duas fontes abertas oficiais ou públicas para localização do domicílio profissional e residencial.
2. Formular uma string de Google Dorking para pesquisar atos societários ou registros de conselhos de classe em formato PDF.
3. Preencher a linha correspondente na Matriz de Evidências, gerando o hash SHA-256 de um documento comprobatório fictício.
4. Elaborar o parágrafo de petição informando o novo endereço ao juízo da execução.

### Gabarito Comentado e Rubrica de Avaliação:
- **Fontes Válidas**: Ficha cadastral simplificada da Junta Comercial estadual (JUCESP/JUCERJA) e consulta ao cadastro público do Conselho Regional de Engenharia (CREA) ou Medicina (CRM).
- **Dorking Recomendado**:
  `"Roberto Silveira Meirelles" (CREA OR "registro profissional" OR "consultório") site:gov.br OR site:org.br filetype:pdf`
- **Critério Forense**: O aluno deve incluir a data e hora com fuso de Brasília (UTC-3), nome do arquivo com extensão entre crases (ex.: `certidao_crea_sp.pdf`) e hash SHA-256 com exatamente 64 caracteres.

---

## 📝 Exercício 2: Desmascarando a Blindagem por Holding Familiar (Caso Prático 02)

### Enunciado do Problema:
A empresa devedora Alpha Logística e Transportes Ltda. teve todas as contas zeradas no SISBAJUD. Contudo, seu sócio administrador circula com automóvel importado e reside em mansão de alto padrão em condomínio fechado. A investigação aponta para uma holding patrimonial familiar recém-criada em nome dos filhos universitários.

### Tarefas do Aluno:
1. Mapear o quadro societário da holding familiar e demonstrar a ausência de capacidade econômico-financeira dos sócios formais (estudantes universitários sem renda declarada).
2. Localizar no SAEC/ONR o registro imobiliário do imóvel residencial da família integralizado no capital da holding a preço vil.
3. Redigir pedido de Incidente de Desconsideração da Personalidade Jurídica (IDPJ) com fundamento no art. 50 do Código Civil e art. 133 do CPC.

### Gabarito Comentado e Rubrica de Avaliação:
- **Elementos Probatórios**: Cruzamento entre o QSA da Receita Federal (data de abertura da holding concomitante ao início das execuções) e a certidão de inteiro teor da matrícula imobiliária demonstrando transferência patrimonial fraudulenta.
- **Tese Jurídica**: Configuração de desvio de finalidade e confusão patrimonial (CC, art. 50, § 2º), permitindo a constrição dos ativos da holding familiar para satisfação das dívidas da empresa operacional.

---

## 📝 Exercício 3: Prova de Sinais Exteriores de Riqueza em Alimentos (Caso Prático 03)

### Enunciado do Problema:
O alimentante alega auferir renda mensal de apenas R$ 2.500,00 como autônomo, requerendo a redução da pensão dos filhos. Todavia, em postagens recentes em redes sociais públicas (Instagram e LinkedIn), exibe viagens para a Europa, relógios de luxo e pilotagem de lancha esportiva de sua propriedade de fato.

### Tarefas do Aluno:
1. Estabelecer o protocolo de preservação técnica forense das postagens públicas sem quebra da cadeia de custódia.
2. Explicar por que a juntada de simples *print screen* unilateral é arriscada à luz do Informativo 811 do STJ.
3. Redigir a minuta de impugnação à revisional de alimentos com base na Teoria da Aparência e no julgado do STJ **AgInt no AREsp 1.834.120/SP**.

### Gabarito Comentado e Rubrica de Avaliação:
- **Protocolo de Custódia**: Captura de página web completa (.warc / .html com cabeçalhos de rede), gravação de tela com áudio ambiental demonstrando a navegação na URL viva, e cálculo imediato de hash SHA-256 do arquivo de vídeo/captura.
- **Precedente Aplicado**: O STJ reconhece que os sinais exteriores de riqueza comprovados por fotografias públicas e ostentação de viagens autorizam a presunção de capacidade contributiva superior à renda formal alegada pelo devedor de alimentos.

---

## 📝 Exercício 4: Atribuição de Perfil Anônimo Difamatório (Caso Prático 04)

### Enunciado do Problema:
Um perfil anônimo no Instagram difama reiteradamente uma sociedade de advogados e seus clientes. A equipe de investigação precisa obter os dados de conexão para identificar a autoria civil e criminal do ilícito.

### Tarefas do Aluno:
1. Identificar as providências preliminares sob o Marco Civil da Internet (art. 22 da Lei 12.965/2014).
2. Explicar a relevância do fornecimento da **Porta Lógica de Origem** em conexões CGNAT, citando os precedentes do STJ (**REsp 1.784.156/SP** e **REsp 1.777.769/SP**).
3. Elaborar a minuta da petição de ação cautelar de fornecimento de registros telemáticos contra o provedor de aplicação (Meta/Instagram).
