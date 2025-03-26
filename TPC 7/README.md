# TPC 7


### Navbar:

Para adicionar a página da tabela de designações - descrições à Navbar, foi adicionado o 
seguinte código ao ficheiro ``layout.html``:

``<a class="nav-link" href="/conceitos/tabela">Tabela</a>``.


### Estilo da tabela:

Para embelezar a tabela de designações - descrições, no ``tabela.html`` foi usado:

```
<style>
#tabela_conceitos tr:hover {
    --bs-table-hover-bg: purple;
}

#tabela_conceitos tr:hover td,
    #tabela_conceitos tr:hover td a {
        color: white;
}
</style>

<table id="tabela_conceitos" class="table table-striped table-bordered table-hover">
```


### Regex Search:

Para permitir a pesquisa com expressões regulares (regex) na tabela de designações - descrições, 
foi adicionada a seguinte configuração no arquivo ``conceito.js``:

```
{
search: {
    regex: true
    }
}
```

### Extra
Foi adicionada a feature de carregar na designação e ser redirecionado para a página da designação e 
respetiva descrição.