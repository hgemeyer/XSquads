---
name: klin-growth
description: >
  Sistema de Crescimento Instagram da Klin (@klin_oficial, calçados infantis).
  Gatilho principal: o Allan diz um MÊS ("roda o growth de agosto", "monta o plano de
  setembro", "growth de out/26") e a skill entrega o PLANO COMPLETO em 3 artifacts —
  De-Para GTM, Calendário do mês dia a dia, e As peças do mês. Também use para:
  análise da conta, medição de aderência, consumo do Radar de Tendências, estudo de
  concorrência (Bibi/Pampili/Kidy), criação de conteúdo ou geração de arte final.
  Todo avanço é registrado em PROGRESSO.md, commitado e pushado no branch.
---

# Klin Growth — Sistema de Crescimento Instagram

## Cadência — todo dia 15, o mês corrente + 3

O time trabalha com **75 dias de antecedência**. Regra: **mês alvo = mês corrente + 3.**

| Roda em | Planeja |
|---|---|
| 15/jul | Outubro |
| 15/ago | Novembro |
| 15/set | Dezembro |
| 15/out | Janeiro do ano seguinte |

Automatizado: rotina de nuvem **`trig_01AGbqkuLVH36dSYK64uykjR`** — todo dia 15 às 10h (13h UTC),
Opus 4.8, repo XSquads, conectores Composio + Gmail + Drive. Avisa o Allan no Telegram ao fim.
O Allan também pode disparar na mão: **"roda o growth de \<mês\>"**.

**Cada rodada carrega o aprendizado da anterior** (bloco 3 do `fluxo-mensal.md`): a aderência
subiu ou caiu? os likes acompanharam? o time executou o que propusemos ou ignorou? o que deu
certo e o que deu errado? **Se a tese não se sustentar, dizer — não maquiar.** Uma tese
refutada com dado vale mais que um placar bonito.

## Quem faz o quê (define tudo o resto)

| Papel | Quem | O que precisa |
|---|---|---|
| **Opera** — roda a skill, mede, publica, faz push | **só o Allan** | Composio (instagram/googledrive/gmail), write no repo, esta skill |
| **Consome e operacionaliza** — grava, produz, publica no feed | **o time** | Só os **3 links**. Nada de Composio, repo ou skill |

Consequências, que valem como regra:

1. **Os 3 artifacts têm URL FIXA.** Republicar sempre nas mesmas — o time salvou o link uma
   vez e ele tem que continuar valendo todo mês. **Nunca criar URL nova.**
2. **Artifact nasce privado.** Ao publicar um artifact **novo**, avisar o Allan que ele precisa
   compartilhar pelo menu da própria página — nenhuma ferramenta faz isso por ele, e sem isso
   o time não abre. Republicação em URL já compartilhada **não** precisa de nada.
3. **Escrever para quem vai executar, não para quem vai aprovar.** O time operacionaliza a
   partir dessas telas: o que estiver ambíguo vira pergunta ou erro de produção. Gancho, texto
   na tela, B-roll, legenda e trava têm que estar na página — não na conversa.

## Regra nº 1 — a entrega são 3 telas, sempre

Quando o Allan disser um mês, a entrega **não é um texto**: são **3 artifacts HTML**, nessa
ordem, um puxando o outro por link no rodapé.

| # | Artifact | O que responde | URL — **FIXA, republicar** |
|---|---|---|---|
| 1 | **De-Para GTM Klin — <trimestre>** | O que o plano diz × o que eu faria × **quanto disso já fazemos** (placar de aderência) | `dec7f5e9-fb08-45ba-b7fe-c215bed1583e` |
| 2 | **<Mês> — Calendário Proposto** | Os 30/31 dias, cada um com formato, gancho e ângulo, contra o que está na aba do mês | `1f4d52f4-1e02-4a9d-aafe-810bbd033b99` |
| 3 | **As peças de <mês>** | Como a peça sai: frame de abertura, roteiro com timecode, texto na tela, legenda | `76c5225b-5260-4b10-95dc-c9bb6163fdf5` |

O título muda de mês ("Setembro 2026 — Calendário Proposto"); **a URL e o favicon, não**. Usar
`label` na publicação (ex.: `set-26`) — a versão anterior fica no histórico do artifact, e o mês
fechado fica registrado como módulo no repo. **A história vive no repo; o link é sempre o mês
corrente.**

Detalhes de estrutura, tokens visuais e esqueleto HTML: **`references/artifacts.md`**.

## Regra nº 2 — continuidade via repo

Tudo vive em `docs/instagram-growth-system/` no branch
`claude/instagram-growth-ai-system-0tbqk7` (repo `hgemeyer/XSquads`).

**Ao iniciar:** `git checkout claude/instagram-growth-ai-system-0tbqk7 && git pull`, depois ler
`PROGRESSO.md` (estado atual) e `README.md` (índice dos módulos).

**Ao terminar QUALQUER avanço (obrigatório):** atualizar `PROGRESSO.md` → commit
convencional → `git push origin claude/instagram-growth-ai-system-0tbqk7`. Sessões remotas
são efêmeras; o repo é a única memória durável.

## O fluxo do mês (o que fazer quando ele disser "agosto")

Detalhe passo a passo, com os comandos: **`references/fluxo-mensal.md`**. Resumo:

1. **Ler o repo** — `PROGRESSO.md` + módulos 11 (estudo), 14 (de-para), 16 (aderência).
2. **Puxar a conta** — mídia da @klin_oficial via Composio, janela dos últimos ~6 meses.
   Recalcular os baselines (não confiar nos números velhos).
3. **Medir a aderência** — `scripts/medir_aderencia.py`, os 12 eixos. É isso que transforma
   opinião em placar.
4. **Ler a aba do mês na planilha GTM** (Drive via Composio). **Atenção:** as abas definem
   **tema e tipo, não formato** — o formato é a lacuna, e é onde a conta perde.
5. **Consumir o Radar** mais recente (Gmail via Composio) + concorrência (módulos 12-13).
6. **Montar os 3 artifacts** na ordem acima.
7. **Se pedir arte:** skill `designer-klin` (ver `references/pecas.md` §Arte final).
8. **Registrar:** módulo novo em `docs/instagram-growth-system/` + PROGRESSO + push.

## Fontes de dados (via Composio MCP)

| Dado | Como acessar |
|---|---|
| Métricas da conta | `INSTAGRAM_GET_IG_USER_MEDIA` (`ig_user_id:"me"`, conta klin_oficial). Campos: `id,caption,permalink,timestamp,media_type,media_product_type,like_count,comments_count`. Paginar com `paging.cursors.after` — itens em `response.data.data`, paging em `response.data.paging` |
| Planilha GTM | Drive `16o3nAkTqRBZcCbM4uJsSzbRvtNwt7IuNEGFuGWPGZPk` ("GTM Klin") via `GOOGLEDRIVE_DOWNLOAD_FILE` — **o campo é `fileId`, não `file_id`**. Baixar o `s3url` e parsear com openpyxl. Abas: Jun/Jul/Ago/SET + Datas Importantes + Estratégia de Brindes |
| Radar de Tendências | `GMAIL_FETCH_EMAILS` com `subject:"Radar de Tendências KLIN"` — roda como Routine a cada 3 dias; pegar sempre a edição mais recente |

## Fatos-chave da conta

Baseline vivo em **`references/dados-conta.md`** (revalidar todo mês com dados novos).
O essencial:

- 472,5k seguidores · **79,1 likes médios/post** (229 posts, 14/jan–15/jul/26)
- **Reel 106 likes / 10 comentários · Carrossel 70 / 2,9 · Card 62 / 4,4** — reel bate card em +70% likes e +127% comentários
- **Sex 101 · Sáb 96** vs qua 66 / dom 69 → todo hero em sexta ou sábado
- Fórmulas virais provadas: concurso UGC (487), **inclusão real c/ especialista (464+270 — 254 likes médios, o maior recorte da conta)**, **mascote (422; 176 likes médios vs 79 da conta)**, emocional 3 gerações (416), série animada (161-222)
- Card-vitrine é o pior conteúdo; produto sempre em rotina/ocasião de uso (produto em reel: 128 likes; em card: 73)
- Diferenciais a martelar: **IBTeC, SAV, Palmilha Ultra** — resposta ao FisioFlex da Bibi
- Territórios vagos: **TikTok** e **"mãe para mãe"**; não disputar o Dia da Menina (23/09, Pampili)
- Tom: mãe para mãe, 💛🐾, nunca institucional; saúde sempre com "converse com o pediatra"; conteúdo IA marcado "*Conteúdo gerado por IA"

## Aderência — o placar que ancora tudo

**34% em 15/07/2026** (12 eixos, média ponderada por impacto). É o número que transforma a
conversa de opinião em fato. Eixos, metas, fórmula e como reexecutar:
**`references/aderencia.md`** + `scripts/medir_aderencia.py`.

Os 7 eixos vermelhos em jul/26: preço ancorado em valor (0%), nano/micro criadoras (0%),
TikTok (0%), gancho na 1ª linha (13%), **tecnologia nomeada (14% — IBTeC e SAV nunca
citados em 6 meses)**, mascote (27% — zero em julho), inclusão (29%).

**Correlação aderência × likes: r = 0,74** (7 meses). Abril foi o mês mais aderente (67%) e o
melhor (103 likes); julho, o menos aderente do trimestre e o pior (60). **Rotular sempre como
relação forte, NÃO como prova de causa** — n=7 e abril teve Dia das Mães.

## Peças

Anatomia de reel/carrossel/card, régua de qualidade, travas de produção e o caminho da arte
final: **`references/pecas.md`**.

O sistema já tem guião pronto para boa parte do mês — **usar antes de inventar**: módulo 03
(50 ganchos), 04 (30 reels R01-R30), 05 (20 carrosséis C01-C20), 07 (visual + prompts IA),
08 (legendas).

## Armadilhas — leia antes de reportar qualquer número

**`references/armadilhas.md`** — erros que já custaram retrabalho aqui e não podem se repetir
(o emoji 🐾 inflando o mascote para 100%, guião citado em dois dias, emoji virando tofu na
Gotham, CTA colidindo com subtítulo, `file_id` vs `fileId`, entre outros).

A regra-mãe: **validar todo classificador por amostra antes de reportar**. Um número errado
num artifact que vai pro time custa mais que meia hora conferindo.
