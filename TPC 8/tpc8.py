import json
import requests

from bs4 import BeautifulSoup



def get_doenca_info(url):
    link = "https://www.atlasdasaude.pt" + url
    response = requests.get(link)
    html_content = response.text
    soup = BeautifulSoup(html_content, 'html.parser')

    div_content = soup.find('div', class_="node-doencas")

    informacao = {}

    # data
    div_data = div_content.find('div', class_="field-name-post-date")
    if div_data:
        informacao["Data"] = div_data.div.div.text

    # conteudo
    div_info = div_content.find('div', class_="field-name-body")

    if div_info:
        info = {"Descricao": []}
        titulo = "Descricao"

        elem = div_info.find("div", class_="field-item even")

        for item in elem:
            if item.name == 'p' or item.name == 'div':
                info[titulo].append(item.text.replace(" ", " "))

            elif item.name == 'h2':
                titulo = item.text.replace(" ", "").title()
                info[titulo] = []

            elif item.name == 'ul':
                info[titulo].append([i.text for i in item.find_all('li')])

            elif item.name == 'h3':
                if len(info[titulo]) == 0:
                    info[titulo].append({item.text.replace(" ", ""): item.a["href"]})

                else:
                    info[titulo][0] = info[titulo][0] | {item.text.replace(" ", ""): item.a["href"]}


        informacao["Informacao"] = info

    # fonte
    div_fonte = div_content.find('div', class_="field-name-field-fonte")
    if div_fonte:
        informacao["Fonte"] = div_fonte.find('div', class_="field-item even").text

    # site
    div_site = div_content.find('div', class_="field-name-field-site")
    if div_site:
        informacao["Site"] = div_site.find('div', class_="field-item even").text

    # nota
    div_nota = div_content.find('div', class_="field-name-field-nota")
    if div_nota:
        nota = div_nota.find("div", class_= "field-item even").text
        informacao["Nota"] = nota

    return {'Url': link, "Conteudo":informacao}


def doencas_letra(letra):
    response = requests.get("https://www.atlasdasaude.pt/doencasAaZ/" + letra)
    print(f'URL: {response.url}')

    html_content = response.text
    soup = BeautifulSoup(html_content, 'html.parser')

    doencas = {}

    for elem in soup.find_all('div', class_="views-row"):
        designacao = elem.div.h3.a.text.strip()
        doenca_url = elem.div.h3.a['href']
        doenca_info = get_doenca_info(doenca_url)

        desc_div = elem.find("div", class_="views-field-body")
        descricao = desc_div.div.text
        doenca_info["Resumo"] = descricao.strip().replace(" ", " ")
        doencas[designacao] = doenca_info

    return doencas


doencas = {}

for a in range(ord("a"), ord("z") + 1):
    letra = chr(a)
    doencas = doencas | doencas_letra(letra)


with open("doencas.json", "w", encoding="utf-8") as file:
    json.dump(doencas, file, indent=4, ensure_ascii=False)