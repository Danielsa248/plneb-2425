# TPC 8

## Extração de informação de uma página
Este projeto tem como objetivo extrair informação sobre doenças a partir da página Atlas da Saúde. 
Foram desenvolvidas duas funções principais para este fim:


### `doencas_letra(letra)`
Esta função percorre todas as letras do alfabeto e, para cada letra, obtém:

- Nome das doenças disponíveis.
- Link para a página específica de cada doença.
- Resumo da doença.

Para obter informação detalhada de cada doença, a função chama `get_doenca_info(url)`, 
que extrai os dados da página da doença e os retorna num dicionário. Os dados recolhidos 
são armazenados no ficheiro JSON `doencas.json`.


### `get_doenca_info(url)`
Esta função recolhe os detalhes da página da doença indicada no URL. A informação é 
organizada num dicionário com os seguintes campos:

#### Data
A data da página é extraída a partir da divisão com a classe `field-name-post-date`:

```python 
div_content.find('div', class_="field-name-post-date")
```

#### Conteúdo
O conteúdo principal da doença encontra-se na divisão `field-name-body`:

```python 
div_info = div_content.find('div', class_="field-name-body")
```

Os elementos de texto são processados e classificados consoante a sua tag HTML:

- `<p>`: Parágrafos de texto.
- `<div>`: Em alguns casos, os parágrafos estão dentro de `<div>` em vez de `<p>`.
- `<h2>`: Títulos das secções.
- `<ul>`: Listas de informação.
- `<h3>`: Artigos relacionados, guardados como um dicionário (`{nome_do_artigo: url}`).

#### Site
Caso a doença possua um site associado, este é extraído da divisão `field-name-field-site`:

```python
div_content.find('div', class_="field-name-field-site")
```

#### Fonte
Na existência de fonte, o conteúdo é extraído de `field-name-field-fonte`:

```python
div_content.find('div', class_="field-name-field-fonte")
```

#### Nota
Se existir uma nota associada à doença, esta é recolhida da divisão `field-name-field-nota`:

```python
div_content.find('div', class_="field-name-field-nota")
```
