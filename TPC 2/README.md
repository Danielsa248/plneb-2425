# TPC 2

## Exercício 1
### Alínea 1.1

Usando o re.match, procuro apenas por ocorrências no início da string.
Assim, como pretendo procurar a palavra "hello" uso: re.match(r'hello, string).


### Alínea 1.2

Usando o re.search, procuro pela primeira ocorrência em qualquer posição da string.
Assim, como pretendo procurar a palavra "hello" uso: re.search(r'hello', string).


### Alínea 1.3

Usando o re.findall, procuro por todas as ocorrências na string.
Assim, como pretendo procurar a palavra "hello", independentemente se é maiúscula
ou minúscula, uso: re.findall(r'hello', string, re.IGNORECASE).


### Alínea 1.4

Como pretendo susbstituir todas as ocorrências da palavras "hello" na string por "*YEP*"
uso re.sub(r'hello', '*YEP*', string, flags = re.IGNORECASE) onde recorro a uma flag
para substituir as palavras com maiúsculas e minúsculas e count = 0 por default para não haver
limite de substituições.


### Alínea 1.5

Para dividir a string por vírgulas uso re.split(r',', string).


## Exercício 2

Uso do pattern "por favor[.!?]$" para procurar "por favor" + sinal de pontuação e $ que
garante que é no final da string.


## Exercício 3

Cria-se uma lista com todas as ocorrências iguais ao termo "eu", daí o uso de '\beu\b'.
Depois calcula-se o comprimento da lista.


## Exercício 4

Uso de re.sub("LEI", novo_curso, linha) para sibstituir todas as ocurrências de "LEI" por string 
no argumento da função.


## Exercício 5

Usámos re.split(",", linha) para separar os números por vírgulas e após tal, percorremos a
lista somando os elementos.


## Exercício 6

Uso o re.findall(r'eu|tu|\bel[ae]\b|nós|vós|\beles\b', linha, flags=re.IGNORECASE) para pesquisar
a ocorrência dos pronomes pessoais independentemente se é maiúscula ou minúscula.


## Exercício 7

Com re.findall(r'[a-zA-Z]\w*', linha) verifico se a string resultante é igual à original.
Caso não seja é porque o nome da variável não é válido.

## Exercício 8

Recorremos ao re.findall(r'(?<![\d.,])\-?\d+(?![\d.,])', linha) onde: 
(?<![\d.,]) garante que antes do número não há "." ou ",",
\-? permite um sinal de menos caso haja,
\d+ captura um dígito ou mais,
(?![\d.,]) garante que depois do número não há um dígito, ponto ou vírgula.


## Exercício 9

Usámos o re.sub(r' +', "*_*", linha) para substituir " " de vários tamanhos apenas por "_".


## Exercício 10

Em cada código da lista cria-se um tuplo com os dois elementos resultantes do split por "-".