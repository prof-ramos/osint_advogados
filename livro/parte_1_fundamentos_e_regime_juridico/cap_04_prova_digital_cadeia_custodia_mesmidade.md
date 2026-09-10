# Capítulo 04: Prova Digital em Juízo: Cadeia de Custódia, Mesmidade, Ata Notarial e Jurisprudência dos Tribunais Superiores

## 1. A Epistemologia da Prova Digital e a Ilusão da Tela

A prova digital possui natureza ontológica radicalmente diversa da prova física documental tradicional:
- **Intangibilidade e Dinamismo**: Vestígios digitais residem em pulsos eletromagnéticos, tabelas relacionais de bancos de dados e sequências binárias de bits, e não no suporte plástico ou papel onde são temporariamente exibidos.
- **Extrema Volatilidade**: Qualquer interação descuidada (abrir um arquivo, ligar um computador, atualizar um feed) altera os metadados de acesso (`atime`, `mtime`), desconfigurando o vestígio original.
- **Facilidade Extrema de Manipulação**: Ferramentas simples de inspeção de código-fonte em navegadores (DevTools) e aplicativos geradores de diálogos falsos de WhatsApp permitem forjar diálogos, horários e fotos em segundos, tornando a captura de tela estática (*print screen*) uma prova de idoneidade presumida nula quando impugnada.

Em juízo, o magistrado não julga o que está na "tela do celular do advogado", mas a **autenticidade, integridade e confiabilidade da cadeia de processamento** que transportou aquele dado do emissor até os autos do processo.

---

## 2. O Princípio da Mesmidade e a Rastreabilidade

O **Princípio da Mesmidade** é o postulado epistemológico fundamental da prova digital: impõe a garantia técnica e jurídica de que o dado digital apresentado em juízo no momento da sentença é **exata e matematicamente idêntico** ao vestígio digital encontrado no ambiente computacional de origem no instante de sua coleta.

Essa identidade é assegurada pelo uso de funções criptográficas de dispersão unidirecional (**hashing**), com destaque para os algoritmos **SHA-256** e **SHA-512**. O código hash atua como a "impressão digital matemática" de um conjunto de bits: qualquer alteração de um único byte no arquivo original gera um código hash totalmente diferente (efeito avalanche), demonstrando de pronto a perda de integridade.

---

## 3. A Cadeia de Custódia: Da Esfera Penal à Aplicação no Processo Civil

Com o advento da Lei nº 13.964/2019 (Pacote Anticrime), o Código de Processo Penal positivou os arts. 158-A a 158-F, definindo a cadeia de custódia como:
> *"O conjunto de todos os procedimentos utilizados para manter e documentar a história cronológica do vestígio coletado em locais ou em vítimas de crimes, para rastrear sua posse e manuseio a partir de seu reconhecimento até o descarte."*

### As 10 Etapas Rígidas e sua Equivalência no OSINT:
1. **Reconhecimento**: Distinguir o elemento de interesse forense.
2. **Isolamento**: Evitar que terceiros ou o próprio analista alterem o estado do dado.
3. **Fixação**: Descrição detalhada do vestígio em diário de buscas.
4. **Coleta**: Extração técnica do dado bruto original (código-fonte, arquivos em formato nativo).
5. **Acondicionamento**: Empacotamento em contêiner digital com cálculo de hash.
6. **Transporte**: Transferência por meio de canais criptografados ou mídias seguras.
7. **Recebimento**: Conferência formal de integridade pelo perito ou cartório judicial.
8. **Processamento**: Análise pericial e geração de relatórios.
9. **Armazenamento**: Guarda de longo prazo em repositório imutável para viabilizar contraperícia.
10. **Descarte**: Destruição documentada após o trânsito em julgado e cumprimento dos prazos da LGPD.

> [!IMPORTANT]
> **Extensão ao Processo Civil e Trabalhista**: Embora topograficamente inserida no CPP, a jurisprudência contemporânea dos Tribunais Estaduais e do STJ é pacífica ao proclamar que os parâmetros de integridade, auditabilidade e repetibilidade da cadeia de custódia aplicam-se a qualquer ramo do Direito (CPC, art. 369, 422 e 424), sob pena de a prova digital juntada unilateralmente ser declarada inidônea e desprovida de eficácia probatória.

---

## 4. O Confronto Probatório: Ata Notarial vs. Preservação Técnica Certificada

