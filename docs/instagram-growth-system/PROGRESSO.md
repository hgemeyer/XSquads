# Registro de Avanços — Sistema de Crescimento Instagram Klin

> Log oficial do projeto. Toda sessão de trabalho deve atualizar este arquivo e fazer push (ver skill `klin-growth` e Routine de push automático).

## Estado atual (15/jul/2026)

**Fase:** Sistema completo + estudo 360º + de-para FINAL prontos para discussão com o time.
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

## Decisões em aberto (aguardando o time)

- [ ] Aprovar o de-para FINAL (reunião com Righi/mkt) — deadline crítico: **17/07** (#CresciDeKlin)
- [ ] Validar placeholders de depoimentos/dados internos nos Stories (módulo 6)
- [ ] Revisão técnica dos conteúdos de saúde (Dra. Be / pediatra)
- [ ] Levar às áreas: paleta PV27 (mkt), kit charms/pins (produto), recrutamento nano/micro (influência)
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
