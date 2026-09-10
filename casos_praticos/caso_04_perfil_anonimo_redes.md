# Estudo de Caso Prático 04: Perfil Anônimo Difamatório em Redes Sociais

## 1. Cenário Fático e Mandato Investigativo

- **Cliente**: Dra. Camila Antunes, médica dermatologista e empresária em Belo Horizonte/MG.
- **Caso**: Ação Cautelar Inominada Antecedente de Exibição de Registros Digitais (art. 22 do Marco Civil da Internet) c/c Reparação de Danos Morais.
- **Alvo**: Operador desconhecido do perfil apócrifo no Instagram `@verdades_estetica_bh`.
- **Problema Jurídico**: O perfil anônimo vem publicando acusações de erro médico e uso de produtos clandestinos contra a autora, marcando pacientes e entidades médicas. O perfil não possui nome real nem foto de pessoa identificada.
- **Pergunta Investigativa**: *Quais elementos técnicos de correlação em fontes abertas permitem traçar uma hipótese fundada sobre a pessoa que opera a conta apócrifa e como estruturar a requisição judicial via Marco Civil da Internet sem risco de indeferimento?*
- **Base Legal**: Art. 5º, X, da CF/88; Arts. 19 e 22 da Lei 12.965/2014 (Marco Civil da Internet).

---

## 2. Ponto de Partida e Identificadores Iniciais (*Seeds*)

- **Handle / Username**: `@verdades_estetica_bh` (Instagram).
- **URL do Perfil**: `https://www.instagram.com/verdades_estetica_bh/`.
- **Bio**: *"Revelando as fraudes e erros médicos das clínicas de BH"*.
- **Postagens**: 14 publicações focadas exclusivamente na Dra. Camila Antunes e em sua sócia.

---

## 3. Cadeia Lógica de Pivoteamento e Atribuição OSINT

```
[Perfil Instagram: @verdades_estetica_bh]
       │
       ▼ (Simulação de Fluxo de Recuperação de Senha Oficial do Instagram)
[Número de telefone mascarado: Final **-****-**84 e E-mail: r*****a@g****.com]
       │
       ▼ (Análise de Rede de Conexões: Primeiros 10 Seguidores e Seguidos da Conta)
[Identificação de conta comum muito ativa: @renataborges_dermato]
       │
       ▼ (Consulta Pública no Conselho Regional de Medicina - CRM/MG)
[Dra. Renata Borges - Dermatologista com consultório no mesmo bairro da vítima]
       │
       ▼ (Registro do Consultório / Cartão CNPJ no REDESIM)
[Telefone comercial cadastrado no CNPJ: (31) 9****-**84 e E-mail: renataborges.estetica@gmail.com]
       │
       ▼ (Sherlock / WhatsMyName - Busca de Reutilização de Username)
[Username "verdades_estetica_bh" criado originalmente com o handle "renata_dicas_bh" em fórum de estética]
       │
       ▼ (Confronto de Estilo Linguístico / Estilometria Forense)
[Uso idêntico de expressões idiomáticas raras, espaçamento e pontuação]
```

---

## 4. Diário de Buscas e Execução Operacional

| Data/Hora | Fonte Consultada | Parâmetro / Termo de Busca | Resultado Bruto | Análise / Decisão |
| :--- | :--- | :--- | :--- | :--- |
| 2026-09-06 08:30 | Instagram Web | Tela "Esqueci minha senha" para `@verdades_estetica_bh` | Exibição de máscara oficial: *"Enviamos um SMS para o número terminado em 84 e e-mail r*****a@g****.com"*. | **Nunca prosseguir com o reset!** Apenas anotar a máscara do provedor. |
| 2026-09-06 09:15 | CRM/MG | `Renata Borges` | CRM-MG 54.321 - Médica em atividade em Belo Horizonte. | Obter nome empresarial e endereço do consultório. |
| 2026-09-06 10:00 | REDESIM / Receita Federal | CNPJ da Clínica Renata Borges | Telefone no cartão CNPJ: `(31) 98877-6684`. Bate exatamente com o final **84**. | O e-mail cadastrado na RFB tem formato compatível: `r...a@gmail.com`. |
| 2026-09-06 11:30 | Instagram (Análise de Grafos) | Extração de seguidores mútuos | O perfil anônimo foi criado em agosto e seguiu apenas 8 pessoas antes de começar os ataques, todas funcionárias da clínica da Dra. Renata. | Indício contundente de autoria ou coordenação próxima. |

