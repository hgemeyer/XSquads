# Os 3 artifacts — estrutura, tokens e esqueleto

A entrega do mês são 3 páginas HTML publicadas como Artifact, encadeadas por link no rodapé.
Elas formam uma família visual: **mesma paleta, mesma tipografia, mesmos chips**. Quem abre a
segunda tem que sentir que é o mesmo documento.

Antes de escrever qualquer uma: carregar a skill `artifact-design`.

## As 3 URLs são fixas — republicar, nunca criar nova

| Artifact | URL | Favicon |
|---|---|---|
| De-Para GTM | `dec7f5e9-fb08-45ba-b7fe-c215bed1583e` | 🐾 |
| `<Mês> — Calendário Proposto` | `1f4d52f4-1e02-4a9d-aafe-810bbd033b99` | 📅🐾 |
| `As peças de <mês>` | `76c5225b-5260-4b10-95dc-c9bb6163fdf5` | 🎬🐾 |

Passar sempre `url` no Artifact. **Por quê:** o time só consome — ele salvou esses 3 links e
não pode receber link novo todo mês. URL nova = time olhando o mês errado.

Título acompanha o mês; **URL e favicon não mudam** (o time acha a aba pelo ícone). Usar `label`
(`set-26`, `out-26`) para o histórico de versões. O mês fechado fica registrado como módulo no
repo — **a história vive no repo; o link é sempre o mês corrente.**

**Artifact nasce privado.** Só nas 3 URLs acima o compartilhamento já está feito. Qualquer
artifact **novo** exige que o Allan compartilhe pelo menu da página — avisar sempre, porque
nenhuma ferramenta faz isso por ele.

---

## Identidade (não mudar — é a família)

```css
/* claro */
--bg:#FDF9F0; --surface:#FFFFFF; --ink:#2A2418; --muted:#7A6F58; --line:#EAE0C8;
--accent:#E8A400; --accent-deep:#8A6200; --accent-soft:#FFF3D0;
--from-bg:#F3EEE1; --from-ink:#5C5340; --to-bg:#FFFAE8; --to-border:#E8C25A;
--ok:#2E7D4F; --ok-bg:#E3F1E7; --warn:#A26B08; --warn-bg:#FBEECF;
--late:#B0392F; --late-bg:#F7E2DF; --track:#EFE7D2;
--chip-prod:#C4E0EF; --chip-prod-ink:#215A75;   /* Produto   */
--chip-edu:#DCE9CF;  --chip-edu-ink:#3F6224;    /* Educação  */
--chip-emo:#F3D9E4;  --chip-emo-ink:#8A3B5C;    /* Emocional */
--chip-ugc:#E4DBF2;  --chip-ugc-ink:#5B4390;    /* UGC       */
/* escuro */
--bg:#201B10; --surface:#2A2415; --ink:#F1E9D4; --muted:#B0A483; --line:#42392250;
--accent:#F0B723; --accent-deep:#F5CE60; --accent-soft:#3A2F10; --track:#3A3220;
--ok:#7FC79A; --ok-bg:#22402D; --warn:#E4B45E; --warn-bg:#453413;
--late:#E58A80; --late-bg:#4A2521;
```

- **Tipografia:** display `"Trebuchet MS", "Segoe UI"` · corpo `"Segoe UI", system-ui` ·
  dados/datas `ui-monospace, Menlo` com `font-variant-numeric: tabular-nums`.
- **Temas:** tokens em `:root`, redefinidos em `@media (prefers-color-scheme:dark)` **e** em
  `:root[data-theme="dark"]`/`[data-theme="light"]`. Nunca estilizar dentro do media query.
- **Emoji-legenda comum aos 3:** ⭐ aposta alta (sex/sáb) · 🐾 mascote · 🔬 tecnologia nomeada ·
  ♿ inclusão · 💰 preço ancorado em valor · 📱 TikTok · 📡 vem do Radar · 🎯 data especial.
- Favicons: De-Para `🐾` · Calendário `📅🐾` · Peças `🎬🐾`. **Manter estáveis entre republicações.**

---

## 1. De-Para GTM Klin — URL FIXA `dec7f5e9-fb08-45ba-b7fe-c215bed1583e`

