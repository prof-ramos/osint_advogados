# Estudo de Caso Prático 05: Publicação Posteriormente Apagada e Cadeia de Custódia

## 1. Cenário Fático e Mandato Investigativo

- **Cliente**: Cooperativa Agrícola Verde Vale.
- **Caso**: Ação Trabalhista com Pedido de Indenização por Assédio Moral Coletivo e Danos Extrapatrimoniais (Proc. nº 0001890-72.2025.5.12.0035 - Vara do Trabalho de Chapecó/SC).
- **Alvo**: Agroindústria e Frigorífico Boi Gordo S/A.
- **Problema Jurídico**: O diretor industrial da reclamada publicou em seu perfil corporativo no LinkedIn um texto comemorando o "recorde de produtividade", no qual confessava explicitamente que os operadores de abate haviam trabalhado durante 18 horas ininterruptas em câmara fria sem pausas térmicas. Ao ser alertado pelo setor jurídico interno sobre a confissão de infração às NRs e jornada exaustiva, o executivo apagou a postagem 4 horas após a publicação. A empresa nega categoricamente em juízo a existência do fato e acusa o reclamante de "fabricar prints falsos".
- **Pergunta Investigativa**: *Como comprovar a higidez, integridade, temporalidade e autoria da postagem excluída, superando a tese de manipulação digital e falsidade documental arguida pela reclamada?*
- **Base Legal**: Arts. 369, 422 e 424 do CPC (subsidiários à CLT); Arts. 158-A e seguintes do CPP (princípios da cadeia de custódia).

---

## 2. Ponto de Partida e Identificadores Iniciais (*Seeds*)

- **URL Original da Postagem (excluída)**: `https://www.linkedin.com/posts/gustavo-silva-agro_produtividade-recorde-frigorifico-activity-7192837465019283746-aB1c`.
- **Nome do Autor da Postagem**: Gustavo Henrique da Silva (Diretor Operacional).
- **Momento da Publicação Original**: 14 de maio de 2025, aproximadamente às 18h30.
- **Momento da Exclusão**: 14 de maio de 2025, às 22h40.

---

## 3. Cadeia de Preservação e Rastreamento de Web Histórica

```
[Publicação Visualizada pelo Reclamante às 19h15]
       │
       ▼ (Procedimento Preventivo Imediato pelo Advogado)
[Captura Técnica Completa via SingleFile: HTML + Base64 + CSS em Arquivo Único]
       │
       ▼ (Submissão Concomitante a Serviços Públicos de Arquivamento Web)
[Submissão aos motores do Wayback Machine (Archive.org) e Archive.today (Archive.ph)]
       │
       ▼ (Extração de Cabeçalhos de Rede / Console do Navegador)
[Gravação de arquivo HAR (HTTP Archive) registrando status 200 OK do LinkedIn e IP do CDN]
       │
       ▼ (Cálculo Imediato de Hash Criptográfico)
[Geração de SHA-256 sobre o arquivo .html, .har e captura de tela PNG em alta resolução]
       │
       ▼ (Acontecendo a Exclusão do Post às 22h40)
[Tentativa de acesso à URL original retorna Erro 404 / "Publicação indisponível"]
       │
       ▼ (Confronto de Fontes Históricas)
[O snapshot no Archive.today permanece imutável e com carimbo de tempo do servidor externo]
```

---

## 4. Diário de Buscas e Procedimentos Periciais de Preservação

| Data/Hora (UTC-3) | Procedimento Técnico Executado | Ferramenta Utilizada | Arquivo Gerado / Hash SHA-256 |
| :--- | :--- | :--- | :--- |
| 14/05/2025 19:22 | Captura do código-fonte completo e elementos gráficos integrados. | Extensão SingleFile (Chromium). | `linkedin_post_gustavo_silva_20250514.html`<br>`Hash: 4a2b9f81c7e...3d91` |
| 14/05/2025 19:24 | Gravação de tráfego de rede e resposta do servidor remoto da Microsoft/LinkedIn. | DevTools do Navegador (Network Export HAR). | `linkedin_network_traffic_20250514.har`<br>`Hash: 8f10c32d4b...9a12` |
| 14/05/2025 19:28 | Requisição de arquivamento no Archive.today. | API / Web Form do Archive.ph | Snapshot permanente gravado na URL: `https://archive.ph/2025.05.14-222815/https://www.linkedin.com/posts/...` |
| 14/05/2025 19:35 | Registro de carimbo de tempo com protocolo de auditoria. | Plataforma de Registro Criptográfico com Carimbo ICP-Brasil. | Certificado Técnico de Preservação nº 2025-BR-9912. |