---

## 5. Matriz de Evidências

| ID | Fato Investigado | Informação Encontrada | Fonte | Data | Tipo | Confiabilidade | Corroboração | Limitação | Classificação | Preservação | Utilidade Jurídica |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **EVD-007** | Difamação e concorrência desleal na internet. | Publicações imputando crimes e imperícia à médica sem qualquer condenação no CRM ou processo judicial. | Instagram (`@verdades_estetica_bh`). | 2026-09-06 08:30 BRT | Primária | Alta | Corroborado por certidão negativa disciplinar do CRM-MG. | O conteúdo pode ser apagado a qualquer momento pela operadora da conta. | Fato Verificado (Materialidade do ilícito digital). | Arquivo `instagram_verdades_estetica_bh_warc.warc` (Hash SHA-256: `6c0f36aa5fd096c937d091d68c9ba2933ca6dfa2811277d84ee84a153ad69d71`). | Provar a materialidade do ato ilícito e justificar a remoção urgente (CPC, art. 300). |
| **EVD-008** | Correlação de identidade do operador da conta apócrifa. | Máscara de telefone (final 84) e e-mail compatíveis com o cadastro oficial da médica concorrente, somado ao padrão de seguidores. | Instagram e Receita Federal. | 2026-09-06 10:00 BRT | Secundária / Técnica | Média-Alta | Corroborado pelo vínculo geográfico e concorrência direta no mesmo nicho de atuação. | **A correlação OSINT não é prova conclusiva de autoria material.** | Indício Forte / Hipótese Fundamentada. | Arquivo `relatorio_atribuicao_mascara_rfb.pdf` (Hash SHA-256: `736f8e375af04c2e580544a252ce7ac411fb80efe155f9ea5616d205154a5c57`). | Demonstrar fumus boni iuris para requisição de dados cadastrais e IPs via art. 22 do MCI. |

---

## 6. Boxes de Aprendizagem Aplicados

> [!CAUTION]
> ### ⚠️ Não Conclua Ainda: A Tríade da Atribuição Digital
> Mesmo com a máscara de telefone (final 84) e e-mail idênticos aos da concorrente, **o advogado jamais deve ajuizar ação indenizatória direta afirmando peremptoriamente que a Dra. Renata é a autora das ofensas**. O número pode pertencer a secretária, terceiro que adquiriu chip reciclado, ou ter sido cadastrado de má-fé por outrem. A cautela deontológica exige ajuizar ação judicial com o rito do Marco Civil da Internet para validação pericial dos registros do provedor.

> [!IMPORTANT]
> ### 🏛️ Medida Judicial: O Rito Obrigatório do Art. 22 do Marco Civil
> Para alcançar a certeza jurídica da autoria, o caminho legal inafastável é:
> 1. Ajuizar pedido judicial fundamentado indicando as URLs específicas dos ilícitos (art. 19, § 1º, MCI).
> 2. Obter ordem determinando que a Meta Plataformas forneça os **registros de conexão e de acesso à aplicação** (endereço IP, porta lógica, data, hora e fuso UTC de login e criação da conta).
> 3. Expedir ofício à operadora de telecomunicações titular do IP para revelar o nome e endereço do assinante da conexão no exato segundo do fato.

---

## 7. Desfecho Jurídico e Aplicação Prática

A Dra. Camila ingressou com Procedimento Comum de Exibição de Dados contra o Instagram (Meta Plataformas do Brasil Ltda.), instruindo a petição inicial com a Ata Notarial e o Relatório OSINT com a hipótese de atribuição.

O juiz da 10ª Vara Cível de Belo Horizonte:
1. Deferiu a **tutela provisória de urgência** determinando a indisponibilização do perfil difamatório em 24 horas sob pena de multa diária (art. 19 do MCI);
2. Determinou o fornecimento dos registros de aplicação (IPs e portas lógicas);
3. De posse dos IPs fornecidos pela Meta, expediu ofício à concessionária de telefonia Claro S/A, que confirmou formalmente que a conexão pertencia ao plano de internet residencial da Dra. Renata Borges.

Somente após essa confirmação oficial da operadora de telecomunicações foi instaurada a Queixa-Crime por Difamação e Calúnia (CP, arts. 138 e 139) e a Ação de Reparação de Danos Morais e Materiais por Concorrência Desleal.
