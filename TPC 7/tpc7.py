from flask import  Flask, request, render_template
import json
import re


app = Flask(__name__)


with open(r'dicionario_medico_.json', encoding='UTF-8') as f:
    db = json.load(f)

@app.route('/')
def hello_world():
    return render_template("home.html")


@app.route('/api/conceitos')
def api_conceitos():
    return db


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


@app.get('/api/conceitos/<designacao>')
def api_conceito(designacao):
    return {"designação":designacao, "descrição": db[designacao]}


@app.post('/api/conceitos')
def adicionar_conceito_api():
    data = request.get_json()
    #{"designacao: descricao}
    db[data["designacao"]] = data["descricao"]

    with open(r'dicionario_medico_.json', 'w', encoding='UTF-8') as f_out:
        json.dump(db, f_out, ensure_ascii=False, indent=4)

    return data


def find_conceito(db: dict, query, word_boundary, case_sensitive):
    res = []

    if word_boundary:
        pattern = r"\b(" + query + r")\b"
    else:
        pattern = "(" + query + ")"

    flags = 0 if case_sensitive else re.IGNORECASE

    for key, value in db.items():
        if re.search(pattern, key, flags) or re.search(pattern, value, flags):
            bold_key = re.sub(pattern, r"<strong>\1</strong>", key, flags)
            bold_value = re.sub(pattern, r"<strong>\1</strong>", value, flags)

            res.append((key, bold_key, bold_value))

    return res


@app.get("/pesquisa")
def pesquisa():
    query = request.args.get('query')
    word_boundary = request.args.get('word_boundary')
    case_sensitive = request.args.get('case_sensitive')

    if not query:
        return render_template("pesquisa.html")

    res = find_conceito(db, query, word_boundary, case_sensitive)
    return render_template("pesquisa.html", conceitos=res, query=query, word_boundary=word_boundary,
                           case_sensitive=case_sensitive, title="Pesquisa")


@app.delete('/conceitos/<designacao>')
def delete_conceito(designacao):
    if designacao in db:
        with open(r'dicionario_medico_.json', "w", encoding='UTF-8') as f_out:
            del db[designacao]
            json.dump(db, f_out, ensure_ascii=False, indent=4)
        return {"message": "Conceito apagado com sucesso!", "redirect_url": "/conceitos", "data": designacao}

    return {"success": False, "message": "Conceito não existe", "data": designacao}


@app.get("/conceitos/tabela")
def conceitos_tabela():
    conceitos = db.items()
    return render_template("tabela.html", conceitos=conceitos, title="Tabela de Conceitos")


if __name__ == '__main__':
    app.run(host="localhost", port=4000, debug=True)
