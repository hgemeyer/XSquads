# Peças — anatomia, régua e arte final

## Antes de inventar: o sistema já tem o guião

| Módulo | O que tem |
|---|---|
| 03 | **50 ganchos** por família (curiosidade, choque, contraintuitivo, lista, erro, segredo, opinião forte, urgência, storytelling, autoridade) |
| 04 | **30 reels R01-R30** completos: gancho, roteiro por timecode, texto na tela, B-roll, prompt de capa IA, legenda |
| 05 | **20 carrosséis C01-C20**: capa-gancho, slide a slide, CTA, prompt de capa, legenda |
| 07 | Sistema visual: paleta, tipografia, zonas seguras, estilo por pilar, 21 prompts de IA |
| 08 | Sistema de legendas |

⚠️ **R = reel, C = carrossel.** Conferir que o ID bate com o formato proposto e que não se
repete no mês (já errei: R01 citado em dois dias, sendo que o carrossel do tema é o C02).

Guiões usados em ago/26: **R22** (primeiros passos, 01/08) · **R10** + gancho 27 (bastidor
IBTeC, 03/08) · **R19** (medir o pé, 17/08) · **C05** (Capri em 5 rotinas, 19/08) · **R11** +
gancho 2 (Palmilha/SAV, 21/08) · **R25** (Cresci de Klin, 28/08) · **C02** (7 sinais, 27/08).

---

## Anatomia de um reel (módulo 07, consolidada)

1. **Gancho falado E na tela** nos primeiros 2-3s. Máx. 8 palavras, corpo grande, terço
   superior central. **A mesma frase é a 1ª linha da legenda**, antes do "…ver mais".
2. **Nada de informação nos 250px de baixo** (UI do Instagram) — 13% do quadro em 1920.
3. **Legendar 100% das falas** — a maioria assiste sem som.
4. **Logo nunca no primeiro segundo.** Assinatura discreta no rodapé. No TikTok, sem logo no
   1º segundo, ponto.
5. **Luz natural quente, câmera "de mãe"**, levemente trêmida. Ângulo baixo: **pés e chão são
   a assinatura visual da Klin**. Produção caseira autêntica vence produção polida.
6. **Até 30s**, cortes rápidos, CTA único e sutil no fim.
7. **Saúde sempre com "converse com o pediatra".** Imagem de IA leva "*Conteúdo gerado por IA".

**Enquadramentos:** reel 9:16 (1080×1920) · carrossel 4:5 (1080×1350) · story 9:16 com
interativos no centro-inferior.

## Carrossel

Slide 1 = capa-gancho · miolo = 1 ideia por slide (numeral gigante amarelo) · penúltimo =
**resumo salvável** · último = CTA. Alternar cor de fundo entre telas, nunca repetir consecutiva.

## Travas de produção registradas

- **Inclusão (fórmula 464+270):** autorização de imagem assinada **pela família e pela
  especialista** antes de gravar. Narrativa é **rotina, não "superação"**. Sem consentimento, a
  peça não sai.
- **Mascote: nunca fala.** Quem conduz é a narração. Aparece inteiro no quadro, orelha caída,
  sempre o mesmo cão.
- **Peça de saúde:** fechar com a ressalva de que a orientação do pediatra/ortopedista vem
  primeiro. Inegociável.
- **Peça que depende de agenda externa** (Dra. Be, laboratório, selo IBTeC filmável): agendar
  no mês anterior ou ela não sai.

---

## Arte final — skill `designer-klin`

**Recorte honesto antes de prometer:** reel não tem arte final, tem **gravação**. O que se gera
é **capa + texto na tela**. As peças 100% estáticas são **card** e **carrossel**.

Fluxo (a skill `designer-klin` manda; aqui só o essencial):

1. **Foto de base**, em ordem: fotos aprovadas existentes → fal.ai (`fal-ai/flux/dev`,
   ~R$0,15/foto) → Card Produtos.
2. **Compor** com `klin_kit.py` (Pillow) — rodar com
   `C:\Users\karde\AppData\Local\Programs\Python\Python311\python.exe`.
3. **Inspecionar cada PNG com Read** — passo obrigatório, não formalidade.
4. **Entregar** em `Claude design\Propostas\<data> <objetivo>\` + `[C] legenda e hashtags.md`.
5. **Informar o custo** no fim da entrega.

### Regras que reprovam (as que já me pegaram)

- **A IA NUNCA inventa o calçado KLIN.** Enquadrar sem o calçado como herói, cortar a área dos
  pés com o card, ou compor o produto real por cima. **Sempre declarar essa ressalva ao
  entregar arte com foto IA.**
- **A IA inventa logo e deforma mão.** Já saiu rótulo vermelho na lingueta e dedos vermelhos
  deformados. Pedir "plain unbranded, no logos, no brand marks" e **inspecionar**.
- **Comfortaa só em título/hook**; Gotham Rounded em todo o resto. Comfortaa no corpo = "cara
  de arte de IA" = reprovado.
- **Emoji só pelo helper `emoji()`** — `center`/`sub_curto` desenham na Gotham, que não tem
  glifo e vira tofu (▯).
- **Posicionamento dinâmico:** usar o `y` que `titulo_hook()` devolve e empilhar. Y fixo colide.
- **Máx. 2 frases / ~6 palavras sobre foto.** O resto vai para a legenda.
- **Hook tem que dominar** (≥66px em 1080; datas ≥90px). Letra tímida reprova.
- **Toda peça de calendário leva hook + CTA** — CTA de engajamento, não de venda.
- **Logo oficial sempre**: outline na base (sobre foto) ou tint no topo (sobre chapado).
- **Grafismo encostando em letra reprova.** Zonas de texto são sagradas. Rosto também.
- **Não misturar registro** (fotográfico-emocional × vetorial-lúdico).
- **Capa de carrossel educativo:** preferir **R4 sobre foto** — `capa_conceito` (R7) sai sem
  logo, com contraste baixo e sem energia. O prompt de capa de cada carrossel já está no
  módulo 05.

### Receitas que funcionam

- **R4 — foto + card 1-canto:** foto full-bleed + card chapado cobrindo 30-40% com **um** canto
  arredondado ~90px + hook branco + CTA amarelo. É a receita mais segura para texto sobre foto
  — e o card ainda **cobre a área dos pés**, resolvendo a regra do calçado.
- **R10 — cena de sonho:** produto REAL via `fal-ai/nano-banana-2/edit` (fotos do produto como
  `image_urls`) em cena cinematográfica + texto mínimo. É a arte vendedora de produto.
- **R9 — fecho/CTA com mascote:** split diagonal + mascote vetor grande + pergunta aberta.

Entregas validadas: `Claude design\Propostas\2026-07-15 agosto pecas\` (card Dia dos Pais 09/08
+ capa do C02 27/08, com o script `compor_agosto.py` reaproveitável — troca só a foto).
