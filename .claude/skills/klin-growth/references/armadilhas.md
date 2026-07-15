# Armadilhas — erros já cometidos aqui, que não podem se repetir

Cada item abaixo custou retrabalho numa sessão real. Ler antes de reportar número ou publicar peça.

---

## A regra-mãe

**Validar todo classificador por amostra antes de reportar.** Imprimir os itens que o filtro
pegou e conferir com o olho. Um número errado num artifact que vai pro time custa mais caro
que meia hora conferindo.

---

## Medição

### 1. O emoji da marca inflou o mascote de 27% para 100% ⚠️ o pior erro até agora
O padrão de detecção do mascote incluía **🐾** — que é **assinatura de marca em 25 posts**, não
aparição do mascote. Resultado: "mascote = 100% aderente, 28 posts". Com critério estrito
(`mascote`, `aventuras com klin`, `cachorr`, `doguinho`, `peludo`): **7 posts, 0,27/semana, 27%**.
A nota global do placar caiu de 49% para 34%.
**Regra:** emoji de assinatura ≠ conteúdo. Nunca usar 🐾/💛 como sinal de tema.

### 2. Palavra-chave estreita subestima o eixo
A primeira lista de produto só tinha nomes de modelo + "modelo" → 14,4% dos posts. Com termos
amplos (tênis, sandália, sapato, chinelo, bota, calçado, coleção, par, solado, velcro) → **39,7%**.
**Regra:** testar a lista nos dois sentidos — estreita demais subestima, larga demais infla.

### 3. Correlação não é causa
r = 0,74 entre aderência mensal e likes, **n = 7 meses**, e abril (o mais aderente) também teve
Dia das Mães. **Sempre rotular no próprio artifact**: "relação forte, não prova de causa".

### 4. Amostra de 1 não é eixo
"Preço ancorado em valor: 0 de 1 post" — n=1. Reportar o **fato** ("a Liquidação não existe no
feed") em vez de fingir que 0% é uma medida estatística.

### 5. A conta tem ~1200 posts até 2022
`INSTAGRAM_GET_IG_USER_MEDIA` pagina bem além da janela de interesse. **Recortar por data**
antes de analisar, ou os baselines saem contaminados por anos anteriores.

---

## APIs

### 6. `fileId`, não `file_id`
`GOOGLEDRIVE_DOWNLOAD_FILE` exige **`fileId`** (camelCase). Com `file_id` o workbench recusa na
validação. O conteúdo vem em `res["data"]["downloaded_file_content"]["s3url"]` — baixar de lá.

### 7. Nesting do Instagram
Itens em `response.data.data`, paging em `response.data.paging`. Ler o nível errado parece
"export vazio". Persistir só `paging.cursors.after` (o `next` é URL com query sensível).

### 8. O sandbox do workbench reinicia
O `sandbox_id_suffix` muda e o estado se perde. Salvar tudo que importa em `/mnt/files/`.

### 9. `Date.now()`/`Math.random()` não existem em Workflow scripts
(Só relevante se orquestrar por Workflow — quebram o resume.)

---

## Guiões e conteúdo

### 10. Guião citado em dois dias, e errado nos dois
Citei `R01` para 01/08 **e** 27/08. R01 é "sinais de que o calçado ficou pequeno" — que é o
**reel** desse tema. O correto: **01/08 = R22** (primeiros passos) e **27/08 = C02** (o carrossel
equivalente).
**Regra:** ao citar guião, conferir (a) que o ID bate com o formato — **R = reel, C = carrossel** —
e (b) que não se repete no mês.

### 11. O sistema já tem o guião pronto — procurar antes de inventar
R19 (medir o pé) e C02 (7 sinais) saíram inteiros dos módulos 04/05: gancho, roteiro, texto na
tela, B-roll, prompt de capa e legenda. **Sempre varrer os módulos 03-08 antes de escrever
peça nova.**

---

## Arte (designer-klin)

### 12. A IA nunca inventa o calçado KLIN
Regra da skill. Opções: enquadrar sem o calçado como herói, cortar a área dos pés com o card,
ou compor o produto real por cima. **Sempre dizer isso ao entregar arte com foto IA** — a peça
serve para aprovar composição, não para publicar com calçado genérico.

### 13. A IA inventa logo
Uma foto saiu com **rótulo vermelho na lingueta** parecendo marca. Outra saiu com **dedos
vermelhos deformados**. **Inspecionar cada PNG (Read) antes de entregar** — é passo obrigatório
do fluxo, não formalidade. Pedir "plain unbranded, no logos, no brand marks" no prompt.

### 14. Emoji na Gotham vira tofu (▯)
`sub_curto`/`center` desenham direto na fonte, e a Gotham não tem glifo de emoji. Emoji só pelo
helper `emoji()` — que é o que `cta()` e `titulo_hook()` usam.

### 15. O offset de emoji do `titulo_hook` é fixo e encosta na palavra
Com hook longo, o emoji cola na última palavra → "grafismo encostando em letra" reprova.
Solução: tirar o emoji do título; o emoji da peça fica no CTA.

### 16. Posicionamento fixo colide
CTA em `y = H*0.855` colidiu com o subtítulo duas vezes. **Usar o `y` que `titulo_hook()`
devolve** e empilhar a partir dele.

### 17. Copy sobre foto: máx. 2 frases / ~6 palavras
Meu subtítulo tinha 3 frases → reprova. O resto vai para a legenda.

### 18. `capa_conceito` (R7) sai fraca sozinha
Vetorial, **sem logo**, amarelo sobre azul dusty com contraste baixo, sem energia. Para capa de
carrossel educativo, preferir **R4 sobre foto** — e o próprio módulo 05 já traz o prompt de capa
de cada carrossel.

### 19. Preço do flux/dev não está tabelado
`fal_api.py` grava `CONFERIR_PRECO` no `custos_fal.csv`. Referência da skill: ~R$0,15/foto.
**Informar o custo no fim de toda entrega** — e vale tabelar o slug de uma vez.

---

## Entrega

### 20. Reel não tem "arte final"
19 dos 31 dias de agosto são reels. Reel = gravação; o que se gera é **capa + texto na tela**.
Peças 100% estáticas: card e carrossel. **Dizer isso antes de prometer arte do mês inteiro.**

### 21. Republicar, não recriar — os 3 têm URL fixa
De-Para `dec7f5e9-…` · Calendário `1f4d52f4-…` · Peças `76c5225b-…`. Passar `url` no Artifact.
**Criar URL nova quebra o link que o time já salvou** — e como só o Allan opera, o time não tem
como descobrir o link novo sozinho. Errei o desenho na primeira versão: publiquei calendário e
peças como URL do mês, o que obrigaria o Allan a recompartilhar todo mês, para sempre.

### 23. Artifact nasce privado — e a ferramenta não compartilha
Publicar **não** dá acesso a ninguém. O Allan tem que compartilhar pelo menu da própria página,
um por um. Não existe parâmetro de share no Artifact. **Ao publicar artifact novo, avisar.**
É a razão de ser da regra de URL fixa: compartilha uma vez, vale para sempre.

### 24. O time não opera — escrever para quem executa
Só o Allan roda a skill (Composio, push, medição). O time **consome e operacionaliza**: grava e
publica a partir das telas, sem perguntar nada. Gancho, texto na tela, B-roll, legenda, CTA e
trava de produção têm que estar **na página**. O que ficar na conversa não chega em quem grava.

### 22. Confirmar o push no remoto
`git push` silencioso + `git log` local **não provam** que subiu. Fazer `git fetch` e conferir
`origin/<branch>` antes de afirmar.
