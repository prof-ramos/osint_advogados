# CODING_STANDARDS.md

Este documento estabelece os padrões normativos, metodológicos e técnicos para contribuição, escrita e revisão de código e documentação no repositório **OSINT Jurídico**.

> [!NOTE]
> Este documento é consultado primariamente pelos agentes revisores durante o processo de *Code Review*.

---

## 1. Integridade de Evidências Digitais e Cadeia de Custódia (ISO/IEC 27037 & Art. 158-A CPP)

Todo caso prático, exercício ou estudo de caso que mencione artefatos digitais deve cumprir estritamente as seguintes regras:

1. **Padrão de Identificadores**:
   - Identificadores de evidência devem seguir estritamente o formato `EVD-\d{3}` (ex.: `EVD-001`, `EVD-002`, ..., `EVD-014`).
   - É proibido o uso de IDs com menos de 3 dígitos (ex.: `EVD-1` ou `EVD-01`).
2. **Hashes Criptográficos**:
   - Todo arquivo preservado deve conter seu respectivo código hash **SHA-256**.
   - O hash deve conter exatamente **64 caracteres hexadecimais** (`^[a-f0-9]{64}$`).
   - **Proibições rígidas**:
     - É expressamente proibido o truncamento de hashes com reticências (ex.: `d4a8e2b1...9c3f`).
     - É expressamente proibido o uso do hash da string vazia (`e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`).
3. **Carimbo Temporal com Fuso Horário**:
   - Todo registro de coleta deve conter carimbo de data e hora com fuso horário explícito (ex.: `2026-09-08 11:00 BRT`, `BRT (UTC-3)` ou padrão ISO 8601 `2026-09-08T11:00:00-03:00`).
4. **Identificação do Arquivo Preservado**:
   - A coluna de preservação da matriz deve explicitar o nome de arquivo com sua extensão técnica real entre crases (ex.: `arquivo_coletado.pdf`, `post_linkedin.html`, `trafego_rede.har`).

---

## 2. Estrutura Canônica dos Casos Práticos (`casos_praticos/`)

Cada arquivo em `casos_praticos/` deve estruturar-se nas seguintes seções:

1. `## 1. Síntese do Caso e Problema Jurídico`: Contextualização material e objetivo processual (ex.: execução de alimentos, localização de bens, ação rescisória).
2. `## 2. Dados Iniciais Disponíveis`: Vetores e sementes iniciais conhecidos.
3. `## 3. Hipóteses e Trilha de Investigação`: formulação de teses e pivôs sucessivos.
4. `## 4. Diário de Buscas e Execução Operacional`: Tabela cronológica com Fonte, Termo de Busca, Resultado Bruto e Decisão do Analista.
5. `## 5. Matriz de Evidências`: Matriz tabular com os 12 campos metodológicos.
6. `## 6. Boxes de Aprendizagem Aplicados`: Pelo menos 2 boxes pedagógicos no formato GitHub Alerts.
7. `## 7. Desfecho Jurídico e Aplicação Prática`: Petição, minuta de requerimento ou providência forense concreta demonstrando o uso processual da evidência.

---

## 3. Separação Arquitetural: Conteúdo Perene vs. Base Dinâmica (ADR-0001)

- **Livro (`livro/`)**:
  - Foco em princípios fundamentais do Direito, lógica dos registros públicos (LRP, Lei 6.015/73), raciocínio investigativo, teoria da prova digital e cadeia de custódia.
  - Proibido acoplar o texto a interfaces efêmeras de ferramentas web ou scripts que quebrem em curto prazo.
- **Base Dinâmica (`base_dinamica/`)**:
  - Catálogo vivo e versionado de ferramentas, bases comerciais, APIs e tabelas de órgãos públicos. Sujeito a atualizações contínuas.

---

## 4. Padrão de Boxes Metodológicos

Utilizar a sintaxe padronizada de GitHub Alerts conforme [metodologia/03_guia_boxes_padronizados.md](file:///Users/gabrielramos/Developer/personal/osint_advogados/metodologia/03_guia_boxes_padronizados.md):

| Box | Tipo de Alerta | Emoji / Título |
| :--- | :--- | :--- |
| 1. Pivô | `> [!TIP]` | `### 🔎 Pivô: [Título]` |
| 2. Não Conclua Ainda | `> [!CAUTION]` | `### ⚠️ Não Conclua Ainda: [Título]` |
| 3. Onde OSINT Para | `> [!IMPORTANT]` | `### 🛑 Onde OSINT Para e Entra a Medida Judicial: [Título]` |
| 4. Validade Jurídica | `> [!NOTE]` | `### ⚖️ Validade Jurídica e Jurisprudência: [Título]` |
| 5. Falácia da Fonte Única | `> [!WARNING]` | `### 🧩 Falácia da Fonte Única: [Título]` |
| 6. LGPD & Ética | `> [!NOTE]` | `### ⚠️ LGPD & Ética: [Título]` |
| 7. Passo a Passo | `> [!IMPORTANT]` | `### 📋 Passo a Passo: [Título]` |
| 8. Dica de Eficiência | `> [!TIP]` | `### ⚡ Dica de Eficiência: [Título]` |

---

## 5. Rigor Terminológico (Conforme CONTEXT.md)

- Não utilizar "Dado Bruto" como sinônimo de "Prova" ou "Fato Verificado".
- Não utilizar "OSINT" como sinônimo de invasão ou intrusão (proibição expressa de violação ao art. 154-A do CP).
- Aplicar os termos com precisão: *Mesmidade*, *Pivô*, *Indício*, *Investigação Defensiva* e *Beneficiário Final*.
