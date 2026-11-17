# Semana 02 - HTML e CSS

## O que foi feito

Portfólio pessoal em HTML e CSS puros, publicado no GitHub Pages, com as seções **Início, Sobre, Habilidades, Projetos e Contato**.

- **HTML semântico:** `header`, `nav`, `main`, `section`, `article` e `footer`, com um único `h1` e hierarquia de títulos sem saltos.
- **CSS externo e organizado** em `css/style.css`, com **variáveis CSS** para cores, fontes, raio e largura máxima.
- **Layout responsivo, mobile first:** o CSS base é a versão de celular (1 coluna), e as media queries acrescentam colunas a partir de 768px e 1024px.
- **Grid** para as grades de habilidades e de projetos e **Flexbox** para o menu, as tags e o conteúdo de cada card.
- **Acessibilidade:** `alt` em todas as imagens, `lang="pt-BR"`, foco visível para navegação por teclado e respeito a `prefers-reduced-motion`.
- **Bônus:** modo escuro automático e transições sutis nos cards e botões.

## Visão única

**Projetos reais, com imagem ampliável sem JavaScript.**

A seção Projetos mostra três projetos que desenvolvi fora da capacitação: a extensão NexusToons Sync, o sistema de fichas do RU e o mod CivilCore. Cada card traz o que o projeto faz, as tecnologias e o link para o código. Os projetos ainda em andamento têm o selo "Em desenvolvimento", e as imagens que não são prints reais estão identificadas como protótipo ou conceito da interface.

Ao clicar numa imagem, ela abre ampliada usando a **Popover API** do HTML: o botão com `popovertarget` abre o elemento com `popover`, e o navegador cuida de fechar com Esc, fechar ao clicar fora e escurecer o fundo (`::backdrop`).

**Onde está no código:**

- `index.html`: cada `article.projeto` tem um `button.projeto-img` e um `div.lightbox` com `popover`.
- `css/style.css`: bloco "Imagem ampliada (Popover)".

O **modo escuro** mostra o valor das variáveis CSS: o bloco `@media (prefers-color-scheme: dark)` só redefine as variáveis, e o site inteiro troca de tema sem repetir nenhuma regra.

## Como rodar

Não precisa instalar nada: abra `semana-02-html-css/index.html` no navegador.

## Link publicado

[lucas-paulino0.github.io/capacitacao-asimov-lucaspaulino/semana-02-html-css/](https://lucas-paulino0.github.io/capacitacao-asimov-lucaspaulino/semana-02-html-css/)

## Dificuldades encontradas

- Ao atualizar o `index.html` por uma versão nova, a tag da minha foto ficou de fora e demorei bastante tempo ate perceber o que tinha acontecido.
- Dois projetos não tinham uma tela pronta para mostrar. Em vez de apresentar uma tela inventada como real, usei imagens identificadas como protótipo e conceito da interface.
