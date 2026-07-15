# Etapa 7 — Sistema Visual e Prompts de IA

Este documento define a identidade visual do feed @klin_oficial e entrega uma biblioteca de prompts de IA prontos para gerar capas, stills e apoios visuais alinhados à marca Klin — calçados infantis, 43 anos de história, conceito "Caminhar Saudável" 💛🐾. **Como usar:** antes de produzir qualquer peça, consulte a seção 1 (identidade) e a tabela da seção 2 (estilo por pilar); para gerar imagens com IA, copie o prompt da seção 3, substitua as variáveis `{entre_chaves}` e siga as regras de segurança da seção 4. Todo conteúdo gerado por IA publicado deve carregar a marcação "*Conteúdo gerado por IA" (padrão atual da marca).

---

## 1. Identidade visual do feed

### Paleta

| Elemento | Definição | Uso |
|---|---|---|
| Amarelo/dourado Klin 💛 | Cor-assinatura da marca (tom quente, solar) | Overlays de texto, molduras de capa, destaques, fundo de infográficos |
| Tons quentes de apoio | Terracota, areia, madeira clara, verde-folha suave | Cenários, figurinos, props — nunca competem com o amarelo |
| Neutros | Off-white, cinza-quente | Fundos de carrossel, respiro visual |
| Luz natural | Golden hour, janelas, sombra de árvore | Padrão em TODAS as fotos e vídeos — evitar flash duro e luz fria de estúdio |

**Regra de ouro:** o feed deve parecer uma tarde de brincadeira no quintal, não um catálogo. Luz quente > luz branca. Sempre.

### Tipografia de overlays

| Uso | Estilo | Regras |
|---|---|---|
| Texto de gancho (1º segundo do reel) | Sans-serif bold, alto contraste (branco com contorno ou amarelo Klin sobre foto escurecida) | Máx. 8 palavras, corpo grande, zona segura central (evitar bordas cortadas pelo UI do Instagram) |
| Legendas dentro do vídeo | Sans-serif regular, caixa alta e baixa | Legendar 100% das falas (maioria assiste sem som) |
| Números e listas em carrossel | Numeral gigante em amarelo Klin + texto em neutro escuro | 1 ideia por slide |
| Assinatura | Logo Klin pequeno + 🐾 | Canto inferior, nunca no primeiro segundo do reel |

### Enquadramentos

| Formato | Proporção | Uso |
|---|---|---|
| Reels | 9:16 (1080×1920) | Todo vídeo. Zona segura: título no terço superior central, nada de informação nos 250px inferiores (UI do IG) |
| Carrossel | 4:5 (1080×1350) | Todo carrossel educativo/infográfico. Capa com promessa clara + seta/indicador de "arraste" |
| Stories | 9:16 | Elementos interativos (enquete/quiz/slider) no centro-inferior, onde o dedão alcança |

### Composição

- **Regra dos terços:** rosto ou ponto de interesse fora do centro; texto no terço oposto.
- **Pés e chão como protagonistas:** ângulo baixo (câmera na altura do tornozelo), close de pezinhos, sapato tocando grama/terra/piso. É a assinatura visual da Klin.
- **Crianças em movimento:** correndo, pulando, escalando — nunca posadas de forma rígida. Leve motion blur é bem-vindo (transmite "criançar").
- **Profundidade de campo rasa:** fundo desfocado, produto/pé nítido.
- **Câmera "de mãe":** ligeiramente tremida, POV de quem vive a cena. Produção caseira autêntica > produção polida (insight de algoritmo 2026).

---

## 2. Estilo por pilar

