# -*- coding: utf-8 -*-
"""Gera os calendarios de ago/set/out 2026 com gancho e copy por dia."""
import io, os, calendar
SC = os.path.dirname(os.path.abspath(__file__))
CSS = io.open(os.path.join(SC, "_base.css"), encoding="utf-8").read()

# dia, abrev, flags, formato, tipo, guiao, proposta, gancho, copy, gtm
AGO = [
(1,"sáb","⭐ 💰","reel","edu","R22","Guião pronto. A Liquidação, nos últimos dias, entra <b>só na legenda</b> — ancorada em custo-por-uso.","O pé do seu bebê muda TUDO quando ele dá os primeiros passos. E quase ninguém te conta isso.","O pé do seu bebê muda TUDO quando ele dá os primeiros passos — e quase ninguém te conta. 👶 Antes de andar: quase todo cartilagem, com uma gordurinha na sola. É proteção natural.","Dicas: conteúdo a definir, vinculado aos primeiros passos"),
(2,"dom","🐾","carr","prod","","Carrossel salvável: o mascote demonstra o velcro passo a passo. Produto na rotina, zero vitrine.","O segredo pra criança calçar sozinha não é pressa. São 3 passos.","Tem uma idade em que ela quer fazer sozinha — e o velcro é o primeiro treino de autonomia do dia. 💛","Hug — sustentando a educação acima"),
(3,"seg","🔬","reel","edu","R10","Mesmo bastidor de fábrica, com <b>selo IBTeC visível na tela</b>. Abre a série de tecnologia do mês.","43 anos testando o que vai no pé do seu filho.","Quem trabalha há 43 anos com pé de criança sabe de uma coisa que pouca gente sabe: o teste não acaba quando o calçado fica pronto. 🔬","Aquecimento Dia dos Pais: visita à fábrica (bastidor + pais)"),
(4,"ter","","reel","prod","","Ocasião de uso: pai e filho de tênis igual, saindo de casa. Fecha com pergunta.","Tem pai que compra o tênis igual ao do filho. E tem pai que compra o do filho igual ao dele.","Tem pai que compra o tênis igual ao do filho. E tem pai que compra o do filho igual ao dele. 😄 Marca aqui o pai que faria isso.","Tênis Freestyle BCO/Azul e Mel (estilo pai e filho)"),
(5,"qua","🐾 💰","reel","prod","","Teaser com o mascote recebendo a caixa. <b>Último dia de Liquidação</b> — na legenda, valor, nunca só desconto.","Chegou uma caixa na Klin. E não é pra você… ainda.","Chegou uma caixa na Klin. E não é pra você… ainda. 📦 O Klin já tentou abrir três vezes. Dia 10 a gente conta o que tem dentro.","Teaser Lançamento PV27"),
(6,"qui","♿","reel","edu","","<b>A pauta de inclusão do mês.</b> Criança real + fisioterapeuta + o olhar do pai. Mecânica do 464+270.","Ninguém me disse que o primeiro passo dele ia demorar. E ninguém me disse o quanto ia valer.","Ninguém disse pra ele que o primeiro passo ia demorar. E ninguém disse o quanto ia valer. 💛 Tem criança que anda com 11 meses. Tem criança que anda com 3 anos. As duas estão andando.","O olhar de um pai quando o filho dá os primeiros passos / bebê"),
(7,"sex","⭐ 🐾 📡","reel","prod","","Hero de sexta: o mascote apresenta a coleção PV27 na paleta verão 26/27.","O Klin viu a coleção nova antes de você. E não soube guardar segredo.","O Klin viu a coleção nova antes de você. E não soube guardar segredo. 🐾 Rosa Pitaya, Laranja Papaya, Verde Glimmer: o verão chegou na Klin.","Teaser Lançamento PV27"),
(8,"sáb","⭐","reel","emo","","<b>O hero do Dia dos Pais — no sábado, não no domingo.</b> Sábado entrega 96 likes; domingo, 69.","Ele não quer um super-herói. Ele quer você no chão, brincando.","Ele não quer um super-herói. Ele quer você no chão, brincando. 💛 Não é o presente caro. É a segunda vez que você topa jogar a mesma brincadeira.","Conteúdo família MINI — visita à fábrica ou outro"),
(9,"dom","🎯","card","emo","","Card comemorativo — <b>o único card do mês</b>. O peso da data já foi entregue no sábado.","Pai é quem agacha.","Pai é quem agacha. Pra amarrar o cadarço. Pra ficar da altura dele. Pra ver o mundo do tamanho que ele vê. 💛 Feliz Dia dos Pais. 🐾","⭐ DIA DOS PAIS — post emocional principal — CARD"),
(10,"seg","🐾 📡","reel","prod","","Abertura oficial em reel de ocasião de uso, com o mascote apresentando a coleção.","A caixa abriu.","A caixa abriu. 📦 Rosa Pitaya, Laranja Papaya, Verde Glimmer — a coleção PV27 chegou pra viver o verão inteiro. 🐾","Lançamento Oficial Primavera Verão"),
(11,"ter","📡","reel","ugc","","Troca o casal macro por <b>8-10 nano/micro criadoras-mãe</b>. UGC cru. <b>Recrutar em julho.</b>","Deixei ele escolher o próprio look. Foi exatamente o que você está imaginando.","Deixei ele escolher o próprio look. Foi exatamente o que você está imaginando. 😅 E olha: ele não tirou o pé do chão o dia inteiro.","Influenciador — lançamento PV KLIN: Weekend, Walk, Sky (casal)"),
(12,"qua","","carr","prod","","O Weekend em ocasião de uso: onde ele vai, com quem, para quê. Sem 'compre já'.","4 lugares onde esse tênis vai antes de sexta-feira.","4 lugares onde esse tênis vai antes de sexta-feira: escola, parquinho, casa da avó e aquele lugar que ninguém planejou. 💛","Weekend"),
(13,"qui","","reel","ugc","","Reel cru da criadora com o Walk. Sem estúdio, sem locução de marca.","A pergunta que toda mãe faz na hora de comprar: 'mas ele vai querer usar?'","A pergunta que toda mãe faz na hora de comprar: 'mas ele vai querer usar?' 😅 A resposta chegou em vídeo.","UGC de lançamento da coleção PV KLIN: Walk"),
(14,"sex","⭐ 💰","reel","edu","","Hero de sexta, mãe para mãe. <b>Ancorar em durabilidade e custo-por-uso.</b> A camada racional do Radar.","Tênis de criança não precisa ser caro. Precisa ser certo.","Tênis de criança não precisa ser caro. Precisa ser certo. 💛 O que faz o preço valer não é o desconto: é quantas vezes ele sai de casa antes de ficar pequeno.","A correria do dia a dia precisa de calçado confiável"),
(15,"sáb","⭐ 🔬 📱 📡","reel","edu","","<b>A peça mais importante do mês.</b> Dra. Be + demonstração + IBTeC + 'por que o bico largo importa'. <b>Estreia no TikTok.</b>","Seu filho NÃO precisa de tênis ortopédico. (Sim, é uma marca de calçado falando isso.)","Seu filho não precisa de tênis ortopédico. (Sim, é uma marca de calçado falando isso.) Ortopédico é tratamento, indicado por médico. Anatômico é o contrário: não corrige nada, só deixa o pé fazer o trabalho dele. 💛","Série Dra. Be — diferença entre tênis anatômico e ortopédico"),
(16,"dom","","carr","prod","","O Flash em ocasião de uso — carrossel salvável, não vitrine.","Existe um tipo de tênis que a criança calça sem ninguém mandar.","Existe um tipo de tênis que a criança calça sem ninguém mandar. E não é sobre o desenho. 💛","Tênis — Flash (sustentação)"),
(17,"seg","","reel","edu","R19","Guião pronto: tutorial de 30s, ímã de saves.","Você provavelmente está medindo o pé do seu filho errado. (Eu também media.)","Papel, caneta e 30 segundos: é só disso que você precisa pra medir o pé do seu filho em casa. 📏 1️⃣ Folha no chão encostada na parede, criança EM PÉ.","Como medir o pé da criança em casa"),
(18,"ter","","carr","ugc","","Os melhores frames de várias criadoras com o Sky, em carrossel.","6 mães, 6 rotinas, o mesmo tênis.","6 mães, 6 rotinas, o mesmo tênis. 💛 A gente não escolheu as cenas: elas mandaram assim mesmo.","UGC de lançamento da coleção PV KLIN: Sky"),
(19,"qua","","carr","prod","","'O Capri em 5 rotinas' — da escola à festa. Produto dentro da ocasião.","O Capri em 5 rotinas — e nenhuma delas é 'ficar bonito na foto'.","O Capri em 5 rotinas — e nenhuma delas é 'ficar bonito na foto'. 😄 Da escola à festa, sem trocar de sapato no meio do caminho.","Tênis — Capri (sustentação)"),
(20,"qui","","reel","ugc","","Reel de uma das criadoras-mãe do elenco: o dia a dia real, do jeito que ela filma.","Não é conteúdo de marca. É o celular da mãe, numa terça qualquer.","Não é conteúdo de marca. É o celular da mãe, numa terça qualquer. 💛","Influenciador — família usando Klin no dia a dia"),
(21,"sex","⭐ 🔬","reel","edu","R11","Hero de sexta. <b>Nomear o que tem dentro</b>, com teste de flexibilidade filmado. 3ª peça de tecnologia.","Existe um teste de 5 segundos que revela se esse tênis serve pro seu filho.","Existe um teste de 5 segundos que revela se esse tênis serve pro seu filho: dobra. Se não dobra na linha dos dedinhos, trava o passo. 🔬 Palmilha Ultra + SAV, testado IBTeC.","Quando a infância acontece no calçado certo"),
(22,"sáb","⭐ 🐾 🎯","reel","emo","","<b>O mascote encontra o Saci e o Curupira.</b> Território cultural que nenhum concorrente ocupa.","Quem foi que deixou uma pegada só?","Quem foi que deixou uma pegada só? 👀 O Klin passou o Dia do Folclore atrás de duas pistas. Não achou nenhum dos dois — achou coisa melhor: um bando de criança querendo procurar junto. 🐾","Folclore Brasileiro — A Klin é do Brasil 🗓️ Dia do Folclore"),
(23,"dom","","carr","prod","","Mesma peça, <b>sem a vitrine</b>: o Walk dentro de uma rotina de domingo.","Domingo não tem hora pra acabar. O tênis também não devia ter.","Domingo não tem hora pra acabar. O tênis também não devia ter. 💛","Tênis — Walk (lançamento + <b>vitrine</b>)"),
(24,"seg","","carr","ugc","","Repost das criadoras com Freestyle e Capri, em carrossel.","A gente não pediu foto bonita. Pediu foto real.","A gente não pediu foto bonita. Pediu foto real. E olha no que deu. 💛🐾","UGC sustentação: Freestyle BCO/Azul e Mel + Capri"),
(25,"ter","🐾","reel","emo","R06","Episódio do mascote na campanha — a fórmula que fez <b>422 likes</b> na trend da Copa.","POV: até o mascote da Klin entrou na trend.","POV: até o mascote da Klin entrou na trend. 😎 Ele não fala. Mas quando entra em quadro, todo mundo entende. 🐾","Conteúdo divertido da campanha"),
(26,"qua","","carr","prod","","O Capri exclusivo em ocasião de uso + onde encontrar. A exclusividade é a informação.","Esse aqui você não acha em qualquer lugar. E tem um motivo.","Esse aqui você não acha em qualquer lugar — e tem um motivo. 💛 O Capri exclusivo mora nas franquias Klin.","Tênis Capri Exclusivo Franquias — conteúdo do produto"),
(27,"qui","","carr","edu","C02","<b>Lacuna preenchida</b> com guião pronto: 10 slides salváveis, ímã de share.","7 sinais de que o calçado do seu filho ficou pequeno — o nº 4 quase ninguém percebe.","Seu filho não vai te avisar que o sapato apertou — o corpo dele avisa por ele. 👀 Ele tropeça, tira o sapato, fica irritado no passeio. Reunimos os 7 sinais.","Definir conteúdo"),
(28,"sex","⭐ 📡","reel","emo","R25","<b>1º episódio da série 'Cresci de Klin'</b>, montado com os UGCs do concurso de julho.","Guardei o primeiro sapatinho dele numa caixa. Sabe por quê?","Guardei o primeiro sapatinho dele numa caixa. Sabe por quê? 💛 Porque um dia ele vai calçar 40 e eu vou querer lembrar que já coube na minha mão.","Memórias que ficam: o primeiro Klin do seu filho"),
(29,"sáb","⭐","reel","prod","","<b>Sem vitrine:</b> a Tic Tac em reel de ocasião de uso, no sábado. Aposta de lançamento no dia que entrega.","Verão é o único lugar onde o pé pode respirar. Aproveita.","Verão é o único lugar onde o pé pode respirar. Aproveita. ☀️","Papete — Tic Tac (lançamento + <b>vitrine</b>)"),
(30,"dom","","carr","ugc","","Repost dos clientes — Klin na vida real, em carrossel.","Klin na vida real não tem filtro. Tem terra.","Klin na vida real não tem filtro. Tem terra, grama e pressa. 💛🐾","Repost clientes — Klin na vida real"),
(31,"seg","🐾","carr","prod","","O Sky em carrossel de ocasião de uso, com o mascote — fecha o mês e emenda em setembro.","Setembro chega em 24 horas. O pé dele já sabe.","Setembro chega em 24 horas. O pé dele já sabe. 🐾","Conteúdo Sky — lançamento"),
]

