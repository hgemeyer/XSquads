---
name: klin-growth
description: >
  Opera o Sistema de Crescimento Instagram da Klin (@klin_oficial, calçados infantis).
  Use quando o usuário pedir: análise da conta Klin, atualização do de-para GTM, consumo do
  Radar de Tendências, criação de conteúdo (reels/carrosséis/stories/legendas/ganchos),
  estudo de concorrência (Bibi/Pampili/Kidy), ou qualquer avanço no projeto Klin/Instagram.
  Garante que todo avanço seja registrado em PROGRESSO.md, commitado e enviado ao branch.
---

# Klin Growth — Sistema de Crescimento Instagram

## Regra nº 1 — Continuidade via repo

Todo trabalho deste projeto vive em `docs/instagram-growth-system/` no branch
`claude/instagram-growth-ai-system-0tbqk7` (repo `hgemeyer/XSquads`).

**Ao iniciar:** `git checkout claude/instagram-growth-ai-system-0tbqk7 && git pull origin claude/instagram-growth-ai-system-0tbqk7`, depois ler `docs/instagram-growth-system/PROGRESSO.md` (estado atual) e `README.md` (índice dos módulos).

**Ao terminar QUALQUER avanço (obrigatório):**
1. Atualizar `PROGRESSO.md` (linha do tempo + decisões em aberto)
2. `git add docs/instagram-growth-system/ && git commit -m "docs: <o que avançou>"` (Conventional Commits)
3. `git push -u origin claude/instagram-growth-ai-system-0tbqk7`

Nunca deixar avanço sem push — sessões remotas são efêmeras; o repo é a única memória durável.

## Mapa dos módulos

| Módulo | Conteúdo |
|---|---|
| README.md | Índice + 7 pilares + como operar |
| PROGRESSO.md | **Estado atual, linha do tempo, pendências** — ler primeiro |
| 01-03 | Pesquisa, 20 oportunidades, 50 ganchos |
| 04-06 | 30 reels, 20 carrosséis, 30 stories (prontos p/ produção) |
| 07-08 | Sistema visual (21 prompts IA) e de legendas |
| 09-10 | Calendário 30 dias e reutilização multicanal |
| 11 | Estudo 360º: 6 meses de dados + leitura do GTM |
| 12-13 | Concorrência nacional e premium (com fontes) |
| 14 | **De-Para GTM FINAL** (documento de decisão do time) |
| 15 | Radar de Tendências × proposta (convergências + 7 ajustes) |

## Fontes de dados (via Composio MCP)

| Dado | Como acessar |
|---|---|
| Métricas da conta | `INSTAGRAM_GET_USER_INFO` / `INSTAGRAM_GET_IG_USER_MEDIA` (ig_user_id: "me", conta @klin_oficial) — paginar com `cursors.after`; legendas de posts específicos via `INSTAGRAM_GET_IG_MEDIA` |
| Planilha GTM | Google Drive, arquivo `16o3nAkTqRBZcCbM4uJsSzbRvtNwt7IuNEGFuGWPGZPk` ("GTM Klin") — exportar como xlsx via `GOOGLEDRIVE_DOWNLOAD_FILE` (abas: Jun/Jul/Ago/SET + Datas Importantes + Estratégia de Brindes) e parsear com openpyxl |
| Radar de Tendências | Gmail via `GMAIL_FETCH_EMAILS` com `subject:"Radar de Tendências KLIN"` — skill do usuário roda como Routine a cada 3 dias; sempre pegar a edição mais recente |

## Fatos-chave (não redescobrir; revalidar ~mensalmente com dados novos)

- Conta: 472,5k seguidores; engajamento base ~0,014%; meta ≥100 likes/post até 30/09
- Reels +69% likes / +122% comentários vs card; sex/sáb são os melhores dias
- Fórmulas virais provadas: concurso UGC (487), inclusão real c/ especialista (464+270), mascote+trend (422), emocional 3 gerações (416), série animada mascote (161-222)
- Card-vitrine de produto é o pior conteúdo — produto sempre disfarçado em rotina/ocasião de uso
- Diferenciais a martelar: selo IBTeC, SAV, Palmilha Ultra (resposta ao FisioFlex da Bibi)
- Campanha ativa: #CresciDeKlin (nostalgia intergeracional)
- Territórios vagos no segmento: TikTok e "mãe para mãe"; não disputar o Dia da Menina (23/09, Pampili)
- Tom: mãe para mãe, 💛🐾, nunca institucional, saúde sempre com "converse com o pediatra"; conteúdo IA marcado "*Conteúdo gerado por IA"

## Fluxos operacionais

**Atualizar estudo de performance:** puxar mídia dos últimos N meses via API → CSV (date,fmt,likes,comments) → estatísticas por mês/formato/dia → atualizar módulo 11 e metas do PROGRESSO.md.

**Consumir novo Radar:** buscar e-mail mais recente → cruzar com módulos 14-15 → atualizar matriz de convergência e o de-para → registrar em PROGRESSO.md.

**Atualizar o de-para visual:** editar o HTML e republicar o artifact existente (URL fixa: https://claude.ai/code/artifact/dec7f5e9-fb08-45ba-b7fe-c215bed1583e) — nunca criar URL nova.

**Criar conteúdo novo:** seguir formatos dos módulos 04-06 (IDs R/C/S sequenciais), ganchos do módulo 03, legendas do 08, visuais do 07 (paleta PV27: Rosa Pitaya, Laranja Papaya, Verde Glimmer + dourado Klin).

**Publicação via API (quando ativada):** exige asset em URL pública; stickers interativos de Stories só pelo app.
