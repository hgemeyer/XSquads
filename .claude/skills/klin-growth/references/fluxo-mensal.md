# Fluxo do mês — do "roda o growth de agosto" aos 3 artifacts

Tempo de referência: ~1 sessão. Nunca pular o bloco 3 (aderência) nem o 8 (push).

---

## 0. Gatilhos

"roda o growth de <mês>" · "monta o plano de <mês>" · "growth de set/26" · "quero o plano
completo de outubro" · ou simplesmente o Allan citando um mês no contexto do Instagram.

Se ele pedir só um pedaço ("só o calendário", "só a aderência"), entregue o pedaço — mas
avise o que fica faltando das 3 telas.

---

## 1. Ler o repo (5 min)

```
git checkout claude/instagram-growth-ai-system-0tbqk7 && git pull
```
Ler `docs/instagram-growth-system/PROGRESSO.md` e `README.md`. Os módulos que importam para
o plano do mês: **11** (estudo 360º), **14** (de-para), **16** (aderência), **17/18** (calendário e
peças do mês anterior — o padrão a repetir).

## 2. Puxar a conta (Composio → workbench)

Paginar `INSTAGRAM_GET_IG_USER_MEDIA` até esgotar o cursor. Salvar em `/mnt/files/`.

```python
all_items=[]; after=None; prev=None; pages=0
while pages < 12:
    args={"ig_user_id":"me","limit":100,
          "fields":"id,caption,permalink,timestamp,media_type,media_product_type,like_count,comments_count"}
    if after: args["after"]=after
    res,err=run_composio_tool("INSTAGRAM_GET_IG_USER_MEDIA",args)
    if err: print("ERR",err); break
    data=(res or {}).get("data",{})
    items=data.get("data",[])
    all_items.extend(items)
    after=((data.get("paging",{}) or {}).get("cursors",{}) or {}).get("after")
    pages+=1
    if (not items) or (after==prev) or (not after): break
    prev=after
```

A conta tem ~1200 posts até 2022 — **recortar a janela** (últimos ~6 meses) antes de analisar.

## 3. Medir a aderência (o bloco que não se pula)

`scripts/medir_aderencia.py` no workbench. Saída: os 12 eixos + nota global + tendência mês a
mês + correlação. Ver `references/aderencia.md`.

**Antes de reportar qualquer eixo, imprimir a amostra classificada e conferir com o olho.**
Foi assim que o mascote apareceu como 100% (era o emoji 🐾 da marca) e caiu para 27%.

## 4. Ler a aba do mês na planilha GTM

```python
res,err=run_composio_tool("GOOGLEDRIVE_DOWNLOAD_FILE",
  {"fileId":"16o3nAkTqRBZcCbM4uJsSzbRvtNwt7IuNEGFuGWPGZPk",
   "mime_type":"application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"})
url=res["data"]["downloaded_file_content"]["s3url"]
# baixar e abrir com openpyxl(data_only=True); aba "Ago"/"SET"/...
```

**Estrutura das abas de mês** (validada em Ago/26): bloco à esquerda com FOCO DE PRODUTO e
MIX DE CONTEÚDO (metas %), e à direita o **CALENDÁRIO DIA A DIA** com colunas
`Data | Dia | Comunicação/Conteúdo | Tipo | Observação`. Há também HISTÓRIAS DO MÊS (temas
com peso) e Parking Lot.

**Descoberta central, repetir na conversa com o time:** a aba define **tema e tipo**
(Produto/Educação/Emocional/UGC), **não formato**. Em Ago/26 só 3 dos 31 dias citavam formato,
inline ("CARD", "Vitrine"). Logo: **não há divergência de formato entre GTM e recomendação —
há lacuna.** Proposta permanente ao time: **criar coluna Formato na planilha**.

## 5. Radar + concorrência

Radar mais recente por Gmail (`subject:"Radar de Tendências KLIN"`). Cruzar com os módulos
12-13. Marcar no artifact com 📡 tudo que vier do Radar — o Allan usa isso para saber o que é
dado externo.

## 6. Montar os 3 artifacts

Ver `references/artifacts.md` (estrutura, tokens, esqueleto). Ordem e encadeamento:

1. **De-Para** — republicar na URL fixa; atualizar o placar de aderência com os números novos.
2. **Calendário do mês** — os 30/31 dias, faixa dourada em sex/sáb, "No GTM" no rodapé de cada
   célula. **Manter 100% dos temas**; mudar formato/gancho/ângulo. Preencher lacunas
   ("a definir") com guião pronto dos módulos 04/05.
3. **As peças** — 6-8 peças cobrindo os 3 formatos + a anatomia + tabela de onde os outros
   dias buscam guião.

**Checar o mix antes de publicar:** reels ≥50%, carrossel ~35%, card ≤15%; tipo 40/25/20/15
(Produto/Educação/UGC/Emocional). E que os eixos vermelhos do módulo 16 estejam cobertos.

## 7. Arte final (só se pedirem)

Skill `designer-klin`. Ver `references/pecas.md` §Arte final — inclusive a ressalva de que
**a IA nunca inventa o calçado KLIN** e o custo tem que ser informado no fim.

## 8. Registrar e pushar (obrigatório)

- Módulo novo em `docs/instagram-growth-system/` (numeração contínua; 16=aderência,
  17=calendário ago, 18=peças ago)
- Linha do tempo no `PROGRESSO.md`, com as **decisões e travas** — não só o que foi feito
- Índice no `README.md`
- Commit convencional + push no branch. **Confirmar no remoto** (`git fetch` + `git log origin/...`)
  antes de dizer que foi.

---

## Régua de qualidade da entrega

Antes de mandar, o plano do mês tem que responder:

1. **Quanto do que pedimos já fazemos?** (placar, com número)
2. **O que muda em cada dia, e por quê?** (dado ao lado da recomendação)
3. **Como a peça sai?** (frame, gancho, roteiro, legenda)
4. **O que trava se não decidirem agora?** (prazos que estouram — recrutamento, agenda externa,
   paleta)
5. **O que é dado e o que é aposta?** (rotular; nunca vender correlação como causa)
