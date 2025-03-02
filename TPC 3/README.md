# TPC 3


## Extração de conceitos

### Abertura e carregamento do ficheiro
Primeiramente dá-se a abertura do ficheiro previamente transformado em txt.
Na mesma etapa, carrega-se o conteúdo do ficheiro para uma variável.

<br>

#### Limpeza
Como o ficheiro possui '\f' indesejados para a sua manipulação e, por vezes,
'\n\f' extra entre o conceito e a sua descrição, removem-se os carateres indesejados com 
expressões regulares, considerando dois casos distintos.

```python
texto = re.sub(r'((\f+)(?=[a-zÀ-ÖØ-öø-ÿ]))', '', texto)
# remove os \f normais que tem nos conceitos

texto = re.sub(r'((\n\f+)(?=[A-Z]))', '', texto) 
# remove os \n e \f que estão entre os conceitos e a descrição
```

Assim, realizando esta substituição por uma string vazia, iremos contribuir para um maior
simplicidade.

<br>

#### Marcar
Cada conceito é precedido por '\n\n'. Para identificar os conceitos
realiza-se a substituição dos '\n\n' por '\n\n@' marcando o início de cada conceito.

<br>

#### Extrair
Para extrairmos os conceitos e a sua descrição, fazemos uma busca pelo texto limitado entre
@ e a próxima ocorrência do @.

```python
l_conceitos = re.findall(r'@(.*)\n([^@]*)', texto)
```

Os resultados contêm \n desnecessários, que são removidos substituindo-os 
por espaços.

<br>

#### Gerar o HTML
Com os conceitos e descrições limpas e estruturadas, gera-se um ficheiro HTML para a 
visualização do dicionário médico.