| Pilar | Estilo de imagem | Enquadramento | Elementos visuais | Iluminação |
|---|---|---|---|---|
| 1. EDUCATIVO | Demonstrativo e limpo: mãos medindo pé, sola dobrando, comparações lado a lado | Close e plano detalhe; 9:16 reel / 4:5 carrossel | Régua, setas amarelas, texto numerado, split-screen antes/depois | Luz natural difusa (janela), sem sombras duras |
| 2. HUMOR RELATABLE | Cru, estilo "filmei com o celular no caos" | POV, câmera na mão, ângulos improvisados | Bagunça real de casa, expressões genuínas, zoom rápido no detalhe cômico | Luz de casa mesmo — autenticidade > perfeição |
| 3. MASCOTE/TREND | Vibrante e lúdico, energia alta | Plano aberto e médio, mascote sempre inteiro no quadro | Mascote Klin 🐾, crianças interagindo, cenário colorido de loja/evento | Luz forte e alegre, cores saturadas |
| 4. EMOCIONAL | Cinematográfico suave, ritmo lento | Planos abertos + detalhes (mãozinha, primeiro passo); costas e silhuetas | Golden hour, câmera lenta, granulado leve tipo filme, espaços de memória (quintal, casa da avó) | Golden hour obrigatória — contraluz dourada |
| 5. PRODUTO DISFARÇADO | Still de alto padrão dentro de contexto de uso real | Close macro no produto em ação (pé pisando, dobra do solado, etiqueta ECO) | Textura do material, terra/planta (etiqueta ECO), unboxing ASMR | Luz natural quente lateral, realce de textura |
| 6. AUTORIDADE/BASTIDORES | Documental: fábrica, mãos que fazem, processo | Plano médio + detalhes de maquinário e costura | Uniformes, bancadas, matéria-prima, "43 anos" como elemento gráfico | Luz industrial real balanceada para o quente |
| 7. UGC/COMUNIDADE | Conteúdo do cliente: imperfeito, verdadeiro | O que vier — repostar com moldura amarela Klin | Depoimentos em texto sobre foto, prints de comentários, selo "família Klin" | A do cliente (não retocar demais — a imperfeição é a prova) |

---

## 3. Biblioteca de prompts de IA

**Como usar:** copie o bloco, substitua as variáveis `{entre_chaves}`, gere em 9:16 (reels) ou 4:5 (carrossel). Base fotográfica consistente da marca em todos os prompts: `warm golden hour light, candid children playing, soft yellow brand tones, shallow depth of field`. Ao publicar imagem gerada por IA, incluir na legenda: **"*Conteúdo gerado por IA"**.

**Negative prompt padrão (usar em todos):**

```text
Negative prompt: photorealistic identifiable child face, close-up of child's face, creepy, distorted hands, extra fingers, cold blue lighting, studio white background, watermark, text artifacts, plastic skin, oversaturated HDR, adult shoes, logos of other brands
```

### 3.1 Capas de reel educativo

**P01 — Capa: sinais de calçado pequeno**

```text
Photograph-style image, low angle close-up of a toddler's feet in {shoe_color} children's sneakers standing on wooden floor, one shoe slightly worn at the toe, warm golden hour light streaming from a window, soft yellow brand tones, shallow depth of field, candid documentary feel, space at top third for bold text overlay, 9:16 vertical composition
```

**P02 — Capa: teste da flexibilidade**

```text
Close-up photograph of adult hands gently bending a flexible {shoe_color} children's sneaker sole into a curve, demonstrating flexibility test, warm natural window light, soft yellow brand tones, shallow depth of field, clean warm neutral background, negative space on upper third for headline text, 9:16 vertical
```

**P03 — Capa: como medir o pé em casa**

```text
Top-down photograph of a child's bare foot standing on a white paper sheet next to a wooden ruler, parent's hand marking heel position with a pencil, warm golden hour light, cozy home floor background, soft yellow accents, shallow depth of field, instructional yet warm mood, 9:16 vertical composition with headline space at top
```

**P04 — Capa: pisada e sola do tênis**

```text
Macro photograph of the worn sole of a children's sneaker held by adult hands, visible wear patterns on {wear_area}, warm side lighting revealing texture, soft yellow brand tones in background blur, shallow depth of field, forensic-but-warm documentary style, 9:16 vertical, top third free for text
```

### 3.2 Humor POV

**P05 — POV: calçando sapato em criança de 2 anos**

