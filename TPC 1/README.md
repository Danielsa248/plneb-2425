# TPC 1

### Exercício 1

Nesta alínea para ler a string ao contrário de forma simples optei por a ler começando do fim para o início.
Outra forma de fazer o mesmo é revertendo a string e depois dar join (linha comentada).


### Exercício 2

Para contar o número de a's e de A's é preciso percorrer a string através de um ciclo
e quando o caracter for igual à letra que pretendemos contar incrementamos no contador específico


### Exercício 3

É criada uma lista com todas as vogais existentes e possível acentuação. 
Percorre-se a string em letras minúsculas para poder comparar com a lista. 
Caso o caracter seja igual a um elementa na lista, significa que é uma vogal 
e o contador aumenta uma unidade.


### Exercício 4

Usando o .lower() a string é convertida para letras minúsculas.


### Exercício 5

Usando o .upper() a string é convertida para letras maiúsculas.


### Exercício 6

Cria-se uma cópia inversa da string passada como argumento e depois comparam-se as strings.
Caso sejam iguais é porque a string original é uma capicua.


### Exercício 7

A string 1 é percorrida e é verificado se cada caracter está presente na string 2.
Caso exista algum caracter que não esteja presente na string 2, as string não estão balanceadas.
Caso os carcteres estejam em tamanhos diferentes (maiúsculo e minúsculo) ou com acentuação diferente,
a comparação resultará em False ('E' diferente de 'e' / 'à' diferente de 'á')



### Exercício 8

A string 2 é percorrida com um ciclo até ao último caracter onde ainda há a possíbilidade
de ter um conjunto igual à string 1. Na procura de ocurrências, é comparado, na string 2,
desde o caracter com índice atual no ciclo até ao caracter que distancia do mesmo uma distância
igual ao tamanho da string 1.


### Exercício 9

As letras de cada palavra são ordenadas alfabeticamente e depois comparadas. Caso as palavras
sejam anagramas, as listas com as letras ordenadas terão de ser iguais.


### Exercício 10

Neste exercício percorro a lista de palavras e para cada palavra ordeno alfabeticamente as
letras. É verificado se essa palavra ordenada já existe como key no dicionário. Caso a 
palavra ordenada seja igual a uma key existente, a palavra original será associada 
a essa key. Caso contrário, é criada uma key com o value igual à palavra original. Assim, 
teremos um dicionário que representa uma tabela de anagramas onde as keys 
são as letras organizadas e os values correspondentes uma lista com as palavras no formato
original que são anagramas entre si.