# klin-growth — instalação e uso em outra máquina

## Modelo de operação (ler antes de tudo)

| Papel | Quem | O que precisa |
|---|---|---|
| **Opera** — roda a skill, mede, publica, faz push | **só o Allan** | Composio, write no repo, esta skill |
| **Consome e operacionaliza** — grava, produz, publica no feed | **o time** | Só os **3 links fixos** |

**O time não instala nada.** Não precisa desta skill, nem de Composio, nem de acesso de escrita
no repo. Ele abre 3 links e trabalha. Esta pasta é para as máquinas onde **o Allan** opera
(local ou Cowork).

Skill portátil. Copie a pasta inteira `klin-growth/` para `~/.claude/skills/` (Claude Code) ou
suba no Cowork. O nome da pasta **tem que ser** `klin-growth` (bate com o `name:` do SKILL.md).

```
klin-growth/
├── SKILL.md                      ← manual principal (a entrada)
├── LEIA-ME.md                    ← este arquivo
├── references/
│   ├── fluxo-mensal.md           ← os 8 blocos do "roda o growth de <mês>"
│   ├── aderencia.md              ← os 12 eixos, fórmula, ordem de ataque
│   ├── artifacts.md              ← os 3 artifacts: estrutura, tokens, esqueleto
│   ├── pecas.md                  ← anatomia, régua, arte final
│   ├── dados-conta.md            ← baseline vivo (revalidar todo mês)
│   └── armadilhas.md             ← 22 erros já cometidos — LER ANTES DE REPORTAR
└── scripts/
    └── medir_aderencia.py        ← motor do placar (roda no workbench Composio)
```

## Como usar

Diga um mês: **"roda o growth de setembro"**. A skill estuda a conta, o mercado, a
concorrência e o que já foi publicado, e entrega **3 artifacts**: De-Para GTM (URL fixa),
Calendário do mês dia a dia, e As peças do mês.

## Dependências

**Obrigatórias:**
- **Composio MCP** com conexões ativas: `instagram` (conta klin_oficial), `googledrive`, `gmail`.
- **Git** com acesso a `hgemeyer/XSquads`, branch `claude/instagram-growth-ai-system-0tbqk7`.
  É onde vivem os módulos 01-18 (guiões, concorrência, estudo, de-para, aderência) — **a skill
  depende deles**. Sem o repo, o fluxo roda pela metade.

**Opcionais (só para arte final):**
- Skill `designer-klin` + `klin-brand` (motor Pillow `klin_kit.py`, fontes, logos).
- Skill `serie-animada-klin` (helper `fal_api.py`) + env **`FAL_KEY`**.
- Python 3.11 com Pillow/rembg — no Windows do Allan:
  `C:\Users\karde\AppData\Local\Programs\Python\Python311\python.exe`.
- Sem esses, a skill entrega os 3 artifacts normalmente; só não gera PNG.

## O que NÃO está aqui (vive no repo)

Os 18 módulos em `docs/instagram-growth-system/`: pesquisa, 50 ganchos, 30 reels, 20
carrosséis, sistema visual, legendas, calendário, reutilização, estudo 360º, concorrência,
de-para, radar, aderência, calendário de agosto e peças de agosto.

**Primeiro comando em máquina nova:**
```
git clone -b claude/instagram-growth-ai-system-0tbqk7 https://github.com/hgemeyer/XSquads.git
cat XSquads/docs/instagram-growth-system/PROGRESSO.md
```

## As 3 URLs fixas — o canal do time

**Republicar sempre nestas. Nunca criar URL nova** — o time salvou esses links e não pode
receber link novo todo mês.

| Artifact | URL |
|---|---|
| De-Para GTM | https://claude.ai/code/artifact/dec7f5e9-fb08-45ba-b7fe-c215bed1583e |
| `<Mês>` — Calendário Proposto | https://claude.ai/code/artifact/1f4d52f4-1e02-4a9d-aafe-810bbd033b99 |
| As peças de `<Mês>` | https://claude.ai/code/artifact/76c5225b-5260-4b10-95dc-c9bb6163fdf5 |

O título acompanha o mês; a URL e o favicon não mudam. Cada mês fechado fica registrado como
módulo no repo — **a história vive no repo; o link é sempre o mês corrente.**

⚠️ **Artifact nasce privado.** Estes 3 já foram compartilhados pelo Allan. Qualquer artifact
**novo** precisa que ele compartilhe pelo menu da própria página — nenhuma ferramenta faz isso
por ele. É por isso que a regra de URL fixa existe: compartilha uma vez, vale para sempre.

## IDs que a skill precisa

- Instagram: conta `klin_oficial` (ig_user_id `"me"` via Composio)
- Planilha GTM (Drive): `16o3nAkTqRBZcCbM4uJsSzbRvtNwt7IuNEGFuGWPGZPk` — campo **`fileId`**
- Radar: Gmail, `subject:"Radar de Tendências KLIN"` (Routine a cada 3 dias)

Atualizado: 15/07/2026.
