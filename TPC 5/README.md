# TPC 5

Os dados do dicionário médico sao primeiramente carregados.

Existem duas rotas para mostrar informação diferente ao utilizador:

A primeira rota, ```/conceitos```, ilustra uma lista de todas as designações do dicionário.
Para tal foi necessária a criação de uma template base, layout.html, e uma template filho, conceitos.html.
A template filho herda o estilo da template base e possui uma divisão, no body, onde é percorrida a lista 
de designações para as representar na página html. Cada designação possui uma tag que caso o utilizador carregue
na designação é redirecionado para a página html da segunda rota. A função para gerir a primeira rota
limita-se a atribuir a uma variável a lista de chaves do dicionário que será usada na template conceitos.html.

A segunda rota, ```/conceitos/<designacoes>```, mostra a designação acompanhada pela sua descrição. Para esse
efeito foi criada uma template designacao_descricao.html que herda parâmetros da template base, layout.html.
Esta possui uma divisão, no body, para mostrar a designação e descrição na página. Para o funcionamento da
segunda rota, a função procura no dicionário o value correspondente à key presente na rota.