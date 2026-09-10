# 0001: Separação entre E-book Perene e Base Dinâmica Complementar

## Status
Accepted

## Contexto e Decisão
Materiais sobre OSINT e tecnologia enfrentam rápida obsolescência em virtude da descontinuação de ferramentas, expiração de domínios e alterações de interfaces governamentais e de redes sociais. Decidimos separar a arquitetura da obra em dois corpos autônomos: o **E-book Perene** (`livro/`), que contém exclusivamente a dogmática jurídica, metodologia probatória, fundamentos epistemológicos e casos práticos estruturados; e a **Base Dinâmica Complementar** (`base_dinamica/` e `osint_brazuca_dataset/`), que hospeda URLs, scripts de terminal, APIs e tabelas de ferramentas sujeitas a manutenção trimestral.

## Consequências
- O livro impresso ou e-book digital não se torna obsoleto quando um script ou portal governamental sai do ar;
- A equipe editorial pode atualizar links e ferramentas continuamente no repositório sem necessidade de publicar nova edição do livro;
- A validade probatória em juízo permanece amparada na metodologia, e não na volatilidade de softwares de terceiros.