SET = [
(1,"ter","","carr","edu","C06","Mantém tema e formato da aba. Só ganha gancho e CTA de salvamento.","5 brincadeiras que desenvolvem seu filho — sem tela e sem gastar nada.","5 brincadeiras que desenvolvem seu filho — sem tela e sem gastar nada. 💛 A nº 3 resolve tarde de chuva.","5 brincadeiras simples que estimulam a criatividade infantil · Carrossel"),
(2,"qua","","carr","prod","C05","Tema e formato mantidos. Ocasião de uso já está na observação da aba.","Cada fase da infância pede um pé diferente. Ninguém te conta qual.","Cada fase da infância pede um pé diferente — e ninguém te conta qual. 👣 0-2, 2-4, 4-8: o que muda, e o que importa em cada uma.","Qual aventura combina com cada fase da infância? · Carrossel · ocasião de uso"),
(3,"qui","","reel","prod","","<b>Card vira reel.</b> Leveza é atributo demonstrável: pesar o Tic Tac na mão vs outro tênis. Card não mostra peso.","Sabe o que acontece com o pé de uma criança dentro de um calçado pesado?","Sabe o que acontece com o pé de uma criança dentro de um calçado pesado? Ela cansa antes, pede colo antes, brinca menos. 💛 O Tic Tac pesa menos que o lanche da escola.","Destaque PV27 + atributo leveza (tic tac) · <b>Card</b>"),
(4,"sex","⭐","reel","ugc","","Hero de sexta, mantido. É o território mãe-para-mãe que a concorrência não ocupa.","Ter o segundo filho não dobra o trabalho. Multiplica.","Ter o segundo filho não dobra o trabalho. Multiplica. 😅 Mas tem uma hora do dia em que os dois brincam juntos e você entende tudo.","Mãe falando sobre a rotina com mais de 1 filho · Reels · rotina com dois, 3 filhos"),
(5,"sáb","⭐","reel","emo","","<b>Carrossel vira reel</b> — é sábado, dia hero, e Dia do Irmão é emoção, não lista.","Irmão é o primeiro amigo. E o primeiro inimigo. Às vezes no mesmo minuto.","Irmão é o primeiro amigo. E o primeiro inimigo. Às vezes no mesmo minuto. 💛 Feliz Dia do Irmão.","Dia do Irmão — a importância da infância compartilhada · <b>Carrossel</b>"),
(6,"dom","","carr","prod","","<b>Card vira carrossel</b> salvável: o feriado em 5 cenas com o New Sport.","Feriado com criança tem duas versões: a que você planejou e a real.","Feriado com criança tem duas versões: a que você planejou e a real. 😄 As duas pedem o mesmo tênis.","Modelo para curtir o feriado com liberdade (new sport) · <b>Card</b>"),
(7,"seg","","reel","emo","","<b>Card vira reel.</b> Independência é movimento — só existe em vídeo.","Ela calçou sozinha. E eu não estava pronta.","Ela calçou sozinha. E eu não estava pronta. 💛 Independência também se aprende brincando — e começa no pé.","Independência também se aprende brincando · <b>Card</b>"),
(8,"ter","","carr","edu","","Tema e formato mantidos. Ganho: gancho contraintuitivo.","Uma marca de calçados pedindo pra deixar seu filho descalço? Sim. E o motivo é sério.","Uma marca de calçados pedindo pra deixar seu filho descalço? Sim — e o motivo é sério. 👣 Brincar livre é o que ensina o pé a ser pé.","Como o brincar livre contribui para o desenvolvimento infantil · Carrossel"),
(9,"qua","","carr","prod","","Mantido. Produto dentro da ocasião, não em vitrine.","As 4 coisas que eu olho ANTES do preço num tênis infantil.","As 4 coisas que eu olho ANTES do preço num tênis infantil. 💛 A 2ª é a que quase ninguém confere na loja.","Destaque de tênis PV27 (capri fem e mas) · Carrossel"),
(10,"qui","","reel","ugc","","Mantido — é a série de mães reais, a melhor aposta do trimestre. <b>Batizar:</b> 'Rotina Real', vinheta de 1s.","Ninguém te conta que o primeiro dia de escola é mais difícil pra você.","Ninguém te conta que o primeiro dia de escola é mais difícil pra você do que pra ele. 💛 Episódio 1 de Rotina Real.","Rotina maternidade real — sono, introdução alimentar, primeiro dia escola · Reels · série de mães"),
(11,"sex","⭐","reel","prod","","Hero de sexta, mantido. Material já pronto da campanha PV27.","Primavera não pede permissão. Chega e manda todo mundo pra rua.","Primavera não pede permissão: chega e manda todo mundo pra rua. 🌼 O Capri já está lá fora.","Capri e outfit: bater tema · Reels · pronto da campanha PV27"),
(12,"sáb","⭐","reel","prod","","<b>Carrossel vira reel</b> — é sábado, e collab com Milon/Stil merece o dia que entrega.","Combinar roupa e calçado de criança em 10 segundos. Vai.","Combinar roupa e calçado de criança em 10 segundos. Vai. ⏱️ Em parceria com @milon e @stil.","Combinações de roupa e calçados (capri) · <b>Carrossel</b> · post collab — milon · stil"),
(13,"dom","","carr","edu","","<b>Card vira carrossel</b> salvável — tema de telas é ímã de save e share.","O tédio também desenvolve criatividade. E a gente rouba isso deles todo dia.","O tédio também desenvolve criatividade — e a gente rouba isso deles todo dia, com a melhor das intenções. 💛","O tédio também desenvolve criatividade? · <b>Card</b> · trazer mais temas de telas"),
(14,"seg","","carr","emo","","Mantido. Aquecimento do Dia do Cliente.","Tem cliente que chegou com um filho. Hoje traz três.","Tem cliente que chegou aqui com um filho. Hoje traz três. 💛 Amanhã a gente conta essas histórias.","Aquecimento Dia do Cliente — memórias construídas juntos · Carrossel"),
(15,"ter","🎯","reel","emo","","Mantido — a aba já pede reel, e a estratégia pede vídeo emocional.","Há 43 anos alguém confia na gente pra cuidar do que ela mais ama.","Há 43 anos alguém confia na gente pra cuidar do que ela mais ama. Obrigado por caminhar com a gente. 💛🐾","Dia do Cliente — Obrigado por caminhar com a gente · Reels"),
(16,"qua","","reel","ugc","","Mantido. <b>Sugestão:</b> virar mini-série de 3 episódios ('um dia de Klin' na fábrica) — PR orgânico.","Ela compra Klin desde que o filho tinha 1 ano. Hoje ele tem 14.","Ela compra Klin desde que o filho tinha 1 ano. Hoje ele tem 14. 💛 Essa é a Kelly — e ela conhece a fábrica por dentro.","Clientes que fazem parte da história da Klin · Reels"),
(17,"qui","🔬","reel","edu","","<b>Carrossel vira reel demonstrável:</b> Dra. Be + criança correndo + teste de estabilidade + <b>selo IBTeC</b>.","Tem uma peça dentro do tênis do seu filho que você nunca viu. E ela decide o passo dele.","Tem uma peça dentro do tênis do seu filho que você nunca viu — e ela decide o passo dele. 🔬 SAV: mais estabilidade pra brincar, correr e explorar. Testado no IBTeC.","Tecnologia SAV: mais estabilidade para brincar, correr e explorar · <b>Carrossel</b>"),
(18,"sex","⭐ 🐾 📡","reel","prod","","Hero de sexta. <b>Mascote como protagonista</b> da campanha + feature filmável: <b>kit de charms/pins</b>.","Faltam 24 dias. E ela já perguntou 40 vezes.","Faltam 24 dias — e ela já perguntou 40 vezes. 🐾 A campanha de Dia das Crianças da Klin começa agora.","Lançamento campanha Dia das Crianças · Reels"),
(19,"sáb","⭐ 🐾","reel","prod","","Hero de sábado, mantido. Segundo dia do lançamento: o mascote conduz.","O Klin não sabe guardar segredo. De novo.","O Klin não sabe guardar segredo. De novo. 🐾 Vem ver o que ele deixou escapar.","Lançamento da campanha · Reels"),
(20,"dom","","reel","prod","","<b>Card vira reel:</b> o Flash é LED. 'Pisou, piscou' não existe em card.","Pisou, piscou. E aí não tem mais volta.","Pisou, piscou. E aí não tem mais volta. ✨ O Flash acende a cada passo — e a criança não quer mais tirar.","Card produto Flash · <b>Card</b>"),
(21,"seg","","reel","edu","","Mantido. Educação de verão com produto integrado.","Meia grossa no calor? Entenda por que essa conta não fecha.","O pé da criança sua três vezes mais que o do adulto. ☀️ Papete e sandália não são só estilo: são respiro.","Sandálias e papetes para os dias mais quentes (tic tac, acqua, hug) · Reels"),
(22,"ter","","carr","prod","","Mantido. Abertura oficial da primavera.","Primavera chegou. E o pé dele quer sair primeiro.","Primavera chegou — e o pé dele quer sair primeiro. 🌼 A coleção PV27 é feita pra isso.","Primavera chegou: coleção PV27 para viver novas descobertas · Carrossel"),
(23,"qua","","reel","ugc","","Mantido. <b>Não disputar o Dia da Menina</b> (data da Pampili) — manter primavera/jardim.","Criança que planta uma semente não esquece mais o que é esperar.","Criança que planta uma semente não esquece mais o que é esperar. 🌱 Comunidade Klin cultivando a primavera.","Comunidade Klin celebrando a primavera educativa · Reels · cultivando o jardim, flores"),
(24,"qui","","carr","edu","","Mantido. Carrossel salvável de benefícios + cuidados.","Brincar na terra faz bem. E não, não é só sujeira.","Brincar na terra faz bem — e não, não é só sujeira. 💛 O que o corpo e a imaginação ganham lá fora.","Brincadeiras ao ar livre: benefícios para corpo e imaginação · Carrossel · benefícios e cuidados"),
(25,"sex","⭐","reel","prod","","<b>Carrossel vira reel</b> — é sexta, dia hero, e a observação da aba já diz 'id dia das crianças'.","O verão inteiro cabe numa sandália e num par de óculos.","O verão inteiro cabe numa sandália e num par de óculos. ☀️ (E na disposição de sair de casa.)","Acqua e óculos — diversão e lúdico · <b>Carrossel</b> · id dia das crianças"),
(26,"sáb","⭐ 📡","reel","ugc","","Hero de sábado. <b>Ampliar para série de 2-3 posts com 3 mães</b> — 'no phone summer' +340% no Radar.","Tirei a tela dela por uma tarde. O que aconteceu depois me assustou.","Tirei a tela dela por uma tarde. O que aconteceu depois me assustou — no bom sentido. 💛 Inspirado em A Geração Ansiosa.","Desafio das telas — mães — inspiração Livro A Geração Ansiosa · Reels · enviar livro pra mãe"),
(27,"dom","","carr","prod","","<b>Card vira carrossel:</b> o Flash em 5 cenas de diversão.","Tem tênis que a criança usa. E tem tênis que ela mostra pros amigos.","Tem tênis que a criança usa — e tem tênis que ela mostra pros amigos. ✨","Diversão, lúdico — Flash · <b>Card</b>"),
(28,"seg","","carr","prod","","<b>Card vira carrossel</b> de ocasião de uso do Capri feminino.","Ela quer o bonito. Você quer o certo. Dá pra ter os dois.","Ela quer o bonito. Você quer o certo. Dá pra ter os dois — e é aí que a conversa acaba em paz. 💛","Capri feminino · <b>Card</b>"),
(29,"ter","🐾","reel","emo","","Mantido — é a <b>volta oficial da série 'Aventuras com Klin'</b> (161-222 likes). Emenda semanal em outubro.","O Klin começou a contagem regressiva. E ele conta errado.","O Klin começou a contagem regressiva pro Dia das Crianças. E ele conta errado. 😄🐾","Contagem regressiva para o Dia das Crianças · Reels · animação do Klin"),
(30,"qua","","carr","edu","","Mantido. Fecha o mês com autonomia — e emenda no presentear de outubro.","Deixar a criança escolher parece perda de tempo. É treino.","Deixar a criança escolher a roupa parece perda de tempo. É treino. 💛 E o primeiro treino de todos é o pé.","Como incentivar a autonomia das crianças nas pequenas escolhas · Carrossel"),
]

