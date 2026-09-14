---
marp: true
theme: default
paginate: true
size: 16:9
header: "OSINT Aplicado ao Direito Brasileiro • Prof. Gabriel Ramos"
footer: "Curso Executivo de Inteligência Investigativa e Prova Digital"
style: |
  section {
    font-family: 'Segoe UI', -apple-system, BlinkMacSystemFont, Roboto, sans-serif;
    background-color: #f8fafc;
    color: #1e293b;
    padding: 40px;
  }
  h1 {
    color: #1e3a8a;
    font-size: 2.2em;
    border-bottom: 3px solid #1e3a8a;
    padding-bottom: 10px;
  }
  h2 {
    color: #0369a1;
    font-size: 1.5em;
  }
  .highlight-box {
    background-color: #eff6ff;
    border-left: 6px solid #3b82f6;
    padding: 15px 20px;
    border-radius: 4px;
    margin: 20px 0;
  }
  .warning-box {
    background-color: #fffbeb;
    border-left: 6px solid #f59e0b;
    padding: 15px 20px;
    border-radius: 4px;
    margin: 20px 0;
  }
  .two-columns {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 30px;
  }
---

<!-- _class: lead -->
# OSINT Aplicado ao Direito Brasileiro
## Módulo 1.4: Prova Digital, Cadeia de Custódia e Jurisprudência do STJ

**Prof. Gabriel Ramos**  
*Cadeia de Custódia • Mesmidade • Hashes Criptográficos • Casos Reais*

---

# A Ilusão da Tela: Por Que Prints Não Bastam?

<div class="two-columns">
<div>

### A Realidade da Prova Digital:
- **Intangibilidade**: Bits em bancos de dados, não na moldura do aparelho.
- **Volatilidade Extrema**: Qualquer clique altera metadados `mtime` e `atime`.
- **Facilidade de Forjamento**: Inspecionar elemento no navegador e apps de conversa falsa.

</div>
<div>

<div class="warning-box">
  <strong>⚠️ Informativo 811 do STJ:</strong><br>
  A captura de tela estática (print screen) desacompanhada de código hash e registro de extração forense é <em>juridicamente imprestável</em>.
</div>

</div>
</div>

---

# Os Três Pilares da Mesmidade Pericial

1. **Rastreabilidade Documentada**:
   Registro cronológico da posse do vestígio desde a coleta até a apresentação em juízo (CPP, art. 158-A).
2. **Imutabilidade Matemática (Hashing SHA-256)**:
   A garantia algorítmica de que nem um único bit foi corrompido ou adulterado.
3. **Auditabilidade por Terceiros**:
   O perito do juízo ou o assistente técnico da parte adversa deve conseguir reproduzir o mesmo resultado.

<div class="highlight-box">
  <strong>Equação Central:</strong><br>
  Arquivo Coletado + Hash SHA-256 no Momento da Captura = Prova Blindada contra Impugnações.
</div>

---

# Laboratório Prático: Como Calcular o Hash no Terminal

Para auditar um arquivo no terminal do macOS ou Linux:

```bash
shasum -a 256 evidencia_contrato.pdf
```

Exemplo de Saída Esperada (64 caracteres hexadecimais):
```text
d54d9b23b49c7be7708579d4fdc7bc5ef44c3c3a4f6cf70e340c4974fa2e1c93  evidencia_contrato.pdf
```

- Transcreva o hash resultante **diretamente no corpo da petição inicial ou contestação**.
- Acoste o arquivo original em mídia física ou repositório em nuvem autenticado.

---

<!-- _class: lead -->
# Próxima Aula: O Ciclo Investigativo em 10 Etapas
## Obrigado! Dúvidas e debates no fórum da disciplina.
