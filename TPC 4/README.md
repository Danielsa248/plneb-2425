# TPC 4

## Página HTML

### Página BMW M3


Para o desenvolvimento da página HTML foi necessária
a criação de divisões para estruturar a mesma. Assim
foram criadas a ```<head> e <body>```.

Na ```<head>```, está presente o título do separador da página
tal como o icon da mesma e o link com estilos de fontes
google entre outros aspetos.

Avançando para o ```<body>```, aqui está presente o conteúdo
da página. De forma a organizar o mesmo, foram criadas
três divisões: ```<header>, <main> e <footer>```. 

A ```<header>``` possui dois títulos formando uma espécie de cabeçalho da página.
Para a implementação desses títulos recorreu-se a ```<h1> e <h4>```.

O ```<main>``` é a divisão que possui a informação a ser mostrada ao utilizador.
Assim, precedida por um título ```<h2>``` é criada a divisão ```<div>```
responsável por conter a informação inicial apresentada. Dentro dessa divisão são
ainda criadas outras divisões, uma para cada modelo de carro, para mostrar
a imagem correspondente e a sua legenda através do ```<span>```. Após a 
criação das anteriores, é criada a divisão responsável pela imagem em 
destaque que possui alguma informação sobre o modelo escolhido. Ao interagir com 
o ```<button>``` "See More" dá-se a ativação de uma divisão com informação detalhada extra. 
São criadas divisões, uma para cada modelo, contendo descrição, 
informação extra, fotos, som do motor e um vídeo do YouTube. 
Para demonstrar essa informação recorreu-se a
```<blockquote>, <h3>, <p>, <img>, <audio> e <iframe>```.

Por fim, o ```<footer>``` representa um rodapé com o nome da
disciplina e autor.

Para efeitos de embelezamento da página foram criadas
funções e estilos presentes em script.js e styles.css, respetivamente.