OUT = [
(1,"qui","","reel","emo","","Abre o mês com a espera — é literalmente o storytelling da estratégia.","Faltam 11 dias. E ela já perguntou 40 vezes.","Faltam 11 dias — e ela já perguntou 40 vezes. 💛 Tem uma idade em que outubro demora mais que o ano inteiro.","Falar das fases da infância, tocar os pais, campanha emotiva"),
(2,"sex","⭐ 📱","reel","prod","","<b>Flash filmado no escuro</b>, criança correndo ao anoitecer. O LED só existe em vídeo. Nativo de TikTok.","Pisou, piscou. E aí não tem mais volta.","Pisou, piscou — e aí não tem mais volta. ✨ Tem uma hora do dia em que o Flash vira o brinquedo favorito da casa.","FOCO 50%: flash carrinho e flash princesa"),
(3,"sáb","⭐ 🐾","reel","emo","","<b>Volta oficial da série do mascote</b>, ep. 1. Semanal em outubro.","O Klin também está esperando o Dia das Crianças. E ele conta os dias errado.","O Klin também está esperando o Dia das Crianças. E ele conta os dias errado. 😄🐾","—"),
(4,"dom","","carr","edu","C04","Guião pronto: checklist salvável na semana da decisão.","Escolha o presente pelo pé. Não pelo desenho.","Escolha o presente pelo pé — não pelo desenho. 👣 O checklist que evita o presente que fica na caixa.","—"),
(5,"seg","","carr","prod","","Acqua Print + óculos: o kit de verão em ocasião de uso — praia, piscina, quintal.","O verão inteiro cabe numa mochila. Se você souber o que colocar.","O verão inteiro cabe numa mochila — se você souber o que colocar. ☀️","SECUNDÁRIO 30%: acqua print + óculos"),
(6,"ter","","reel","ugc","","Criadora-mãe: humor relatable, cru. O elenco recrutado em julho trabalhando.","O que ele pediu × o que eu comprei.","O que ele pediu × o que eu comprei. 😅 Spoiler: ele usou o meu todo dia.","—"),
(7,"qua","🔬","reel","edu","","Dra. Be: o teste do polegar antes de dar. Nomeia <b>Palmilha Ultra + IBTeC</b>. Tecnologia na semana da compra.","Presente que aperta não é presente.","Presente que aperta não é presente. 💛 Antes de embrulhar, faz o teste do polegar: um dedo de folga na ponta. Se não sobrar, já ficou pequeno.","—"),
(8,"qui","🐾","reel","prod","","Mascote ep. 2: ele pisa, acende, se assusta, pisa de novo. Produto dentro da brincadeira.","O Klin descobriu o Flash. A casa não dorme desde então.","O Klin descobriu o Flash. A casa não dorme desde então. ✨🐾","FOCO 50%: flash princesa"),
(9,"sex","⭐ 💰","reel","prod","","<b>A camada racional na véspera do fim de semana de compra:</b> durabilidade, custo-por-uso, parcelamento.","Quanto custa um presente que dura a infância inteira?","Quanto custa um presente que dura a infância inteira? 💛 Divide pelo número de vezes que ele sai de casa. Aí a conta muda.","Campanha de dia das crianças. Presentear"),
(10,"sáb","⭐ 💰 📡","reel","prod","","<b>O hero de presente do mês.</b> Sábado, pico de compra, 96 likes médios. PINs + combo irmãos.","Ela não quer o tênis. Ela quer o tênis que é só dela.","Ela não quer o tênis — quer o tênis que é só dela. 💛 Com os PINs, cada par vira único. E ninguém troca na escola.","SATÉLITE 20%: acqua kids LED + acqua kids PINs · ALAVANCADOR"),
(11,"dom","","carr","ugc","","Repost das famílias: prova social no domingo, com a compra ainda quente.","O presente chegou. E o pé não saiu mais dele.","O presente chegou — e o pé não saiu mais dele. 💛🐾","Repost Famílias e Clientes"),
(12,"seg","🎯","card","emo","","<b>DIA DAS CRIANÇAS.</b> Card comemorativo, um dos dois do mês. Zero venda: a venda foi no sábado.","Hoje é o dia delas. Aqui, há 43 anos, todo dia é.","Hoje é o dia delas. Aqui, há 43 anos, todo dia é. 💛🐾","A marca que celebra todos os dias o dia das crianças, há 43 anos"),
(13,"ter","","reel","ugc","","<b>O dia seguinte:</b> a criança usando o presente, do jeito que a mãe filmou.","O presente não ficou na caixa. Ficou no pé.","O presente não ficou na caixa. Ficou no pé — e já tem terra. 💛","Repost Famílias e Clientes"),
(14,"qua","","carr","prod","","Abre o HALLOW KLIN e vira a chave para o verão: o mix de sol entra em ocasião de uso.","Outubro tem duas metades. A segunda é a divertida.","Outubro tem duas metades — e a segunda é a divertida. 🎃 O verão chegou na Klin.","HALLOW KLIN · FOCO/SECUNDÁRIO/SATÉLITE: VERÃO"),
(15,"qui","💰","carr","edu","C18","Guião pronto. <b>Ancora valor DEPOIS da compra</b> — quem ganhou o presente quer que ele dure.","Ganhou tênis novo? Tem 3 coisas que fazem ele durar o dobro.","Ganhou tênis novo? Tem 3 coisas que fazem ele durar o dobro — e nenhuma delas é deixar na caixa. 💛","—"),
(16,"sex","⭐ 🐾","reel","emo","","Mascote ep. 3: abre o Halloween pelo humor, não pelo susto.","O Klin escolheu a fantasia. Errou todas.","O Klin escolheu a fantasia. Errou todas. 😄🐾 Ajuda ele nos comentários.","Halloween é momento de brincar e se divertir em família"),
(17,"sáb","⭐ ♿","reel","edu","","<b>A pauta de inclusão do mês</b>, em dia hero. Mecânica do 464+270. Consentimento assinado antes de gravar.","Alguns passos mudam tudo. E os primeiros são sempre os mais longos.","Alguns passos mudam tudo — e os primeiros são sempre os mais longos. 💛 Cada criança tem o seu tempo. Converse sempre com o pediatra. 🩺","—"),
(18,"dom","","carr","prod","","Acqua Kids LED em ocasião de uso — o verão que acende.","O verão também acende.","O verão também acende. ✨☀️","SATÉLITE: acqua kids LED"),
(19,"seg","","reel","ugc","","Criadora-mãe: a rotina real de segunda com o calçado novo.","Segunda-feira com criança não começa. Ela desaba em cima de você.","Segunda-feira com criança não começa — ela desaba em cima de você. 😅 Mas hoje ele calçou sozinho.","Influencer"),
(20,"ter","📡","carr","prod","","<b>PINs: monta o teu.</b> Personalização é a tendência nº 1 do Radar e já é satélite da estratégia.","64% dos pais dizem que o filho quer o que é só dele. Os PINs resolvem isso.","Monta o teu. 💛 Com os PINs, o mesmo modelo vira o tênis que só existe uma vez — o dela.","SATÉLITE: aqua kids PINs"),
(21,"qua","🔬","carr","edu","R24","Segunda peça de tecnologia — a conta passou 6 meses sem nomear nenhuma.","Vira o tênis do seu filho agora e olha a sola. Ela conta uma história.","Vira o tênis do seu filho agora e olha a sola. Ela conta uma história. 👣 3 sinais que revelam como ele pisa.","—"),
(22,"qui","","carr","prod","","Acqua Print: as 5 ocasiões do verão. Produto dentro da cena.","5 lugares onde o verão acontece. Nenhum deles pede sapato fechado.","5 lugares onde o verão acontece — e nenhum deles pede sapato fechado. ☀️","SECUNDÁRIO: acqua print"),
(23,"sex","⭐ 🐾","reel","edu","","Mascote ep. 4. É literalmente a frase da estratégia — 'a Klin ensina a entrar na brincadeira'.","Fantasia boa não se compra. Se inventa com o que tem em casa.","Fantasia boa não se compra — se inventa com o que tem em casa. 🎃 O Klin mostra como. 🐾","A Klin ensina a entrar na brincadeira"),
(24,"sáb","⭐","reel","ugc","","Criadoras: fantasia caseira, feita com a criança. <b>A resposta vira o conteúdo do dia 31.</b>","Fizemos a fantasia dela em 20 minutos. Com caixa de sapato.","Fizemos a fantasia dela em 20 minutos — com caixa de sapato. 🎃 Manda a de vocês que a gente reposta dia 31.","Campanha - Famílias e Clientes"),
(25,"dom","","carr","prod","","O mix de verão completo — o que calçar em cada ocasião de sol.","O verão tem 5 ocasiões. E um pé só.","O verão tem 5 ocasiões — e um pé só. ☀️ O guia pra não errar.","VERÃO"),
(26,"seg","","carr","edu","C06","Guião pronto, versão Halloween. Encaixa no 'no phone summer' (+340% no Radar).","5 brincadeiras de Halloween que não precisam de tela nem de dinheiro.","5 brincadeiras de Halloween que não precisam de tela nem de dinheiro. 🎃 A nº 4 dura a noite inteira.","—"),
(27,"ter","","reel","ugc","","Criadora-mãe: preparando o Halloween em casa, com a criança.","Halloween em casa custa zero. Se a criança ajudar a fazer.","Halloween em casa custa zero — se a criança ajudar a fazer. 🎃","Influencer"),
(28,"qua","📱","reel","prod","","<b>Flash no escuro, versão Halloween.</b> O LED vira a fantasia. Nativo de TikTok.","A melhor fantasia do ano já está no pé dele.","A melhor fantasia do ano já está no pé dele. ✨🎃","Produtos de ocasião"),
(29,"qui","🎯","card","emo","","O <b>'card da data'</b> que a estratégia pede — entregue, e é o segundo e último card do mês.","Feliz Halloween. Ou, como a gente chama aqui: quinta-feira.","Feliz Halloween. Ou, como a gente chama aqui: quinta-feira. 🎃💛","GTM: <b>Cards da data</b>"),
(30,"sex","⭐ 💰","reel","prod","","Véspera. O verão que começa — e a ponte para novembro. <b>Não antecipar desconto</b> (Black Friday abre 06/11).","O verão dura 4 meses. O tênis errado dura 3 semanas.","O verão dura 4 meses. O tênis errado dura 3 semanas. ☀️ A conta é essa.","VERÃO · NOV: YELLOW KLIN abre 06/11"),
(31,"sáb","⭐ 🐾 🎯","reel","emo","","<b>HALLOWEEN — a maior aposta do trimestre.</b> Mascote + fantasia + sábado = a fórmula do 422. Fecha com o repost do dia 24.","O Klin passou o ano inteiro esperando pra usar essa fantasia.","O Klin passou o ano inteiro esperando pra usar essa fantasia. 🎃🐾 E vocês mandaram as de vocês — olha aí.","Momento de se aproximar das famílias"),
]