---

## 5. Matriz de Evidências

| ID | Fato Investigado | Informação Encontrada | Fonte | Data | Tipo | Confiabilidade | Corroboração | Limitação | Classificação | Preservação | Utilidade Jurídica |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **EVD-009** | Confissão de jornada de trabalho abusiva e sem pausas térmicas. | Texto expresso do diretor: *"Nossa equipe de abate bateu 18h seguidas de operação hoje sem parar as esteiras da câmara fria"*. | LinkedIn (Perfil oficial de Gustavo Henrique da Silva). | 14/05/2025 19:22 BRT | Primária | Alta (Confissão extrajudicial - art. 389 CPC) | Corroborado por relatórios de pesagem de carga e cartões de ponto que atestam ausência de marcação. | O post foi excluído posteriormente pelo autor da página. | Fato Verificado (Materialidade e autoria da manifestação). | Arquivo `linkedin_post_gustavo_silva_20250514.html` (Hash SHA-256: `10b9798bae81cb179b9cbf2237a77e10996d3911bd669247e4b934410c7bdac0`). | Instruir inicial trabalhista como confissão real da reclamada (art. 391 do CPC). |
| **EVD-010** | Conduta intencional de supressão probatória (*spoliation of evidence*). | Exclusão do conteúdo poucas horas após repercussão negativa interna. | Comparação entre o snapshot das 19h28 e a resposta HTTP 404 das 22h50. | 14/05/2025 22:50 BRT | Técnica | Alta | Corroborado pelos logs de indisponibilidade da URL. | O LinkedIn não informa publicamente o motivo da exclusão (se pelo usuário ou denúncia). | Fato Verificado (Supressão do conteúdo da rede). | Arquivo `linkedin_network_traffic_20250514.har` (Hash SHA-256: `ec67bac0cdcd2ace70b73c72c68f168853a3a1bff23bae2af42f16bce843b576`). | Pedir aplicação de presunção de veracidade dos fatos articulados pela parte adversa (CPC, art. 400). |

---

## 6. Boxes de Aprendizagem Aplicados

> [!NOTE]
> ### 📦 Preservação: O Tripé da Evidência Web Descentralizada
> Jamais confie exclusivamente no disco rígido do seu computador. Uma evidência digital web é considerada robusta pelo Judiciário quando apoiada em um **tripé de redundância**:
> 1. **Cópia Local com Hash**: O arquivo HTML bruto salvo localmente, com hash calculado na hora;
> 2. **Espelho em Terceiro Confiável**: A preservação automática em repositórios neutros e imutáveis públicos (Wayback Machine / Archive.today);
> 3. **Rastreabilidade de Tráfego**: Os metadados de requisição HTTP (arquivo HAR) comprovando o IP do servidor de origem e a ausência de manipulação local.

> [!WARNING]
> ### ⚖️ Limite Jurídico: Impugnação de Print e a Perícia Técnica
> Se a parte contrária impugnar a veracidade do conteúdo alegando montagem (CPC, art. 428, I), a mera juntada de imagem PNG ou JPEG será considerada imprestável pelo juiz. Porém, a apresentação do arquivo HTML original com os hashes conferíveis em audiência transfere para a parte que arguiu a falsidade o ônus de provar a adulteração (CPC, art. 429, I).

---

## 7. Desfecho Jurídico e Aplicação Prática

Na audiência de instrução na Vara do Trabalho de Chapecó, a reclamada sustentou formalmente a falsidade da prova, afirmando que a imagem juntada na petição era uma "montagem grotesca feita em Photoshop".

O advogado do reclamante, contudo, peticionou disponibilizando em juízo:
1. O arquivo digital original `linkedin_post_gustavo_silva_20250514.html` em mídia física lacrada;
2. A conferência do código hash SHA-256 diretamente no terminal do tribunal perante o juiz;
3. O link público e auditável do Archive.today gerado na data do fato;
4. O requerimento de aplicação das penalidades de litigância de má-fé caso a empresa persistisse na falsa arguição de falsidade.

Diante da higidez técnica incontestável da cadeia de custódia, o magistrado rejeitou a impugnação da reclamada, considerou a manifestação como **confissão extrajudicial espontânea** da empregadora e condenou a empresa ao pagamento de horas extras, adicional de insalubridade e indenização por assédio moral coletivo no valor de R$ 500.000,00.