```text
Candid POV photograph from parent's perspective looking down at a wiggling toddler's feet refusing a {shoe_color} sneaker, motion blur on tiny kicking legs, chaotic cozy living room, toys scattered, warm morning window light, soft yellow tones, authentic smartphone-photo aesthetic, humorous everyday parenting moment, child seen from behind/above with face not visible, 9:16 vertical
```

**P06 — POV: rotina da manhã caótica**

```text
Wide candid photograph of a chaotic family morning hallway scene, one child's shoe mid-air, backpack tipping over, cereal bowl on bench, seen from doorway, no identifiable faces (children from behind), warm early morning golden light, soft yellow brand tones, real-life documentary humor, slightly tilted framing like a rushed phone photo, 9:16 vertical
```

**P07 — POV: pai no parquinho**

```text
Action photograph from behind of a dad in casual clothes chasing a small child running across a sunlit playground, both slightly motion-blurred, child wearing bright {shoe_color} sneakers, sandy ground kicked up, warm golden hour light, candid children playing, soft yellow tones, shallow depth of field, joyful exhausted-parent energy, faces not visible, 9:16 vertical
```

### 3.3 Mascote

**P08 — Mascote em cenário de trend**

```text
Cheerful plush mascot character, a friendly cartoon-style yellow-and-brown puppy dog mascot costume, full body in frame, striking a playful {trend_pose} pose in a colorful children's shoe store, kids' sneakers on wooden shelves in background, bright warm lighting, saturated joyful colors with dominant soft yellow brand tones, high-energy fun atmosphere, 9:16 vertical
```

**P09 — Mascote na fábrica**

```text
Documentary-style photograph of a friendly plush puppy dog mascot costume character standing on a shoe factory floor next to stitching machines and rows of colorful children's sneakers in production, wearing a tiny safety vest, warm industrial lighting balanced to golden tones, soft yellow brand palette, playful contrast between cute mascot and real craftsmanship, 9:16 vertical
```

**P10 — Mascote + pegadas 🐾**

```text
Whimsical photograph of yellow paw prints trail across a warm wooden floor leading to a friendly plush puppy mascot peeking from behind a shelf of children's shoes, warm golden hour light from window, soft yellow brand tones, playful treasure-hunt mood, shallow depth of field, space for text along the paw trail, 9:16 vertical
```

### 3.4 Emocional

**P11 — Primeiros passos (golden hour)**

```text
Cinematic photograph of a toddler taking first wobbly steps across a sunlit backyard lawn toward open parent arms, shot from behind the child at ankle height, tiny {shoe_color} first-walker shoes as focal point, warm golden hour backlight creating a soft halo, gentle film grain, candid children playing, soft yellow brand tones, shallow depth of field, nostalgic emotional mood, no visible faces, 9:16 vertical
```

**P12 — Infância passa rápido**

```text
Emotional cinematic photograph of a child's silhouette running through tall golden grass at sunset, arms open wide, small sneakers catching the light, seen from behind, warm golden hour light, gentle lens flare, soft film grain, soft yellow brand tones, evokes fleeting childhood and freedom, plenty of sky negative space for a headline, 9:16 vertical
```

**P13 — Gerações (43 anos)**

```text
Warm nostalgic photograph of two pairs of shoes side by side on a wooden doorstep: vintage 1980s children's leather shoes and a modern colorful kids' sneaker, late afternoon golden light, dust motes in sunbeam, soft yellow tones, shallow depth of field, storytelling composition about generations and legacy, 4:5 vertical
```

### 3.5 Produto / still

**P14 — Still hero de produto**

```text
Premium product still-life photograph of a {product_line} children's sneaker in {shoe_color} placed on warm natural stone surface with scattered autumn leaves, side warm natural light emphasizing material texture and flexible sole, soft yellow brand tones in blurred background, shallow depth of field, editorial catalog quality with organic warmth, 4:5 vertical
```

**P15 — Etiqueta ECO plantável**

```text
Macro photograph of small hands planting a seed-paper shoe tag into a terracotta pot of dark soil, a green sprout emerging nearby, children's sneaker softly blurred in background, warm golden window light, soft yellow and earth tones, shallow depth of field, hopeful sustainability storytelling, hands only with no faces, 4:5 vertical
```

