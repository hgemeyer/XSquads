# 20 — RETOMAR AQUI (parado em 15/jul/2026, fim do dia)

> **Leia este arquivo primeiro.** O trabalho parou no meio de uma tarefa, com um estado
> inconsistente que precisa ser resolvido antes de qualquer coisa nova.

---

## O que está ERRADO agora (resolver primeiro)

**O link `1f4d52f4-1e02-4a9d-aafe-810bbd033b99` está mostrando OUTUBRO, mas o Allan o
compartilhou com o time como sendo AGOSTO.** Quem abrir hoje vê o mês errado.

Causa: eu tinha desenhado os 3 artifacts com URL fixa e republiquei outubro por cima de agosto.
**O Allan reverteu essa decisão: quer um link por mês, todos vivos.** (Ver armadilha 21.)

---

## A tarefa em aberto: 3 calendários com gancho e copy

O Allan pediu, no fim do dia 15/07:

1. **Um link por mês** — agosto, setembro e outubro, todos no ar.
2. **Gancho e copy em cada dia** do calendário (a aba SET marca "Hooks?" como pendente há meses;
   é isso que fecha).

### O que JÁ está pronto (não refazer)

- **`scripts/gen_calendarios.py`** (neste repo) — gerador com **os 92 dias já escritos**:
  agosto (31), setembro (30) e outubro (31), cada dia com dia/flags/formato/tipo/guião/
  proposta/**gancho**/**copy**/linha do GTM. É o grosso do trabalho e está feito.
- **`scripts/_base.css`** — o CSS da família (tokens claro/escuro, chips, `.hk` do gancho,
  `.cp` da copy, `.nav`, faixa dourada de sex/sáb).
- O gerador tem as funções `celula()`, `grade()` e `pagina()` prontas. **Falta só chamar.**

### O que FALTA fazer

1. Fechar o `gen_calendarios.py`: montar as chamadas de `pagina()` para os 3 meses (eyebrow, h1,
   sub, placar, teses, extras e foot de cada um) e rodar.
   - Primeiro dia da semana (Seg=0): **agosto/26 = sáb (5)** · **setembro/26 = ter (1)** ·
     **outubro/26 = qui (3)**.
   - Faixas de agosto: nenhuma. Setembro: nenhuma. Outubro: `{0: "RETA FINAL DIA DAS
     CRIANÇAS…", 14: "HALLOW KLIN…"}`.
2. Publicar **3 artifacts separados**:
   - **Agosto → republicar em `1f4d52f4-…`** (é o link que o Allan já compartilhou como agosto;
     devolve a semântica certa).
   - **Setembro → URL nova.**
   - **Outubro → URL nova.**
   - Preencher a `.nav` de cada página com as 3 URLs reais depois de publicar (a de setembro e
     outubro só existem depois do primeiro publish → publicar, pegar a URL, atualizar a `.nav`
     dos 3 e republicar).
3. **Avisar o Allan que ele precisa compartilhar os 2 links novos** (setembro e outubro) pelo
   menu da página — artifact nasce privado.
4. Atualizar o mapa de URLs em `references/dados-conta.md` e na skill.

### Depois disso (pendência anterior, ainda de pé)

**As peças de outubro** — o artifact `76c5225b-…` ainda mostra as de agosto. Prioridade:
10/10 (hero de presente + PINs), 31/10 (Halloween + mascote), 07/10 (Dra. Be), 02/10 (Flash no
escuro). Ver módulo 18 para o padrão. **Com a política nova, as peças de outubro vão para uma
URL nova**, e as de agosto ficam onde estão.

---

## Aprendizados desta sessão (já incorporados à skill)

| # | Aprendizado |
|---|---|
| 1 | **Decisão de design que apaga trabalho anterior não é minha.** Fixei as URLs para poupar o Allan de recompartilhar, e com isso apaguei a visão de agosto. Ele reverteu. Custo aceito: 2 links novos por mês. |
| 2 | **As abas de mês não têm o mesmo layout.** `Ago`: sem coluna Formato. `SET`: **com** Formato + coluna de pendências marcando **"Hooks?"**. Inspecionar as 6 primeiras linhas antes de parsear. |
| 3 | **Não existe aba de Out/Nov/Dez.** De outubro em diante, o plano sai da linha do mês na aba `Estratégia NACIONAL - GTM` (macro tema, foco/secundário/satélite, storytelling, GTM). |
| 4 | **Gancho e copy são parte do calendário**, não extra. O time grava a partir dele. |
| 5 | **Cadência confirmada:** todo dia 15, o mês corrente + 3. Rotina `trig_01AGbqkuLVH36dSYK64uykjR` (dia 15, 10h BRT). Primeira execução: **15/08 → novembro**. |
| 6 | **O Composio não aparece na lista padrão de conectores de rotina**, mas existe: `52d5ad52-1110-421f-b898-74b1f25db2f5`, `https://connect.composio.dev/mcp`. Sem ele a rotina não puxa o Instagram e falha calada. |

---

## Estado dos artifacts em 15/jul, fim do dia

| Artifact | URL | Conteúdo atual | Situação |
|---|---|---|---|
| De-Para GTM | `dec7f5e9-…` | Jul-Set + placar 34% | ✅ ok, fixo, compartilhado |
| Calendário | `1f4d52f4-…` | **Outubro** | ⚠️ compartilhado como agosto → devolver agosto |
| Peças | `76c5225b-…` | Agosto | ⚠️ ok para agosto; faltam as de outubro (URL nova) |
| Setembro | — | — | ❌ não existe |
| Outubro (definitivo) | — | — | ❌ não existe (está ocupando o link de agosto) |

## Primeiro comando de amanhã

```
git checkout claude/instagram-growth-ai-system-0tbqk7 && git pull
cat docs/instagram-growth-system/20-RETOMAR-AQUI.md
python docs/instagram-growth-system/scripts/gen_calendarios.py   # tem os 92 dias prontos
```
