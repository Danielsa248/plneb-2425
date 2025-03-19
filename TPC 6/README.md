# TPC 6

## Página de Pesquisa de Termo

Para a implementação de uma página para pesquisa de ocorrências de um termo no dicionário médico
foram desenvolvidas rotas e uma página html.



### Página HTML:

Esta página herda da página pai, ```layout.html``` e possui no seu body um `<form>` e uma `<table>`:

- `<form>`: inclui a barra de pesquisa para inserir o termo a procurar, bem como botões para realizar uma pesquisa 
exata ou parcial.


- `<table>`: apresenta os resultados da pesquisa, organizados em três colunas:
identificador da linha, designação e descrição.  


  
### Rotas:

Na Navbar ou no menu principal, ao clicar no botão de pesquisa, o utilizador é redirecionado 
para a rota `/pesquisar`. Nesta rota, o método `pesquisar_palavra()` é chamado, renderizando o 
template acima descrito. Quando o utilizador realiza a pesquisa, o método `pesquisar()` é acionado. 
Este método procura correspondências no dicionário, verificando tanto as designações como as descrições. 
O comportamento do algoritmo varia conforme o tipo de pesquisa selecionado:  

- **Pesquisa exata**: O algoritmo verifica se a palavra corresponde exatamente à designação ou se está 
presente na descrição. Caso haja correspondência, a palavra é destacada a **negrito**.


- **Pesquisa parcial**: O algoritmo procura ocorrências da palavra dentro da designação ou descrição, 
destacando a parte correspondente a **negrito**.  