| Vetor de Comparação | Ata Notarial (CPC, Art. 384) | Plataforma de Preservação Técnica Forense | Print Screen Simples (Captura de Tela) |
| :--- | :--- | :--- | :--- |
| **Natureza Jurídica** | Instrumento público lavrado por Tabelião de Notas dotado de fé pública (*juris tantum*). | Documento eletrônico certificado com hash SHA-256 e carimbo ICP-Brasil/Blockchain. | Reprodução mecânica simples (CPC, art. 422). |
| **Capacidade Pericial Técnica** | Baixa. O tabelião atesta apenas o que vê na tela; raramente audita tráfego de rede, código-fonte ou IPs. | **Altíssima**. Preserva cabeçalhos HTTP, rotas WHOIS, endereços IP de resposta e código-fonte bruto. | Nula. Não registra metadados nem código subjacente. |
| **Custo Financeiro** | Elevado (emolumentos estaduais cobrados por página/hora). | Baixo a moderado (cobrança por relatório pericial emitido). | Gratuito. |
| **Velocidade em Casos Críticos** | Lenta (depende de agendamento e deslocamento ao cartório). | **Instantânea** (captura em tempo real de conteúdos voláteis como Stories). | Instantânea, porém juridicamente frágil. |
| **Vulnerabilidade em Juízo** | Dificilmente impugnada quanto à data, mas vulnerável à alegação de "página clonada ou falsa". | Inatacável pericialmente se submetida à contraperícia e preservada a mesmidade. | **Imprestável** se impugnada especificamente pela parte adversa. |

---

## 5. Jurisprudência Consolidada do STJ e o Movimento Regulatório do CNJ

### 5.1. A Invalidade dos Prints de WhatsApp Desprovidos de Integridade
O STJ pacificou o entendimento de que capturas de tela do WhatsApp Web, desacompanhadas da extração forense da base de dados do aparelho ou de ata notarial que comprove a continuidade e integralidade das mensagens, não constituem meio de prova idôneo para condenação penal ou medidas cíveis gravosas:
> *"As mensagens enviadas por meio do aplicativo WhatsApp Web admitem a possibilidade de exclusão unilateral de mensagens, bem como de adulteração do teor das conversas sem deixar vestígios visíveis na tela. Imprescindível a realização de exame pericial idôneo ou observância estrita da cadeia de custódia para conferir credibilidade ao material."* (STJ, 5ª Turma, AgRg no RHC 143.169/RJ; 6ª Turma, RHC 99.735/SC).

### 5.2. O Princípio *Pas de Nullité Sans Grief* (Art. 563 do CPP)
Ao analisar vícios formais na cadeia de custódia, o STJ fixou que a suposta quebra das formalidades do art. 158-A não acarreta nulidade automática absoluta da prova:
> *"Eventual irregularidade no cumprimento das formalidades da cadeia de custódia não conduz, de plano, à ilicitude ou inadmissibilidade da prova, competindo à parte que suscita a nulidade demonstrar o efetivo prejuízo e elementos concretos que coloquem em dúvida a idoneidade e integridade do vestígio recolhido."* (STJ, 6ª Turma, HC 703.978/SC).

### 5.3. A Portaria CNJ nº 391/2025 no Contexto da Governança Forense
A Portaria nº 391/2025 do Conselho Nacional de Justiça instaurou Grupo de Trabalho especializado destinado a padronizar as diretrizes técnicas e operacionais para a custódia, armazenamento e valoração da prova digital no Poder Judiciário. 

> [!NOTE]
> **Enquadramento Preciso**: A Portaria CNJ 391/2025 **não é uma norma pericial finalizada nem lei processual**, mas sim um ato administrativo de evolução institucional que sinaliza aos advogados que, muito em breve, a adoção de padrões formais de integridade digital será condição cogente para a admissibilidade de qualquer prova telemática nos tribunais brasileiros.

---

## 6. Boxes Didáticos do Capítulo

> [!NOTE]
> ### 📦 Preservação: Como Calcular Hash SHA-256 no Terminal
> Para comprovar a integridade de qualquer arquivo salvo (PDF, vídeo, HTML), abra o terminal do seu sistema operacional e execute:
> - **macOS / Linux**: `shasum -a 256 nome_do_arquivo.ext`
> - **Windows (PowerShell)**: `Get-FileHash nome_do_arquivo.ext -Algorithm SHA256`
> Transcreva o código de 64 caracteres resultante diretamente no corpo da petição ou relatório forense.

> [!WARNING]
> ### ⚖️ Limite Jurídico: A Presunção Relativa da Ata Notarial
> A ata notarial não transforma uma mentira em verdade. O tabelião apenas lavra: *"Em 10/09/2026 acessei a página X e vi a imagem Y"*. Se a página acessada for uma cópia falsa (*phishing* ou arquivo local aberto no navegador do cliente), a ata notarial não terá o condão de validar a autenticidade daquele fato contra o réu. A contraparte pode exigir a perícia do código-fonte e da infraestrutura do servidor.

> [!NOTE]
> ### 🧪 Verificação: O Teste da Repetibilidade
> Antes de fechar a preservação, faça o teste da repetibilidade pericial: *"Se um perito do juízo ou o assistente da parte contrária tentar reproduzir os meus passos com base no meu diário de buscas, ele chegará ao mesmo arquivo com o mesmo hash?"* Se a resposta for sim, a evidência está blindada contra alegações de quebra de cadeia de custódia.