**Sempre republicar passando `url`.** Criar URL nova quebra o link que o time já tem.

Seções:
1. **Aderência: o que pedimos × o que já fazemos** — medidor global (donut `conic-gradient`),
   placar dos 12 eixos (barra + nota + "o que já temos feito" + linha do porquê importa),
   e a série mensal aderência × likes. **Vermelhos primeiro.**
2. A estrutura (vale para os 3 meses) — as ~10 mudanças de fundo, em linhas
   `Estamos fazendo → Eu faria` + `Dado:`
3. Mês corrente, dia a dia
4-5. Meses seguintes
6. O que já passou — e como recuperar (🔴 passou / 🟡 parcial)
7. As decisões com deadline nesta semana

Rodapé: base de dados, **nota de metodologia** (como a aderência é medida) e a ressalva do
classificador de mascote.

## 2. `<Mês> — Calendário Proposto`

Grade **Seg→Dom** (7 colunas). Seg-first não é estética: põe **sex e sáb adjacentes**, e a faixa
dourada vertical (`.cell.band`) mostra de relance que toda aposta alta cai nos dias que
entregam. Célula:

```
[dia + abrev]  [flags]
[chip formato] [chip tipo]
proposta (o que eu faria, com o porquê em negrito)
─────────
No GTM: <texto literal da aba>
```

Blocos abaixo da grade: legenda dos emojis · **O que muda de mês para mês** (tabela
julho real → agosto proposta) · **O mix de conteúdo** (aba × proposta) · **As decisões que
precisam sair antes do dia 1º**.

Rodapé: **a nota de leitura obrigatória** — "a aba define tema e tipo, não formato; o formato
aqui é proposta, não divergência" + o que foi preenchido onde o GTM dizia "a definir".

Mobile: `grid-template-columns:1fr`, esconder `.hd` e `.cell.empty`.

## 3. `As peças de <mês>`

1. **A anatomia de um reel** — frame 9:16 anotado + as 7 regras do módulo 07.
2. **As peças** (6-8, cobrindo os 3 formatos), cada uma:
   - frame 9:16 (ou 4:5) com o **texto de abertura como aparece na tela**
   - timeline com timecode: `🎙 fala` + `texto na tela` (pill escura/amarela) + `🎬 b-roll`
   - legenda real (1ª linha = gancho), hashtags
   - `.note` com o porquê / a trava de produção
3. **Carrossel**: strip horizontal de slides 4:5 (capa → conteúdo → resumo salvável → CTA).
4. **E os outros N dias** — tabela dia → de onde sai o guião.

**O bloco dourado é placeholder de foto/vídeo** — dizer isso no rodapé. Não são artes finais.

Frame em CSS:
```css
.phone{width:236px;aspect-ratio:9/16;border-radius:16px;position:relative;overflow:hidden;
  background:linear-gradient(160deg,var(--shot1),var(--shot2))}
.phone .scrim{position:absolute;inset:0;
  background:linear-gradient(180deg,rgba(0,0,0,.42) 0%,rgba(0,0,0,.05) 42%,rgba(0,0,0,.30) 100%)}
.hook{position:absolute;top:9%;left:12px;right:12px;text-align:center;font-weight:800;
  color:#fff;text-transform:uppercase;text-shadow:0 2px 10px rgba(0,0,0,.6)}
.safe{position:absolute;left:0;right:0;bottom:13%;border-bottom:1px dashed rgba(255,255,255,.42)}
/* 13% = os 250px de UI do Instagram em 1920 */
```

---

## Régua de escrita (vale para os 3)

- **Número ao lado da recomendação.** "≥50% reels" sozinho é opinião; "reel faz 106 likes,
  card 62" é argumento.
- **Vermelho primeiro.** O que não fazemos vem antes do que já fazemos.
- **Rotular dado × aposta.** Correlação nunca vira causa (ver `armadilhas.md`).
- **Dizer o que trava.** Prazo que estoura (recrutamento, agenda externa, paleta) vale mais
  que mais uma recomendação.
- **Não replanejar.** A tese do sistema: os temas do GTM estão certos; o desalinhamento é de
  formato e gancho — e isso se corrige regravando.