FMT = {"reel":("f-reel","Reel"),"carr":("f-carr","Carrossel"),"card":("f-card","Card")}
TIP = {"prod":("t-prod","Produto"),"edu":("t-edu","Educação"),"emo":("t-emo","Emocional"),"ugc":("t-ugc","UGC")}


def celula(d, gtm_label):
    dia, ab, flags, fmt, tipo, guiao, prop, gancho, copy, gtm = d
    hero = ab in ("sex", "sáb")
    cls = "cell" + (" band hero" if hero else "")
    fc, fn = FMT[fmt]; tc, tn = TIP[tipo]
    g = f'<span class="g">{guiao}</span>' if guiao else ""
    return f'''    <div class="{cls}">
      <div class="top"><span class="d">{dia:02d}<small>{ab}</small></span><span class="flags">{flags}</span></div>
      <div class="chips"><span class="f {fc}">{fn}</span><span class="t {tc}">{tn}</span>{g}</div>
      <p class="p">{prop}</p>
      <div class="hk"><i>Gancho — falado + na tela nos 2s</i>“{gancho}”</div>
      <div class="cp"><i>Copy — 1ª linha da legenda</i>{copy}</div>
      <div class="gtm"><i>{gtm_label}</i>{gtm}</div>
    </div>
'''


