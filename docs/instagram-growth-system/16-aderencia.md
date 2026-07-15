# 16 — Medição de Aderência (recomendado × praticado)

**Data:** 15/jul/2026 · **Base:** 229 posts da @klin_oficial (14/jan–15/jul/2026), API Instagram via Composio
**Vive em:** seção 1 do artifact do de-para → https://claude.ai/code/artifact/dec7f5e9-fb08-45ba-b7fe-c215bed1583e

## Pergunta

O módulo 14 diz **o que fazer**. Este módulo responde **quanto disso já é feito** — medido post a post, não por percepção.

## Resultado

**Aderência global: 34%** (média dos 12 eixos ponderada por impacto). 1 eixo verde, 4 amarelos, 7 vermelhos.

| Eixo | Meta | Praticado (jan–jul) | Aderência |
|---|---|---|---|
| Tecnologia nomeada (IBTeC/SAV/Palmilha) | série mensal | 2 posts em 6 meses, só abril; **zero** IBTeC/SAV | **14%** |
| Mascote 1×/semana | 26 posts | 7 posts (0,27/sem); **zero em julho** | **27%** |
| Gancho na 1ª linha | 100% | 12,7% | **13%** |
| Inclusão 1 pauta/mês | 7 meses | 2 meses (3 posts) | **29%** |
| Preço ancorado em valor | sempre | 1 post de preço no feed, 0 ancorado | **0%** |
| Influência nano/micro (8–10 mães) | elenco montado | 2 posts com @menção | **0%** |
| TikTok ativo | repost + estreia | zero presença | **0%** |
| Cards ≤15% do mix | ≤15% | 33,2% (jul 40% — piorando) | **45%** |
| Hero em sex/sáb | 100% | 9 dos top 20 | **45%** |
| Reels ≥50% do mix | ≥50% | 32,8% (jul 40%) | **66%** |
| Produto fora do card-vitrine | zero vitrine | 31 dos 91 posts de produto em card | **66%** |
| Carrossel ~35% | ~35% | 34,1% | **100%** |

## Metodologia (reproduzível)

1. Paginar `INSTAGRAM_GET_IG_USER_MEDIA` (`ig_user_id:"me"`, campos `timestamp,media_type,media_product_type,like_count,comments_count,caption`) até esgotar `paging.cursors.after`.
2. Recortar a janela 14/jan–15/jul/2026 → 229 posts.
3. Formato: `media_product_type=REELS` ou `media_type=VIDEO` → reel; `CAROUSEL_ALBUM` → carrossel; resto → card.
4. Tema por palavra-chave na legenda (normalizada sem acento).
5. Nota por eixo = realizado ÷ meta, limitada a 100% (invertida quando a meta é um teto, ex.: cards ≤15%). Média ponderada por peso de impacto (3 = move engajamento diretamente, 1 = marginal).

### Armadilha registrada (não repetir)

A primeira medição deu **mascote = 100%** porque o padrão incluía o emoji **🐾** — que é assinatura de marca em 25 posts, não aparição do mascote. Com critério estrito (`mascote`, `aventuras com klin`, `cachorro`…): **7 posts**, e a nota cai de 100% para 27%. **Sempre validar classificador por amostra antes de reportar.**

## Achados que mudam a conversa

- **O ativo mais rentável está parado.** Mascote = 176 likes médios vs 79 da conta. Zero em julho.
- **A tecnologia é um ativo mudo.** IBTeC e SAV nunca foram citados no feed em 6 meses. O único post da Palmilha Ultra (07/04) fez 144 likes — quase 2× a média. A Bibi martela o FisioFlex com estudo da PUC-RS.
- **Inclusão: 254 likes médios**, o maior de qualquer recorte da conta. Feito 2 vezes, funcionou as 2, parou.
- **A Liquidação não existe no feed** (peso 0,4 no plano de julho, 1 post menciona preço). Decidir se ela sai dos Stories antes de discutir como comunicá-la.
- **Julho é o pior mês do semestre** (59,8 likes médios vs 103,2 de abril) e o mês com mais card (40%).
- **Correlação aderência × engajamento: r = 0,74** (7 meses). Abril foi o mês mais aderente (67%) **e** o melhor (103,2). Relação forte, **não prova de causa** — abril também teve Dia das Mães. Amostra pequena; revalidar a cada mês.

## Ordem de ataque sugerida (esforço × retorno)

1. **Gancho na 1ª linha** — 13% de aderência, custo zero, não muda pauta nem produção. Biblioteca pronta (módulo 03).
2. **Nomear IBTeC/SAV/Palmilha** — 14%, ativo já existe, é só dizer o nome.
3. **Mascote semanal** — 27%, fórmula provada (422), ativo parado.
4. **Matar o card-vitrine** — mesmo produto em reel faz 128 vs 73 likes.
5. **Recrutar nano/micro mães** — 0% e é o de maior prazo: sem decisão em julho, a série de setembro não tem elenco.

## Como reexecutar

Rodar o fluxo "Atualizar estudo de performance" do skill `klin-growth` e recalcular a tabela acima. Sugerido: **mensal**, junto da atualização do módulo 11. A meta é ver a aderência subir de 34% e testar se os likes acompanham.
