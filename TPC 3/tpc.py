import re



# Abertura e carregamento do ficheiro
with open (r'../../PLN_Aula/aula3/dicionario_medico.txt', encoding='utf-8') as file:
    texto = file.read()


# Limpeza
texto = re.sub(r'((\f+)(?=[a-zÀ-ÖØ-öø-ÿ]))', '', texto) # remove os \f normais que tem nos conceitos
texto = re.sub(r'((\n\f+)(?=[A-Z]))', '', texto) # remove os \n e \f que estão entre os conceitos e a descrição


# Marcar
texto = re.sub(r'(\n\n)', r'\1@', texto)


# Extrair
l_conceitos = re.findall(r'@(.*)\n([^@]*)', texto)

def limpa_descricao(descricao):
    descricao = descricao.strip()
    descricao = re.sub(r'\n', ' ', descricao)
    return descricao

conceitos = [(conceito, limpa_descricao(descricao)) for conceito, descricao in l_conceitos]


# Gerar o HTML
def gera_html(conceitos):
    html_header = '''
                <!DOCTYPE html>
                <head>
                <meta charset="utf-8">
                <title>Dicionário Médico</title>
                </head>
                <body>
                <h1>Dicionário de Conceitos Médicos</h1>
                '''

    html_conceitos = ""

    for conceito, descricao in conceitos:
        html_conceitos += f'''
                        <div>
                        <p><b>{conceito}</b></p>
                        <p>{descricao}</p>
                        </div>
                        <hr/>
                        '''

    html_footer = '''
                <body>
                </html>'''

    return html_header + html_conceitos + html_footer


html = gera_html(conceitos)

with open(r'dicionario_medico.html', 'w', encoding='utf-8') as file:
    file.write(html)