**P16 — Unboxing ASMR (frame de capa)**

```text
Overhead photograph of hands opening a warm yellow shoebox with tissue paper, revealing a brand-new {shoe_color} children's sneaker, seed-paper eco tag visible on laces, warm directional light creating soft shadows, tactile textures emphasized, soft yellow brand tones, cozy anticipation mood, 9:16 vertical with lower third free for caption text
```

### 3.6 Bastidores de fábrica

**P17 — Mãos que fazem (43 anos)**

```text
Documentary photograph of skilled artisan hands stitching a small children's shoe at a factory workbench, leather pieces and tools arranged around, warm tungsten light mixed with daylight, honest craftsmanship mood, 43 years of heritage feel, soft yellow brand accents on materials, shallow depth of field, hands and craft in focus with no identifiable faces, 9:16 vertical
```

**P18 — Linha de produção poética**

```text
Wide documentary photograph of rows of colorful children's sneakers moving along a factory production line, receding into warm depth, morning light through industrial windows, dust particles in light beams, soft yellow brand tones, cinematic scale showing craftsmanship at volume, 9:16 vertical with top third for headline
```

### 3.7 Carrossel infográfico

**P19 — Fundo de capa para carrossel educativo**

```text
Clean warm background image for infographic design: soft off-white textured paper backdrop with subtle yellow watercolor wash on edges, a single children's sneaker and wooden ruler arranged in the lower corner, warm natural light, large empty central area for text and charts, soft yellow brand tones, minimal and inviting, 4:5 vertical
```

**P20 — Fundo: guia de tamanhos por idade**

```text
Flat-lay photograph background of children's shoes in ascending sizes arranged in a gentle arc from baby booties to kids' size sneakers on warm wooden floor, generous negative space above for size chart overlay, warm golden light, soft yellow brand tones, shallow depth of field on edges, growth-journey storytelling, 4:5 vertical
```

**P21 — Fundo: fases 0-2, 2-4, 4-8 anos**

```text
Triptych-style photograph background: three zones on warm neutral surface showing a baby crawling shoe, a toddler first-walker shoe and a kids' running sneaker, evenly spaced with clear space between them for text columns, soft warm side light, soft yellow brand tones, clean instructional composition, 4:5 vertical
```

> **Nota de publicação:** toda imagem gerada com os prompts acima deve levar a marcação **"*Conteúdo gerado por IA"** na legenda ou na própria arte, conforme o padrão atual da marca. Imagens reais de clientes/fábrica não levam a marcação.

---

## 4. Regras de segurança visual

Estas regras são **inegociáveis** e valem para fotos reais, vídeos e imagens geradas por IA:

1. **Dignidade sempre.** Crianças retratadas brincando, aprendendo e sendo cuidadas — nunca em situação vexatória, de choro explorado ou humor à custa da criança. O humor é sobre o caos da rotina dos pais, não sobre a criança.
2. **Proibido rosto hiper-realista de criança gerado por IA.** Nenhum prompt deve gerar rostos infantis identificáveis e fotorrealistas. Preferir sempre: **ângulos de costas, pés, mãos, silhuetas e planos abertos**. Os prompts desta biblioteca já incluem "no visible faces" / "faces not visible" — não remover.
3. **Crianças reais só com autorização.** UGC e fotos de clientes exigem consentimento expresso dos responsáveis antes do repost. Em eventos de loja, priorizar enquadramentos que não identifiquem rostos sem autorização.
4. **Nada de dados que localizem a criança:** sem uniforme escolar identificável, fachada de escola, placas de rua ou nome completo em overlays.
5. **Transparência de IA:** marcar "*Conteúdo gerado por IA" em toda peça gerada, sem exceção.
6. **Coerência com o tom Klin:** nenhuma imagem deve culpabilizar a mãe (ex.: nada de "mãe errada" visual). O contraste educativo é sobre o calçado/situação, nunca sobre quem cuida. 💛