def grade(dados, primeiro_wd, faixas, gtm_label):
    # primeiro_wd: 0=seg ... 6=dom
    out = ['  <div class="grid">']
    for h in ["Seg", "Ter", "Qua", "Qui"]:
        out.append(f'    <div class="hd">{h}</div>')
    out.append('    <div class="hd hero">Sex ⭐</div><div class="hd hero">Sáb ⭐</div><div class="hd">Dom</div>')
    if faixas.get(0):
        out.append(f'    <div class="faixa">{faixas[0]}</div>')
    for _ in range(primeiro_wd):
        out.append('    <div class="cell empty"></div>')
    col = primeiro_wd
    for d in dados:
        if d[0] in faixas and d[0] != 0:
            while col % 7 != 0:
                out.append('    <div class="cell empty"></div>'); col += 1
            out.append(f'    <div class="faixa">{faixas[d[0]]}</div>')
        out.append(celula(d, gtm_label))
        col += 1
    while col % 7 != 0:
        out.append('    <div class="cell empty"></div>'); col += 1
    out.append('  </div>')
    return "\n".join(out)


NAV = '''  <div class="nav">
    <a href="https://claude.ai/code/artifact/{a}" {ca}>Agosto</a>
    <a href="https://claude.ai/code/artifact/{s}" {cs}>Setembro</a>
    <a href="https://claude.ai/code/artifact/{o}" {co}>Outubro</a>
    <a href="https://claude.ai/code/artifact/76c5225b-5260-4b10-95dc-c9bb6163fdf5">As peças</a>
    <a href="https://claude.ai/code/artifact/dec7f5e9-fb08-45ba-b7fe-c215bed1583e">De-Para &amp; aderência</a>
  </div>'''

