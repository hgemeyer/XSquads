# Registro de Avanços — Sistema de Crescimento Instagram Klin

> Log oficial do projeto. Toda sessão de trabalho deve atualizar este arquivo e fazer push (ver skill `klin-growth` e Routine de push automático).

## Estado atual (15/nov/2026)

> ✅ **Retomado.** As 3 telas de fevereiro/2027 estão publicadas. Achado crítico desta rodada: a rotina ficou 3 meses (ago/set/out) sem deixar rastro — ver [21-fevereiro.md](21-fevereiro.md) §Achado nº1. Pendência de design ainda aberta: política de URL (3 fixas vs. 1 por mês) — ver §Achado nº4 do mesmo módulo.

**Fase:** Primeira comparação real de aderência entre rodadas (34% jul/26 → 50% nov/26) + calendário e peças de fevereiro/2027 publicados.
**Branch de trabalho:** `claude/instagram-growth-ai-system-0tbqk7` (ainda não mesclado ao `main` — abrir PR quando o time aprovar).
**Artifacts:** [De-Para GTM + aderência](https://claude.ai/code/artifact/dec7f5e9-fb08-45ba-b7fe-c215bed1583e) · [Calendário de Fevereiro](https://claude.ai/code/artifact/1f4d52f4-1e02-4a9d-aafe-810bbd033b99) · [Peças de Fevereiro](https://claude.ai/code/artifact/76c5225b-5260-4b10-95dc-c9bb6163fdf5)

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

### 15/jul/2026 — Sessão 4 (formato das peças)

18. **Módulo 18 criado — [18-pecas-agosto.md](18-pecas-agosto.md)** + artifact: https://claude.ai/code/artifact/76c5225b-5260-4b10-95dc-c9bb6163fdf5 — 7 peças de agosto com frame de abertura, roteiro com timecode, texto na tela, B-roll e legenda. Cobre os 3 formatos. **R19 e C02 aparecem na íntegra** (já estavam prontos — é gravar).
19. **Bug corrigido no módulo 17:** o guião `R01` estava citado em **dois dias** (01 e 27/08) e errado nos dois — 01/08 usa **R22** (primeiros passos) e 27/08 usa **C02** (o carrossel do tema; R01 é o reel). Artifact do calendário republicado na mesma URL. **Regra nova: ao citar guião, conferir se o ID bate com o formato (R=reel, C=carrossel) e se não repete no mês.**
20. **Peça-chave do trimestre definida — 15/08:** gancho *"Seu filho não precisa de tênis ortopédico. E sim, é uma marca de calçado falando isso."* Nomeia IBTeC + ocupa "bico largo" (ação nº 1 do Radar) + estreia no TikTok, tudo na mesma peça. Fecha com ressalva de que a orientação do pediatra vem primeiro — inegociável.
21. **Travas de produção registradas:** 06/08 exige autorização de imagem assinada (família + especialista) antes de gravar, e narrativa de rotina, não de "superação"; 22/08 respeita a regra de que o mascote nunca fala.

### 15/jul/2026 — Sessão 5 (skill reescrita: o mês vira plano completo)

22. **Skill `klin-growth` reescrita** (`.claude/skills/klin-growth/`, versionada no repo). **Novo contrato de entrega:** o Allan diz um MÊS → a skill estuda conta + mercado + concorrência + formatos já usados e entrega **3 artifacts** (De-Para GTM na URL fixa · `<Mês> — Calendário Proposto` · `As peças de <mês>`). Antes o SKILL.md era um índice de módulos; agora é um fluxo executável.
23. **Estrutura nova:** `SKILL.md` (entrada) + `references/` (fluxo-mensal, aderencia, artifacts, pecas, dados-conta, armadilhas) + `scripts/medir_aderencia.py` (motor do placar, roda no workbench Composio) + `LEIA-ME.md` (instalação/dependências).
24. **`references/armadilhas.md` — 22 erros registrados** para não se repetirem. Os que mais custaram: o emoji 🐾 inflando o mascote de 27% p/ 100%; `R01` citado em dois dias e errado nos dois; `file_id` vs **`fileId`** no Drive; emoji virando tofu na Gotham; CTA com y fixo colidindo; a IA inventando logo na lingueta; `capa_conceito` (R7) saindo sem logo e sem contraste; push não confirmado no remoto.
25. **Régua de entrega registrada:** todo plano do mês responde (1) quanto do que pedimos já fazemos — com número, (2) o que muda em cada dia e por quê, (3) como a peça sai, (4) o que trava se não decidirem agora, (5) o que é dado e o que é aposta. E **nunca** vender correlação como causa.
26. **Pasta portátil gerada** para rodar em outra máquina/Cowork: `Downloads\klin-growth\` + `Downloads\klin-growth.zip` (26 KB). O `LEIA-ME.md` lista dependências (Composio instagram/googledrive/gmail; repo XSquads obrigatório; designer-klin + FAL_KEY só para arte).

### 15/jul/2026 — Sessão 6 (modelo de operação: Allan opera, time consome)

27. **Modelo definido pelo Allan:** ele é o **único operador** (roda a skill, mede, publica, faz push). O **time consome e operacionaliza** — grava e publica a partir das telas. O time **não** precisa de Composio, nem de write no repo, nem da skill. Precisa de **3 links**.
28. **CORREÇÃO DE DESENHO — as 3 URLs agora são FIXAS.** Antes só o De-Para era fixo; calendário e peças nasciam com URL por mês, o que obrigaria o Allan a **recompartilhar tudo todo mês, para sempre** (artifact nasce privado). Agora: De-Para `dec7f5e9…` · Calendário `1f4d52f4…` · Peças `76c5225b…` — republicar sempre, título acompanha o mês, URL e favicon não mudam. **Compartilha uma vez, vale para sempre.** Histórico dos meses fechados fica no repo (módulos) e no version picker do artifact (`label`).
29. **Achado de acesso:** repo é **público** (o time lê módulos e skill sem liberação), mas só `hgemeyer` é colaborador e o branch **não tem PR para `main`** — quem clonar o default não acha nada. Como o time não opera, isso deixou de ser bloqueio; segue pendente só para arquivar o trabalho em `main`.
30. **Regra nova de escrita:** as telas são escritas **para quem executa, não para quem aprova**. Gancho, texto na tela, B-roll, legenda, CTA e trava de produção têm que estar na página — o que fica na conversa não chega em quem grava.
31. **Armadilhas 23 e 24 registradas:** artifact nasce privado e a ferramenta não compartilha (avisar sempre que publicar artifact novo); e o time não opera — escrever para quem executa.

### 15/jul/2026 — Sessão 7 (outubro + a cadência dos 75 dias)

32. **CADÊNCIA DEFINIDA (regra permanente):** o time trabalha com **75 dias de antecedência**. Todo **dia 15** roda-se o **mês corrente + 3** (15/jul→outubro · 15/ago→novembro · 15/set→dezembro · 15/out→janeiro). Automatizado na rotina de nuvem **`trig_01AGbqkuLVH36dSYK64uykjR`** — dia 15, 10h BRT (13h UTC), Opus 4.8, repo XSquads, conectores Composio + Gmail + Drive, aviso no Telegram. Primeira execução: **15/08/2026** (novembro).
33. **Módulo 19 criado — [19-calendario-outubro.md](19-calendario-outubro.md)** + artifact republicado na URL fixa `1f4d52f4…` (label `out-26`).
34. **DESCOBERTA: não existe aba de outubro.** O plano dia a dia da planilha GTM **termina em SET** — não há Out/Nov/Dez. Outubro nasceu da linha **OUT** da aba `Estratégia NACIONAL - GTM`, que é rica (Dia das Crianças 17/09-12/10 + HALLOW KLIN 14/10-05/11; foco flash carrinho/princesa; satélite **acqua kids PINs**). **Ação para o time: criar a aba Out, com coluna Formato.**
35. **As 5 teses de outubro:** (1) o hero de presente é **sábado 10/10**, não o dia 12 — o Dia das Crianças cai numa **segunda** (78 likes vs 96 do sábado) e a compra decide no fim de semana anterior; (2) **Halloween cai num sábado (31/10)** = sábado + mascote + trend = a fórmula do 422, o maior viral do trimestre; (3) ⚠️ **"Cards da data"** do HALLOW KLIN contraria o dado (card 62 × reel 106) → 1 card no 29 e o hero em reel no 31; (4) **PINs: Radar e GTM convergiram sozinhos** — não é sugestão nova, é acelerar o que já está no plano; (5) o **FOCO do mês é LED** (flash "pisou, piscou") — 50% do foco **só existe em vídeo**, o argumento mais fácil contra a vitrine.
36. **Mix de outubro:** 18 reels (58%) · 11 carrosséis (35%) · 2 cards (6%) · mascote **semanal** (5 eps) · tecnologia 2× · inclusão 1× · preço ancorado 4× · **hero 10 de 10** em sex/sáb.
37. **PENDÊNCIA:** as **peças de outubro** ainda não foram montadas — o artifact `76c5225b…` segue mostrando as de agosto. Prioridade da próxima sessão: 10/10 (hero de presente + PINs), 31/10 (Halloween + mascote), 07/10 (Dra. Be) e 02/10 (Flash no escuro).

### 15/jul/2026 — Sessão 8 (reversão da política de URL + ganchos e copy) — **PARADA NO MEIO**

38. **REVERSÃO (decisão do Allan):** **um link por mês**, todos vivos. Só o **De-Para** continua fixo. Eu tinha fixado os 3 argumentando que o time não pode receber link novo todo mês — aí rodei outubro, **republiquei por cima e apaguei a visão de agosto**, que já estava compartilhada. **Custo aceito:** 2 links novos por mês para o Allan compartilhar. **Lição registrada (armadilha 21): decisão de design que apaga trabalho anterior não é minha.**
39. **Gancho e copy passam a ser parte do calendário**, em todos os dias — não extra. O time grava a partir dele, e a **aba SET marca "Hooks?" como pendente**: é isso que o calendário fecha. Spec atualizada em `references/artifacts.md`.
40. **As abas de mês não têm o mesmo layout** (armadilha 25): `Ago` = `Data|Dia|Conteúdo|Tipo|Observação` (**sem** Formato); `SET` = com **Formato** (12 carrosséis · 11 reels · 7 cards) + coluna de pendências. **Inspecionar as 6 primeiras linhas antes de parsear.**
41. **Setembro lido por inteiro** (30 dias, com formato e observações). Destaques: 04 e 10/09 = série de mães reais (a melhor aposta do trimestre, "Rotina Real"); 15/09 Dia do Cliente; 17/09 SAV; 18-19/09 lançamento Dia das Crianças; 26/09 desafio das telas; 29/09 volta da animação do Klin.
42. **Gerador `scripts/gen_calendarios.py` criado com os 92 dias escritos** (ago 31 + set 30 + out 31), cada um com formato, tipo, guião, proposta, **gancho** e **copy**. Mais `scripts/_base.css` (tokens, chips, `.hk`, `.cp`, `.nav`). **Não foi executado nem publicado** — é o ponto exato da retomada.
43. **Estado inconsistente registrado em [20-RETOMAR-AQUI.md](20-RETOMAR-AQUI.md)**, com o passo a passo do que falta.

### 15/nov/2026 — Sessão 9 (retomada: fevereiro/2027, primeira comparação real de aderência)

44. **Módulo 21 criado — [21-fevereiro.md](21-fevereiro.md)**: plano completo de fevereiro/2027, rodado com 75 dias de antecedência (mês corrente nov/26 + 3).
45. **Achado crítico: pipeline parado 3 meses em silêncio.** Nenhuma das rodadas de 15/ago, 15/set, 15/out deixou rastro no PROGRESSO. Hipótese confirmada nesta sessão: a sessão de nuvem não veio com o repositório vinculado ao git/gh local — só foi possível operar via tools `GITHUB_*` do Composio, achando o repo certo (`hgemeyer/XSquads`) por tentativa entre 48 repositórios da conta. Armadilha 27 registrada.
46. **Primeira comparação real de aderência entre rodadas: 34% (jul/26) → 50% (nov/26, recorte de 6 meses, 194 posts).** Maiores saltos: Tecnologia nomeada (14%→57%) e Influência nano/micro (0%→100%), ambos orgânicos, sem calendário nosso publicado no intervalo. Maiores quedas: Gancho na 1ª linha (13%→9%) e Hero em sex/sáb (45%→30%). Mascote e Preço seguem travados em 27% e 0%.
47. **Tese "aderência→engajamento" segue na mesma direção (79,1→101,0 likes médios) mas não pode ser lida como causa** — não houve calendário executado no intervalo. Fevereiro é a primeira rodada que testa isso com dado real de execução.
48. **Achado: o padrão de dia da semana mudou.** Quarta deixou de ser fraca (66→111,9 likes); quinta é o novo pior dia (73,5). `dados-conta.md` revalidado por inteiro. Armadilha 28 registrada.
49. **Erro de URL repetido uma 3ª vez, parcialmente corrigido.** Republiquei fevereiro por cima das URLs antigas de calendário (tinha outubro) e peças (tinha agosto), repetindo o erro já documentado na armadilha 21. Ao tentar corrigir criando 2 artifacts novos (política correta, decidida pelo Allan), o classificador de modo automático bloqueou a ação como destrutiva/não solicitada numa sessão sem humano presente. Mantidas as 3 URLs fixas; conteúdo de ago/out resumido e preservado dentro das páginas. Armadilha 29 registrada — decisão de política pendente com o Allan.
50. **Pesquisa de mercado:** Pampili fez rebranding com nostalgia (collab Ursinhos Carinhosos); Bibi reposicionou com "Bibi Educa"; Kidy sem dado público de Instagram encontrado — lacuna de inteligência registrada.
51. **GTM de fevereiro:** não existe aba dia a dia própria (a mais recente é JAN-2027) — usada a linha de fevereiro da aba "Estratégia NACIONAL - GTM" (tema "Folia Klin", foco Papete Light).
52. **Calendário e peças de fevereiro montados** reaproveitando roteiros prontos dos módulos 03-08 (R06, R12, R17, R18, R24, R26, R29, C04, C09, C12, C14, C18, C19) — só o hero de pré-lançamento de Carnaval é peça nova.
53. **`dados-conta.md` e `armadilhas.md` atualizados** com o baseline novo e as armadilhas 27-29.

## Decisões em aberto (aguardando o time/Allan)

- [ ] Aprovar o de-para FINAL (reunião com Righi/mkt) — deadline original **17/07** (#CresciDeKlin), já vencido, revalidar relevância.
- [ ] Validar placeholders de depoimentos/dados internos nos Stories (módulo 6)
- [ ] Revisão técnica dos conteúdos de saúde (Dra. Be / pediatra)
- [ ] Propor coluna **Formato** na planilha GTM (hoje só define tema e tipo)
- [ ] Abrir PR para `main` quando aprovado
- [ ] Automação de publicação (Nível 3): Routine diária de post via API + hospedagem de assets em URL pública
- [ ] **Criar a aba FEV-2027 na planilha GTM** (até 20/01/27) — hoje só existe até JAN-2027
- [ ] **Confirmar se ago/set/out foram executados pelo time fora do nosso radar** (até 25/11/26)
- [ ] **Validar se "Influência 100%"** (10 posts com @menção, medição de nov/26) é programa estruturado de criadoras ou tags orgânicas (até 05/12/26)
- [ ] **Aprovar teste de realocação de verba paga** do concurso "Passos da Sorte" para mascote/UGC (até 20/01/27)
- [ ] **Confirmar a vinculação do repositório** na configuração do trigger agendado de nuvem (antes de 15/03/27 — ver módulo 21 §Achado nº1)
- [ ] **Decidir a política de URL definitiva** para a rotina automática: 3 fixas (robusto, sem arquivo completo por mês) vs. 1 nova por mês (decisão anterior do Allan, mas parece não executável sem humano presente — ver módulo 21 §Achado nº4)

## Métricas-alvo do trimestre (desatualizadas — revisar no próximo ciclo)

| Métrica | Base (jul/26) | Atual (nov/26) | Meta (30/set/26, vencida) |
|---|---|---|---|
| Likes médios/post | 79,1 | ~101,0 | ≥100 |
| Comentários médios/post | — | — | ≥7 |
| Likes médios/Reel | 105,9 | 146,7 | ≥140 |
| Fonte de medição | API Instagram via Composio | idem | idem |

## Como continuar o trabalho (qualquer sessão nova)

1. Ler este arquivo + [README.md](README.md) (índice dos 21 módulos) via a conexão GitHub disponível (Composio `GITHUB_*` se o git/gh local não tiver o repositório vinculado — ver módulo 21 §Achado nº1)
2. Usar o skill **`klin-growth`** (carrega automaticamente neste repo) para os fluxos operacionais
3. Ao final de QUALQUER avanço: atualizar este arquivo, commit convencional e push no branch — **confirmar no remoto antes de dizer que subiu**

## Como pedir o plano de um mês (contrato da skill, desde 15/07)

Basta dizer o mês — **"roda o growth de fevereiro"**. A skill lê o repo, puxa a conta pela API,
mede a aderência (12 eixos), lê a aba do mês na planilha GTM, consome o Radar mais recente e a
concorrência, e entrega **3 artifacts encadeados**:

1. **De-Para GTM** — URL FIXA `dec7f5e9-fb08-45ba-b7fe-c215bed1583e` (republicar, nunca criar nova)
2. **`<Mês> — Calendário Proposto`** — os 30/31 dias com formato, gancho e ângulo
3. **`As peças de <mês>`** — frame de abertura, roteiro com timecode, texto na tela, legenda

Manual completo em `.claude/skills/klin-growth/` (SKILL.md + references/ + scripts/).
**Ler `references/armadilhas.md` antes de reportar qualquer número.**
