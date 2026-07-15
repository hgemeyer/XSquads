# Registro de Avanços — Sistema de Crescimento Instagram Klin

> Log oficial do projeto. Toda sessão de trabalho deve atualizar este arquivo e fazer push (ver skill `klin-growth` e Routine de push automático).

## Estado atual (15/jul/2026)

**Fase:** Sistema completo + estudo 360º + de-para FINAL + **medição de aderência (34%)** prontos para discussão com o time.
**Branch de trabalho:** `claude/instagram-growth-ai-system-0tbqk7` (ainda não mesclado ao `main` — abrir PR quando o time aprovar).
**Artifact visual (de-para):** https://claude.ai/code/artifact/dec7f5e9-fb08-45ba-b7fe-c215bed1583e

## Linha do tempo

### 15/jul/2026 — Sessão 1 (fundação completa)

1. **Sistema de conteúdo (módulos 1-10)** — pesquisa com dados reais da conta via API (Composio), 20 oportunidades, 50 ganchos, 30 guiões de Reels, 20 carrosséis, 30 Stories, sistema visual com 21 prompts de IA, sistema de legendas, calendário 30 dias, matriz de reutilização 7 plataformas.
2. **Estudo 360º (módulo 11)** — 228 posts analisados (14/jan-14/jul): Reels +69% likes vs cards; pico abr (103 likes médios) e queda jun-jul (62); virais = concurso UGC (487), inclusão T21 (464+270), mascote (422), emocional Dia das Mães (416).
3. **Concorrência (módulos 12-13)** — Bibi/Pampili/Kidy + VEJA/Adidas/Tip Toey Joey, ~50 fontes. Gaps confirmados: TikTok vazio no segmento; ninguém fala "mãe para mãe".
4. **Planilha GTM lida** (Google Drive via Composio, abas Jul/Ago/Set) e **de-para dia a dia criado (módulo 14)** — 87% do trimestre ajustável.
5. **Radar de Tendências consumido (módulo 15)** — edições 10 e 13/07 (via Gmail/Composio; skill roda como Routine a cada 3 dias). Radar confirmou 6 teses e adicionou 4: camada racional de preço, selo IBTeC como hero, paleta verão 26/27, bico largo/TikTok.
6. **De-para v2 FINAL (módulo 14 atualizado)** — integra radar: #CresciDeKlin (17/07), IBTeC em 3 peças de julho, nano/micro criadoras, charms como feature filmável do Dia das Crianças.
7. **Skill `klin-growth` criado** em `.claude/skills/klin-growth/` + Routine de push automático configurada.

### 15/jul/2026 — Sessão 2 (medição de aderência)

8. **Módulo 16 criado — [16-aderencia.md](16-aderencia.md)**, a pedido do Allan: cruzar *o que precisamos fazer* × *o que já fazemos*. 12 eixos do módulo 14 medidos contra os **229 posts** reais (14/jan–15/jul, API via Composio). **Aderência global: 34%** — 1 verde, 4 amarelos, 7 vermelhos.
9. **Piores eixos:** preço ancorado em valor, nano/micro criadoras e TikTok (0%); gancho na 1ª linha (13%); tecnologia nomeada (14% — **IBTeC e SAV nunca citados no feed em 6 meses**); mascote (27% — 176 likes médios e **zero em julho**); inclusão (29% — 254 likes médios, feito só 2×).
10. **Correlação aderência × likes: r = 0,74** (7 meses). Abril = mês mais aderente (67%) e melhor (103,2 likes); julho = menos aderente do trimestre e pior do semestre (59,8). Rotulado como relação forte, **não causa** (abril teve Dia das Mães).
11. **Armadilha registrada:** classificador de mascote inflava para 100% por contar o emoji 🐾 (assinatura de marca, 25 posts). Critério estrito → 7 posts, 27%. Validar classificador por amostra antes de reportar.
12. **Artifact atualizado na MESMA URL** (dec7f5e9…): nova seção 1 "Aderência: o que pedimos × o que já fazemos" (medidor global, placar dos 12 eixos, série mensal aderência × likes); seções antigas renumeradas 2–7; base corrigida de 228 → 229 posts; nota de metodologia no rodapé.

### 15/jul/2026 — Sessão 3 (calendário de agosto)

13. **Módulo 17 criado — [17-calendario-agosto.md](17-calendario-agosto.md)** + artifact visual em formato de calendário: https://claude.ai/code/artifact/1f4d52f4-1e02-4a9d-aafe-810bbd033b99
14. **Descoberta na aba Ago:** a planilha define **tema e tipo, não formato** — só 3 dos 31 dias citam formato inline (09 "CARD", 23 e 29 "Vitrine"). Ou seja, **não há divergência de formato entre GTM e recomendação: há lacuna.** O formato é decidido na produção sem critério registrado, e é o eixo onde a conta mais perde. **Proposta ao time: criar coluna Formato na planilha.**
15. **Proposta dos 31 dias:** 31/31 temas mantidos (2 lacunas "a definir" preenchidas com guião pronto — 01 e 27/08). Mix: 19 reels (61%) · 11 carrosséis (35%) · 1 card (3%). Tipo: Produto 12 (39%) · Educação 8 (26%) · UGC 6 (19%) · Emocional 5 (16%).
16. **Cobertura dos eixos vermelhos do módulo 16 em agosto:** mascote 7× (≥1/semana), tecnologia nomeada 3× (03/15/21), inclusão 1× (06), preço ancorado 3× (01/05/14 — Liquidação até 05/08), hero 9 de 9 em sex/sáb, criadoras nano/micro 6×, TikTok estreia 15/08.
17. **Decisão de calendário registrada:** hero do Dia dos Pais no **sábado 08** (96 likes médios) e não no domingo 09 (69) — domingo fica com o card comemorativo (único card do mês) + Stories UGC.

## Decisões em aberto (aguardando o time)

- [ ] Aprovar o de-para FINAL (reunião com Righi/mkt) — deadline crítico: **17/07** (#CresciDeKlin)
- [ ] Validar placeholders de depoimentos/dados internos nos Stories (módulo 6)
- [ ] Revisão técnica dos conteúdos de saúde (Dra. Be / pediatra)
- [ ] Levar às áreas: paleta PV27 (mkt), kit charms/pins (produto), recrutamento nano/micro (influência)
- [ ] **Antes de 1º/08 (módulo 17):** recrutar 8-10 criadoras-mãe (trava os dias 11/13/18/20/24/30 e a série de setembro) · agendar Dra. Be + laboratório para 15/08 · fechar paleta verão 26/27 antes do teaser de 05/08
- [ ] Propor coluna **Formato** na planilha GTM (hoje a aba Ago só define tema e tipo)
- [ ] Abrir PR para `main` quando aprovado
- [ ] Automação de publicação (Nível 3): Routine diária de post via API + hospedagem de assets em URL pública

## Métricas-alvo do trimestre

| Métrica | Base (jul) | Meta (30/set) |
|---|---|---|
| Likes médios/post | 62 | ≥100 |
| Comentários médios/post | 2,6 | ≥7 |
| Likes médios/Reel | 80 | ≥140 |
| Fonte de medição | API Instagram via Composio (mesmos endpoints do módulo 11) | idem |

## Como continuar o trabalho (qualquer sessão nova)

1. `git checkout claude/instagram-growth-ai-system-0tbqk7 && git pull`
2. Ler este arquivo + [README.md](README.md) (índice dos 15 módulos)
3. Usar o skill **`klin-growth`** (carrega automaticamente neste repo) para os fluxos operacionais
4. Ao final de QUALQUER avanço: atualizar este arquivo, commit convencional e push no branch
