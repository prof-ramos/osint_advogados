# Capítulo 01: Investigação OSINT no Cenário Jurídico Brasileiro: Limites, Ética e Distinções Conceituais

## 1. A Virada Probatória Digital na Advocacia

A prática da advocacia contenciosa, consultiva e criminal no Brasil atravessa uma transformação definitiva. O modelo tradicional de instrução processual — estritamente dependente de ofícios judiciais lentos e depoimentos testemunhais falíveis — já não responde à velocidade com que relações contratuais se dissolvem, patrimônios são transferidos e ilícitos são consumados no ambiente digital.

Nesse contexto emerge a **OSINT Jurídica** (*Open Source Intelligence aplicada ao Direito*), compreendida como a atividade metodológica de **coleta, tratamento, triangulação, análise e preservação de dados obtidos em fontes abertas e públicas, com a estrita finalidade de produzir conhecimento lícito e elementos de convicção aptos a instruir procedimentos judiciais, administrativos ou negociais**.

Longe de ser uma atividade clandestina ou mero sinônimo de "hackerismo", o OSINT jurídico é o aperfeiçoamento contemporâneo da secular **prova indiciária e documental**, respaldado pelo princípio da ampla liberdade probatória (art. 369 do CPC e art. 155 do CPP).

---

## 2. Demarcações Epistemológicas e Conceituais

Para que a atuação do operador do Direito seja legítima e defensável, é indispensável estabelecer a linha divisória entre OSINT e outras disciplinas afins:

| Atividade | Objeto e Metodologia | Natureza Jurídica | Risco de Ilicitude |
| :--- | :--- | :--- | :--- |
| **OSINT Jurídico** | Coleta metódica em fontes públicas, registros estatais e repositórios acessíveis sem quebra de segurança. | Atividade probatória lícita (art. 369 CPC; Prov. 188/2018 CFOAB). | Baixo, se respeitada a LGPD e limites de invasão. |
| **Investigação Defensiva** | Procedimento conduzido pelo advogado no interesse do cliente (pesquisa aberta + entrevistas + perícias privadas). | Prerrogativa da advocacia (Provimento 188/2018 do CFOAB). | Nulo, quando formalizado em procedimento próprio. |
| **Perícia Forense Computacional** | Exame técnico direto sobre dispositivos apreendidos (hardware, discos rígidos, memória volátil) mediante cadeia de custódia. | Meio de prova pericial formal (arts. 464 CPC e 159 CPP). | Depende de consentimento do titular ou ordem judicial. |
| **E-Discovery** | Busca e triagem em bases privadas de documentos eletrônicos internos de uma das partes em litígio. | Procedimento de produção antecipada de prova ou compliance. | Requer legitimidade contratual ou judicial. |
| **Intrusão / Hacking Ilegal** | Acesso não autorizado mediante exploração de falhas, contorno de autenticação ou quebra de senhas. | **Crime tipificado** (art. 154-A do Código Penal). | **Prova ilícita absoluta (art. 5º, LVI, CF)**. |

---

## 3. O Que É e o Que Não É OSINT Jurídico

### O Que É:
- Consultar certidões em Juntas Comerciais, cartórios de registro de imóveis e portais de transparência.
- Aplicar operadores avançados de pesquisa (*dorking*) para indexar publicações oficiais e diários de justiça.
- Mapear a presença digital aberta de um devedor para identificar sinais exteriores de riqueza.
- Analisar códigos-fonte HTML públicos e metadados de arquivos distribuídos voluntariamente na internet.

### O Que Não É (Condutas Ilícitas):
- Utilizar credenciais obtidas em vazamentos de senhas para ingressar no e-mail ou rede social de terceiros.
- Criar perfis falsos com engenharia social agressiva para induzir o investigado a erro ou extrair confissões (falsidade ideológica e ilícito ético).
- Contratar os denominados "painéis puxa-tudo" no Telegram para adquirir dados protegidos por sigilo fiscal/bancário (receptação de dados públicos e crime contra a administração pública).

---

## 4. Boxes Didáticos do Capítulo

> [!WARNING]
> ### ⚖️ Limite Jurídico: O Delito de Invasão de Dispositivo Informático
> O art. 154-A do Código Penal criminaliza expressamente a conduta de *"invadir dispositivo informático alheio, conectado ou não à rede de computadores, mediante violação indevida de mecanismo de segurança"*. O advogado que ultrapassa a barreira da publicidade e acessa áreas restritas protegidas por login alheio não está fazendo OSINT, mas cometendo crime com pena de até 5 anos de reclusão, tornando a prova radicalmente imprestável no processo.

> [!TIP]
> ### 🔎 Pivô: Da Qualificação em Processo Público ao Rastreamento Registral
> Ao localizar uma petição inicial ou contestação pública em outro tribunal onde o seu investigado atuou, examine a qualificação: regime de casamento, profissão, endereço residencial e nome dos advogados constituídos. Esses dados representam o ponto de partida perfeito para pesquisas nas Juntas Comerciais e no Operador Nacional do Registro de Imóveis (ONR).

> [!CAUTION]
> ### ⚠️ Não Conclua Ainda: A Homonímia no Sistema Judiciário Brasileiro
> O Brasil possui milhões de cidadãos que compartilham o mesmo prenome e sobrenome (ex.: "José da Silva", "Maria de Souza Santos", "Carlos Eduardo Rodrigues"). Jamais atribua uma condenação criminal, dívida executada ou participação societária a um investigado baseando-se unicamente no nome. A confirmação exige a tríade: **Nome + CPF/RG + Nome da Filiação ou Data de Nascimento**.
