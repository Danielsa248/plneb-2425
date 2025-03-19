from flask import  Flask, request, render_template
import json
import re


app = Flask(__name__)


with open(r'dicionario_medico_.json', encoding='UTF-8') as f:
    db = json.load(f)


@app.route('/')
def hello_world():
    return render_template("home.html")


@app.route('/conceitos')
def conceitos():
    designacoes = list(db.keys())

    return render_template("conceitos.html", designacoes=designacoes, title="Lista de Conceitos")


@app.post('/conceitos')
def adicionar_conceito():
    descricao = request.form.get('descricao')
    designacao = request.form.get('designacao')

    db[designacao] = descricao

    with open(r'dicionario_medico_.json', 'w', encoding='UTF-8') as f_out:
        json.dump(db, f_out, ensure_ascii=False, indent=4)

    designacoes = list(db.keys())

    return render_template("conceitos.html", designacoes=designacoes, title="Lista de Conceitos")


@app.route('/conceitos/<designacao>')
def conceito_designacao(designacao):
    descricao = db.get(designacao, "Não foi encontrada uma descrição")

    return render_template("designacao_descricao.html", designacao=designacao, descricao=descricao,
                           title="Designação - Descrição")


@app.route('/pesquisar')
def pesquisar_palavra():
    return render_template('pesquisa.html')


@app.post('/pesquisar')
def pesquisar():
    palavra = request.form.get('palavra').lower()
    tipo_pesquisa = request.form.get('flexRadioDefault')
    resultados = []

    if tipo_pesquisa =="exata":
        for designacao in db.keys():
            if palavra == designacao.lower():
                match = (designacao,  f'<strong>{designacao}</strong>', db[designacao])
                resultados.append(match)
            elif palavra in re.findall(rf'\b{palavra}\b', db[designacao], flags=re.IGNORECASE):
                descricao_destacada = re.sub(rf'\b({palavra})\b', f'<strong>{palavra}</strong>', db[designacao],
                                         flags=re.IGNORECASE)
                match = (designacao, designacao, descricao_destacada)
                resultados.append(match)

    else:
        for designacao in db.keys():
            if palavra in designacao.lower():
                designacao_destacada = re.sub(rf'{palavra}', f'<strong>{palavra}</strong>', designacao,
                                              flags=re.IGNORECASE)
                match = (designacao, designacao_destacada, db[designacao])
                resultados.append(match)
            elif palavra in  db[designacao].lower():
                descricao_destacada = re.sub(rf'{palavra}', f'<strong>{palavra}</strong>', db[designacao],
                                             flags=re.IGNORECASE)
                match = (designacao, designacao, descricao_destacada)
                resultados.append(match)

    return render_template('pesquisa.html', resultados=resultados)


if __name__ == '__main__':
    app.run(host="localhost", port=4000, debug=True)
