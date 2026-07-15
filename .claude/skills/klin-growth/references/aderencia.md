# Aderência — o placar que ancora a conversa

**Pergunta que ele responde:** de tudo que a análise manda fazer, **quanto a conta já faz?**
Medido post a post, não por percepção.

**Resultado em 15/07/2026: 34%** — 1 eixo verde, 4 amarelos, 7 vermelhos.

Motor: `scripts/medir_aderencia.py` (roda no Composio REMOTE_WORKBENCH).

---

## Os 12 eixos

| Eixo | Meta | Peso | Jul/26 | Nota |
|---|---|---|---|---|
| Tecnologia nomeada (IBTeC/SAV/Palmilha) | série mensal | 3 | 2 posts em 6 meses, só abril | **14%** |
| Mascote | 1×/semana | 3 | 7 posts/26 sem · zero em julho | **27%** |
| Gancho na 1ª linha | 100% | 2 | 12,7% | **13%** |
| Inclusão | 1 pauta/mês | 2 | 2 de 7 meses | **29%** |
| Preço ancorado em valor | sempre | 2 | 1 post de preço no feed, 0 ancorado | **0%** |
| Influência nano/micro | elenco de 8-10 mães | 2 | 2 posts com @menção | **0%** |
| TikTok | repost + estreia | 1 | zero presença | **0%** |
| Cards no mix | ≤15% | 3 | 33,2% (jul 40%) | **45%** |
| Hero em sex/sáb | 100% | 2 | 9 dos top 20 | **45%** |
| Reels no mix | ≥50% | 3 | 32,8% (jul 40%) | **66%** |
| Produto fora do card-vitrine | zero vitrine | 3 | 31 dos 91 posts de produto em card | **66%** |
| Carrossel no mix | ~35% | 1 | 34,1% | **100%** |

**Peso:** 3 = move engajamento diretamente · 2 = relevante · 1 = marginal.

## Fórmula

- "quanto mais melhor": `nota = min(100, 100 × atual/meta)`
- "quanto menos melhor" (teto, ex.: cards ≤15%): `nota = min(100, 100 × meta/atual)`
- Global: média das notas **ponderada pelo peso**.

Cores: 🟢 ≥70 · 🟡 40-69 · 🔴 <40.

## Classificadores (validados)

```python
MASC_STRICT = [r"\bmascote\b", r"aventuras (com|do) klin", r"aventura com o klin",
               r"\bklinzinho\b", r"\bcachorr", r"\bdoguinho\b", r"\bpeludo\b"]
# NUNCA incluir 🐾 — e assinatura de marca em 25 posts, nao aparicao do mascote
DIF   = [r"\bibtec\b", r"\bsav\b", r"palmilha ultra", r"palmilha"]
INC   = [r"inclus", r"sindrome de down", r"\bt21\b", r"autis", r"\btea\b",
         r"deficien", r"fisioterap", r"terapeut"]
PRECO = [r"desconto", r"liquida", r"\boff\b", r"\bpromo", r"\bsale\b", r"\bpreco\b", r"\bparcel"]
VALOR = [r"durab", r"dura a estacao", r"custo por uso", r"dura mais", r"resist",
         r"qualidade", r"43 anos"]
PROD  = [r"\bcapri\b", r"\bhug\b", r"\bsky\b", r"\bweekend\b", r"\bwalk\b", r"\bflash\b",
         r"\bmatilda\b", r"\bmodelo", r"\btenis\b", r"sandalia", r"\bsapato", r"chinelo",
         r"\bbota\b", r"\bcalcado", r"colecao", r"\bpar\b", r"\bsolado\b", r"\bvelcro\b"]
```

Normalizar a legenda sem acento (NFD + remover Mn) antes de casar.

**Formato:** `media_product_type == "REELS"` ou `media_type == "VIDEO"` → reel;
`CAROUSEL_ALBUM` → carrossel; resto → card.

**Gancho na 1ª linha:** tem "?" **ou** começa com (voce sabia|sabia que|para de|pare de|nunca|
3 |5 |7 |o erro|nao |atencao) **ou** é caixa alta curta (≤60 chars).

## Tendência mensal e correlação

Calcular a aderência mês a mês (4 eixos medíveis: reels, cards, mascote, tecnologia) e cruzar
com likes médios. Em jan-jul/26: **r = 0,74** (n=7). Abril = mais aderente (67%) e melhor
(103,2 likes). Julho = 30% e 59,8.

⚠️ **Rotular sempre no artifact: "relação forte, NÃO prova de causa"** — n pequeno e abril teve
Dia das Mães.

## Ordem de ataque (esforço × retorno)

1. **Gancho na 1ª linha** — 13%, custo zero, não muda pauta nem produção. Biblioteca de 50 pronta.
2. **Nomear IBTeC/SAV/Palmilha** — 14%, o ativo já existe, é só dizer o nome.
3. **Mascote semanal** — 27%, fórmula provada (422), ativo parado.
4. **Matar o card-vitrine** — mesmo produto em reel faz 128 likes; em card, 73.
5. **Recrutar nano/micro mães** — 0% e é o de **maior prazo**: sem decisão em julho, a série de
   setembro fica sem elenco.

## Quando reexecutar

**Mensal**, junto da atualização do módulo 11. A meta é ver a aderência subir de 34% e testar
se os likes acompanham. **Se agosto executar o plano e os likes não subirem, a tese está
errada e deve ser revista** — é esse o teste.
