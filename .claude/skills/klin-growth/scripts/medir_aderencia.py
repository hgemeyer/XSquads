# -*- coding: utf-8 -*-
"""Mede a aderencia da @klin_oficial aos 12 eixos do de-para (modulo 16).

ONDE RODA: Composio REMOTE_WORKBENCH (usa run_composio_tool, que so existe la).
COMO: colar em celulas; a celula 1 baixa e salva em /mnt/files/klin_media.json.

Saida: notas por eixo, nota global ponderada, tendencia mes a mes e correlacao
aderencia x likes.

ARMADILHA CENTRAL (ja custou retrabalho): NUNCA usar o emoji da marca como sinal
de tema. O padrao de mascote incluia o emoji da pata e deu 100% (era assinatura em
25 posts). Com criterio estrito: 7 posts, 27%. Validar amostra antes de reportar.
"""

# ============ CELULA 1 — baixar =============================================
CELULA_1 = r'''
import json
all_items=[]; after=None; prev=None; pages=0
while pages < 12:
    args={"ig_user_id":"me","limit":100,
          "fields":"id,caption,permalink,timestamp,media_type,media_product_type,like_count,comments_count"}
    if after: args["after"]=after
    res,err=run_composio_tool("INSTAGRAM_GET_IG_USER_MEDIA",args)
    if err: print("ERR",err); break
    data=(res or {}).get("data",{})
    items=data.get("data",[])          # itens em data.data
    all_items.extend(items)
    paging=data.get("paging",{}) or {}
    prev=after
    after=((paging.get("cursors",{}) or {}).get("after"))
    pages+=1
    if (not items) or (after==prev) or (not after): break
print("paginas",pages,"total",len(all_items))
json.dump(all_items,open("/mnt/files/klin_media.json","w",encoding="utf-8"),ensure_ascii=False)
'''

