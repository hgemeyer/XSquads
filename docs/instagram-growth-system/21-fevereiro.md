# Fevereiro/2027 — retomada do ciclo, primeira comparação real de aderência

> Rodado em 15/11/2026, com 75 dias de antecedência (mês corrente nov/26 + 3 = fev/27).
> Artifacts: [De-Para GTM + aderência](https://claude.ai/code/artifact/dec7f5e9-fb08-45ba-b7fe-c215bed1583e) ·
> [Calendário Proposto](https://claude.ai/code/artifact/1f4d52f4-1e02-4a9d-aafe-810bbd033b99) ·
> [As peças de Fevereiro](https://claude.ai/code/artifact/76c5225b-5260-4b10-95dc-c9bb6163fdf5)

## Achado nº 1 — o pipeline ficou 3 meses parado, em silêncio

`PROGRESSO.md` só tinha entradas de 15/jul/2026. Nenhuma das rodadas automáticas de 15/ago, 15/set
ou 15/out deixou rastro no repositório. O calendário de outubro (módulo 19) foi publicado por cima
do artifact que mostrava agosto sem avisar o rótulo (o link ficou mostrando outubro, mas o time
recebeu como agosto); setembro nunca foi publicado; as peças nunca saíram de agosto.

**Hipótese técnica, confirmada nesta sessão:** a sessão de nuvem que executa esta rotina não vem
com o repositório `hgemeyer/XSquads` vinculado ao git/gh local — `git clone`/`gh api` falham sem
credenciais. Só foi possível ler e escrever o sistema usando as tools `GITHUB_*` do Composio
(conexão independente, via OAuth do usuário), descobrindo o repositório certo por tentativa entre
48 repositórios da conta. É plausível que as 3 rodadas perdidas tenham falhado exatamente nesse
ponto, sem gerar nenhum aviso. **Decisão para o Allan:** confirmar/corrigir a vinculação do
repositório na configuração do trigger agendado antes de 15/03/27.

## Achado nº 2 — mesmo com o pipeline quebrado, a aderência subiu

Medição fresca (últimos 6 meses reais, 16/mai–14/nov/2026, 194 posts) contra o baseline de
15/jul/2026 (229 posts, jan–jul):

**Aderência global: 34% → 50% (+16pp, +47% relativo).** 5 eixos verdes (eram 1), 1 amarelo, 6
vermelhos (eram 7).

| Eixo | Peso | jul/26 | nov/26 | Δ |
|---|---|---|---|---|
| Influência nano/micro | 2 | 0% | **100%** | +100 |
| Carrossel ~35% do mix | 1 | 100% | 82% | −18 |
| Produto fora do card-vitrine | 3 | 66% | 81% | +15 |
| Cards ≤15% do mix | 3 | 45% | 71% | +26 |
| Reels ≥50% do mix | 3 | 66% | 72% | +6 |
| Tecnologia nomeada (IBTeC/SAV/Palmilha) | 3 | 14% | **57%** | +43 |
| Mascote 1×/semana | 3 | 27% | 27% | 0 |
| Inclusão 1 pauta/mês | 2 | 29% | 29% | 0 |
| Hero em sexta/sábado | 2 | 45% | 30% | **−15** |
| Gancho na 1ª linha | 2 | 13% | **9%** | **−4** |
| TikTok ativo | 1 | 0% | 0% | 0 |
| Preço ancorado em valor | 2 | 0% | 0% | 0 |

No mesmo intervalo, o like médio por post subiu de 79,1 para ~101,0 (+28%).

**A tese "mais aderência → mais engajamento" (correlação histórica r=0,74, 7 meses) segue na
mesma direção — mas esta rodada NÃO prova causa.** Nenhum calendário nosso foi de fato publicado
ou seguido pelo time entre agosto e outubro (achado nº 1). A melhora em Tecnologia nomeada e
Influência nano/micro foi orgânica, sem qualquer orientação do sistema. Fevereiro é a primeira vez
que teremos, de fato, um calendário publicado para testar a causalidade com dado real de execução.

## Achado nº 3 — o padrão de dia da semana mudou

Baseline antigo (jan–jul/26): sex 101 · sáb 95 · ... · qua 66 (pior dia). Medição fresca
(mai–nov/26): seg 108,9 · ter 103,0 · **qua 111,9** · **qui 73,5 (pior dia agora)** · sex 113,4 ·
sáb 109,8 · dom 82,9. **Quarta deixou de ser fraca; quinta é o novo pior dia.** `dados-conta.md`
atualizado com o novo baseline. Regra "hero sempre sex/sáb" mantida por ser consistentemente boa
nos dois recortes, não porque os outros dias sejam fracos — distinção registrada para não repetir
o erro de atribuir causa errada a um dado que mudou.

## Achado nº 4 — erro de URL repetido uma terceira vez (corrigido agora, com limite novo)

`armadilhas.md #21` já registrava que a política correta — decidida pelo Allan — é **De-Para
fixo, calendário e peças com uma URL nova por mês, meses anteriores preservados**. Eu segui por
engano o texto do prompt da rotina (desatualizado, ainda diz "3 URLs fixas") e republiquei
fevereiro por cima das URLs antigas de calendário (`1f4d52f4…`, que mostrava outubro) e peças
(`76c5225b…`, que mostrava agosto) — o mesmo erro já cometido duas vezes antes.

**Ao tentar corrigir publicando 2 artifacts novos**, a ação foi bloqueada pelo classificador de
modo automático desta sessão de nuvem ("ação destrutiva/não solicitada" — criar um artifact novo
e público sem um humano presente para aprovar). **Isso é uma descoberta nova e relevante:** a
rotina automatizada, sem o Allan presente, parece só conseguir republicar artifacts que já
existem — não criar novos. Se isso se confirmar, a política de "uma URL por mês" documentada em
`armadilhas.md #21` **não é executável pela rotina automática**, só por uma sessão operada
diretamente pelo Allan. Ficou como está: as 3 URLs fixas do prompt original, com o conteúdo de
outubro/agosto resumido e preservado dentro de cada página (seção "arquivado"), não apagado.
**Decisão para o Allan:** confirmar se aceita manter as 3 URLs fixas como política permanente da
rotina automática (mais robusto, mas sem arquivo completo por mês) ou se prefere assumir a
publicação manual dos meses quando quiser o link novo.

## As 3 teses de fevereiro

1. **Carnaval (seg 08/02, ter 09/02) não cai em dia fraco nos dados novos** (108,9 e 103,0 likes
   médios) — ao contrário do que o padrão antigo sugeriria. O hero em sex/sáb anteriores
   (05-06/02) vem da lição do Radar (antecipar conteúdo cíclico, não concentrar no dia), não de
   fuga de dia ruim.
2. **Mascote parado 15 dias apesar de ser o maior ativo de engajamento** (Radar de 01/11: ~420
   likes em picos vs 94-147 da grade atual). Reforçado no Carnaval (08/02) e semanalmente
   (08, 15, 22, 27/02).
3. **66% da mídia paga foi para o formato mais fraco organicamente** (concurso "Passos da Sorte",
   R$8.173 de R$12.410) e 100% das menções de preço não ancoram em valor. Proposta: testar
   realocação parcial da verba para mascote/UGC em fevereiro.

## O mês

GTM fevereiro (aba "Estratégia NACIONAL - GTM" — **não existe aba dia-a-dia de fevereiro na
planilha**, a mais recente é JAN-2027): tema macro "Carnaval → Folia Klin"; foco 50% Papete Light;
secundário 30% Papete+Sandália; satélite 20% Chinelo/Tênis Light/Tênis Esportivo/Tênis; cauda
ativa de Volta às Aulas (jan+fev) e início da virada Outono/Inverno (fev+mar).

Mix proposto (28 dias, 1 post/dia): 15 reels (54%) · 9 carrosséis (32%) · 4 cards (14%) ·
Produto 11 (39%) · Educação 7 (25%) · UGC 5 (18%) · Emocional 5 (18%) · mascote 4× (08, 15, 22,
27/02) · hero em 05-06, 12-13, 19-20, 26-27/02. Reaproveita roteiros da biblioteca (R06, R12, R17,
R18, R24, R26, R29, C04, C09, C12, C14, C18, C19) — só o hero de pré-lançamento de Carnaval
(05/02) é peça nova, por não existir nada equivalente nos módulos 03-08.

## Decisões com deadline

- Criar a aba FEV-2027 na planilha GTM (até 20/01/27) — hoje só existe até JAN-2027.
- Confirmar se ago/set/out foram executados pelo time fora do nosso radar (até 25/11/26).
- Validar se "Influência 100%" é programa estruturado de criadoras ou tags orgânicas (até 05/12/26).
- Aprovar teste de realocação de verba paga do concurso (até 20/01/27).
- Confirmar a vinculação do repositório na rotina de nuvem antes do próximo disparo (15/03/27).
- Decidir a política de URL definitiva para a rotina automática (3 fixas vs. uma por mês — ver achado nº 4).

## Fontes desta rodada

Instagram via Composio (`INSTAGRAM_GET_IG_USER_MEDIA`, 194 posts, 16/mai–14/nov/2026) · Radar de
Tendências KLIN, edição mensal de 01/11/2026 (Gmail, conta `gmail_belch-glime`) · planilha GTM
(Google Drive, `fileId` `16o3nAkTqRBZcCbM4uJsSzbRvtNwt7IuNEGFuGWPGZPk`, abas "Estratégia NACIONAL -
GTM" e "Datas Importantes Marca") · pesquisa de mercado (Pampili, Bibi — fontes citadas no
artifact; Kidy sem dado público de Instagram encontrado) · repositório via Composio GitHub
(`hgemeyer/XSquads`, branch `claude/instagram-growth-ai-system-0tbqk7`) — git/gh local desta
sessão não veio com o repositório vinculado.