LEG = '''  <div class="leg">
    <span><b>⭐</b> aposta alta (sex/sáb)</span>
    <span><b>🐾</b> mascote</span>
    <span><b>🔬</b> tecnologia nomeada (IBTeC/SAV/Palmilha)</span>
    <span><b>♿</b> pauta de inclusão</span>
    <span><b>💰</b> preço ancorado em valor</span>
    <span><b>📱</b> TikTok</span>
    <span><b>📡</b> vem do Radar</span>
    <span><b>🎯</b> data especial</span>
    <span>Chip dourado = <b>guião já pronto</b> nos módulos 04/05</span>
  </div>'''


def pagina(titulo, eyebrow, h1, sub, nav, placar, teses, grade_html, leg, extras, foot):
    return f'''<title>{titulo}</title>
<style>
{CSS}</style>

<div class="wrap">
  <div class="eyebrow">{eyebrow}</div>
  <h1>{h1}</h1>
  <p class="sub">{sub}</p>
{nav}
{placar}
{teses}
  <h2>O mês</h2>
  <p class="h2sub">A faixa dourada é sexta e sábado — 101 e 96 likes médios, contra 66 da quarta. Toda aposta alta cai nela. Cada dia traz o <b>gancho</b> (falado e na tela nos 2 primeiros segundos) e a <b>copy</b> (a 1ª linha da legenda, antes do “…ver mais”).</p>
  <div class="cal">
{grade_html}
  </div>
{leg}
{extras}
  <p class="foot">{foot}</p>
</div>
'''
print("modulo carregado")