# ============ CELULA 2 — medir ==============================================
CELULA_2 = r'''
import json, re, math, statistics, unicodedata
from collections import Counter
from datetime import datetime, timezone

# >>> AJUSTAR A JANELA A CADA RODADA <<<
INI = datetime(2026,1,14,tzinfo=timezone.utc)
FIM = datetime(2026,7,16,tzinfo=timezone.utc)

items=json.load(open("/mnt/files/klin_media.json",encoding="utf-8"))
def dt(s): return datetime.strptime(s,"%Y-%m-%dT%H:%M:%S%z")
def norm(t):
    t=unicodedata.normalize("NFD",(t or "").lower())
    return "".join(c for c in t if unicodedata.category(c)!="Mn")

P=[i for i in items if INI<=dt(i["timestamp"])<FIM]
P.sort(key=lambda i: dt(i["timestamp"]))
n=len(P); print("posts na janela:",n)

def fmt(i):
    if i.get("media_product_type")=="REELS": return "reel"
    mt=i.get("media_type")
    if mt=="CAROUSEL_ALBUM": return "carrossel"
    if mt=="VIDEO": return "reel"
    return "card"
def has(i,pats):
    t=norm(i.get("caption"))
    return any(re.search(p,t) for p in pats)

# --- classificadores validados (NUNCA por emoji de marca aqui) ---
MASC=[r"\bmascote\b",r"aventuras (com|do) klin",r"aventura com o klin",r"\bklinzinho\b",
      r"\bcachorr",r"\bdoguinho\b",r"\bpeludo\b"]
DIF =[r"\bibtec\b",r"\bsav\b",r"palmilha ultra",r"palmilha"]
INC =[r"inclus",r"sindrome de down",r"\bt21\b",r"autis",r"\btea\b",r"deficien",
      r"fisioterap",r"terapeut"]
PRECO=[r"desconto",r"liquida",r"\boff\b",r"\bpromo",r"\bsale\b",r"\bpreco\b",r"\bparcel"]
VALOR=[r"durab",r"dura a estacao",r"custo por uso",r"dura mais",r"resist",r"qualidade",r"43 anos"]
PROD=[r"\bcapri\b",r"\bhug\b",r"\bsky\b",r"\bweekend\b",r"\bwalk\b",r"\bflash\b",r"\bmatilda\b",
      r"\bmodelo",r"\btenis\b",r"sandalia",r"\bsapato",r"chinelo",r"\bbota\b",r"\bcalcado",
      r"colecao",r"\bpar\b",r"\bsolado\b",r"\bvelcro\b"]

def gancho(i):
    cap=(i.get("caption") or "").strip()
    if not cap: return False
    l1=cap.split("\n")[0].strip(); t=norm(l1)
    return ("?" in l1) or bool(re.match(
        r"^(voce sabia|sabia que|para de|pare de|nunca|3 |5 |7 |o erro|nao |atencao)",t)) \
        or (len(l1)<=60 and l1.isupper())

c=Counter(fmt(i) for i in P)
reel_pct=100*c["reel"]/n; card_pct=100*c["card"]/n; carr_pct=100*c["carrossel"]/n
prod=[i for i in P if has(i,PROD)]; prod_card=len([i for i in prod if fmt(i)=="card"])
ms=[i for i in P if has(i,MASC)]
dif=[i for i in P if has(i,DIF)]
inc_m=sorted({dt(i["timestamp"]).month for i in P if has(i,INC)})
meses=sorted({dt(i["timestamp"]).month for i in P})
g=[i for i in P if gancho(i)]
inf=[i for i in P if re.search(r"@[a-z0-9_.]{3,}", norm(i.get("caption")) or "")]
pr=[i for i in P if has(i,PRECO)]; pr_anc=[i for i in pr if has(i,VALOR)]
semanas=(dt(P[-1]["timestamp"])-dt(P[0]["timestamp"])).days/7
top20=sorted(P,key=lambda i:-(i.get("like_count") or 0))[:20]
hero=len([i for i in top20 if dt(i["timestamp"]).weekday() in (4,5)])

# >>> CONFERIR A AMOSTRA ANTES DE REPORTAR <<<
print("\n--- amostra mascote (conferir com o olho) ---")
for i in ms: print("  ",dt(i["timestamp"]).strftime("%d/%m"),fmt(i),i.get("like_count"),"L",
                   norm(i.get("caption"))[:60])
print("--- amostra tecnologia ---")
for i in dif: print("  ",dt(i["timestamp"]).strftime("%d/%m"),fmt(i),i.get("like_count"),"L",
                    norm(i.get("caption"))[:60])

def mais(a,meta): return max(0,min(100,round(100*a/meta)))
def menos(a,meta): return max(0,min(100,round(100*meta/a))) if a>0 else 100

EIXOS=[
 ("Tecnologia nomeada (IBTeC/SAV/Palmilha)", f"{len(dif)} posts / {len(sorted({dt(i['timestamp']).month for i in dif}))} de {len(meses)} meses",
    mais(len(sorted({dt(i['timestamp']).month for i in dif})), len(meses)), 3),
 ("Mascote 1x/semana", f"{len(ms)} posts / {semanas:.0f} sem = {len(ms)/semanas:.2f}/sem",
    mais(len(ms)/semanas,1), 3),
 ("Gancho na 1a linha", f"{100*len(g)/n:.1f}%", mais(100*len(g)/n,100), 2),
 ("Inclusao 1 pauta/mes", f"{len(inc_m)} de {len(meses)} meses", mais(len(inc_m),len(meses)), 2),
 ("Preco ancorado em valor", f"{len(pr_anc)} de {len(pr)} posts de preco",
    (round(100*len(pr_anc)/len(pr)) if pr else 0), 2),
 ("Influencia nano/micro", f"{len(inf)} posts com @mencao", 0 if len(inf)<8 else 100, 2),
 ("TikTok ativo", "medir fora desta API", 0, 1),
 ("Cards <=15%", f"{card_pct:.1f}%", menos(card_pct,15), 3),
 ("Hero em sex/sab", f"{hero} dos top 20", mais(100*hero/20,100), 2),
 ("Reels >=50%", f"{reel_pct:.1f}%", mais(reel_pct,50), 3),
 ("Produto fora do card-vitrine", f"{prod_card} de {len(prod)} em card",
    round(100*(1-prod_card/len(prod))) if prod else 100, 3),
 ("Carrossel ~35%", f"{carr_pct:.1f}%", menos(carr_pct,35), 1),
]
tot=sum(s*w for _,_,s,w in EIXOS); peso=sum(w for _,_,_,w in EIXOS)
print("\n--- PLACAR ---")
for nome,atual,s,w in EIXOS:
    print(f"{s:3d}% (peso {w}) {nome:42s} {atual}")
print("\nADERENCIA GLOBAL:",round(tot/peso),"%")
print("verde",len([e for e in EIXOS if e[2]>=70]),
      "amarelo",len([e for e in EIXOS if 40<=e[2]<70]),
      "vermelho",len([e for e in EIXOS if e[2]<40]))

# --- engajamento por formato (baseline do artifact) ---
print("\n--- por formato ---")
for f in ["reel","carrossel","card"]:
    s=[i for i in P if fmt(i)==f]
    if s: print(f, len(s), "likes", round(sum(i.get("like_count") or 0 for i in s)/len(s),1),
                "coment", round(sum(i.get("comments_count") or 0 for i in s)/len(s),1))
dias=["seg","ter","qua","qui","sex","sab","dom"]
by=Counter(); tt=Counter()
for i in P:
    d=dt(i["timestamp"]).weekday(); by[d]+=(i.get("like_count") or 0); tt[d]+=1
print("por dia:", {dias[d]: round(by[d]/tt[d],1) for d in sorted(tt)})

# --- tendencia mensal + correlacao ---
print("\n--- mes a mes ---")
linhas=[]
for m in meses:
    mm=[i for i in P if dt(i["timestamp"]).month==m]
    k=len(mm); cm=Counter(fmt(i) for i in mm)
    r=100*cm["reel"]/k; ca=100*cm["card"]/k
    sem_m=len({dt(i["timestamp"]).isocalendar()[1] for i in mm})
    msc=len([i for i in mm if has(i,MASC)])/max(sem_m,1)
    d=len([i for i in mm if has(i,DIF)])
    a=round((mais(r,50)*3 + menos(ca,15)*3 + mais(msc,1)*3 + mais(d,1)*3)/12)
    lk=sum(i.get("like_count") or 0 for i in mm)/k
    linhas.append((m,a,lk)); print(f"{m:02d} n={k:3d} ader {a:3d}% likes {lk:6.1f}")
xs=[l[1] for l in linhas]; ys=[l[2] for l in linhas]
if len(xs)>2:
    mx=statistics.mean(xs); my=statistics.mean(ys)
    cov=sum((x-mx)*(y-my) for x,y in zip(xs,ys))
    den=math.sqrt(sum((x-mx)**2 for x in xs)*sum((y-my)**2 for y in ys))
    if den: print("\ncorrelacao ader x likes: r =",round(cov/den,2),f"(n={len(xs)} meses)")
    print("ROTULAR NO ARTIFACT: relacao forte, NAO prova de causa (n pequeno)")
'''

if __name__ == "__main__":
    print(__doc__)
    print("\n=== CELULA 1 ===", CELULA_1)
    print("\n=== CELULA 2 ===", CELULA_2)
