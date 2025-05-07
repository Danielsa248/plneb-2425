# TPC10 - Web Scraper para a Revista Portuguesa de Medicina Interna

## Descrição

Este script Python realiza a extração de informações da Revista Portuguesa de 
Medicina Interna (RPMI), acessível através do 
site [revista.spmi.pt](https://revista.spmi.pt/index.php/rpmi/issue/archive). 
O programa coleta dados estruturados sobre todas as edições da revista e os seus 
respetivos artigos, incluindo metadados como títulos, autores, DOIs, 
palavras-chave e resumos, guardando tudo em formato JSON.

---

## Funcionalidades

O script possui quatro funções principais:

1. **`procura_pags(link)`**:
   - Gera URLs para as diferentes páginas de arquivo da revista (até 6 páginas)
   - Chama `get_arq()` para cada página

2. **`get_arq(link_arq)`**:
   - Acessa uma página do arquivo da revista
   - Identifica todas as revistas listadas
   - Extrai o link de cada revista e chama `extract_info()` para cada uma

3. **`extract_info(link_pub)`**:
   - Acessa a página de uma revista específica
   - Extrai o título e data da publicação
   - Identifica todos os artigos na publicação
   - Para cada artigo, chama `extract_art_info()` e coleta as informações
   - Armazena os dados no dicionário `INFO`

4. **`extract_art_info(link_art)`**:
   - Acede à página de um artigo específico
   - Extrai metadados do artigo:
     - Título
     - Lista de autores
     - DOI (quando disponível)
     - Palavras-chave (quando disponíveis)
     - Resumo/Abstract (quando disponível)
   - Retorna um dicionário com essas informações

---

## Estrutura dos Dados

O script cria um arquivo JSON com a seguinte estrutura:

```json
{
    "Título da Revista (Volume X Número Y)": {
        "data": "YYYY-MM-DD",
        "artigos": [
            {
                "titulo": "Título do Artigo 1",
                "autores": ["Autor 1", "Autor 2"],
                "doi": "https://doi.org/...",
                "keywords": ["palavra-chave 1", "palavra-chave 2"],
                "abstract": ["Texto do resumo..."]
            },
            {
                "titulo": "Título do Artigo 2",
                ...
            }
        ]
    },
    "Título de Outra Revista": {
        ...
    }
}
```