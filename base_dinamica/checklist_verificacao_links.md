# Checklist e Rotina de Auditoria Periódica da Base Dinâmica

## 1. Diretriz de Manutenção Contínua

As fontes abertas digitais, repositórios de ferramentas no GitHub e interfaces governamentais passam por constantes reformulações, manutenções técnicas e alterações legislativas.

Para garantir que a base operacional permaneça funcional para leitores e alunos de cursos, adota-se o seguinte protocolo de **revisão periódica trimestral**:

---

## 2. Checklist Trimestral de Auditoria Operacional

- [ ] **1. Portais Governamentais Oficiais (`.gov.br` / `.jus.br`)**:
  - [ ] Verificar se a URL de consulta ao QSA da Receita Federal permanece ativa ou migrou para nova interface do Gov.br.
  - [ ] Testar a emissão de certidões simplificadas nas principais Juntas Comerciais (JUCESP, JUCERJA, JUCEMG, JUCISRS).
  - [ ] Verificar se o Portal da Transparência da CGU alterou parâmetros de consulta pública de servidores e contratos.
  - [ ] Checar disponibilidade e eventuais novos módulos do SAEC / ONR para registro de imóveis.

- [ ] **2. Repositórios e Scripts Open Source (GitHub / CLI)**:
  - [ ] Executar teste automatizado com Sherlock / Blackbird para identificar quebra de seletores ou falsos positivos em redes sociais brasileiras.
  - [ ] Testar o script Holehe contra serviços nacionais (Mercado Livre, Globoplay, Nubank, etc.) para verificar bloqueios de requisições.
  - [ ] Avaliar se os repositórios oficiais receberam novos commits ou se foram descontinuados/arquivados pelo mantenedor.

- [ ] **3. Ferramentas de Preservação e Verificação Web**:
  - [ ] Verificar compatibilidade da extensão SingleFile com as versões mais recentes dos navegadores Chromium e Firefox.
  - [ ] Testar tempo de resposta e limitações de cota do Wayback Machine (`web.archive.org`) e Archive.today.
  - [ ] Auditar conformidade dos certificados digitais de carimbo de tempo ICP-Brasil emitidos por plataformas de custódia.

- [ ] **4. Marco Regulatório e Segurança Jurídica**:
  - [ ] Conferir publicação de novas resoluções da ANPD sobre dosimetria ou legítimo interesse.
  - [ ] Auditar jurisprudência recente do STJ em "Jurisprudência em Teses" para verificar se houve novos julgados sobre nulidade de prints ou cadeia de custódia.
  - [ ] Acompanhar regulamentações do CNJ sobre custódia digital de provas (evolução do GT da Portaria 391/2025).

---

## 3. Registro de Auditorias Realizadas

| Ciclo de Auditoria | Data de Execução | Responsável Técnico | Fontes / Links Descontinuados | Ação Corretiva Implementada |
| :--- | :--- | :--- | :--- | :--- |
| **Auditoria Inicial (Ciclo 0)** | 2026-09-10 | Antigravity AI / Gabriel Ramos | Links antigos de blogs e URLs truncadas da Câmara | Substituição por URLs oficiais do Planalto, CFOAB e repositório canônico. |
| **Próxima Revisão Agendada** | 2026-12-10 | Coordenação Técnica | A conferir | Rotina programada no cronograma editorial. |
