import json
import requests

from bs4 import BeautifulSoup


LINK = f'https://revista.spmi.pt/index.php/rpmi/issue/archive'
INFO = {}


def procura_pags(link):
    link_pag = link
    for i in range(1, 7):
        if i != 1:
            link_pag = link + f'/{i}'
        get_arq(link_pag)


def get_arq(link_arq):
    response = requests.get(link_arq)
    html_content = response.text
    soup = BeautifulSoup(html_content, 'html.parser')

    ul_pubs = soup.find('ul', class_="issues_archive")

    for pub in ul_pubs.find_all('li'):
        link_pub = pub.a['href']
        extract_info(link_pub)


def extract_info(link_pub):
    response = requests.get(link_pub)
    html_content = response.text
    soup = BeautifulSoup(html_content, 'html.parser')

    content = soup.find('div', class_="page page_issue")

    # Título do revista
    titulo = content.h1.text.strip()

    print(f"A processar: {titulo}")

    # Data da publicação
    data = content.find('div', class_="heading")
    data = data.find('span', class_="value").text.strip()

    seccoes = content.find('div', class_="sections")
    art_infos = []
    artigos = seccoes.find_all('div', class_="obj_article_summary")

    for art in artigos:
        link_art = art.h3.a['href']
        info = extract_art_info(link_art)
        art_infos.append(info)

    INFO[titulo] = {'data': data, 'artigos': art_infos}

def extract_art_info(link_art):
    response = requests.get(link_art)
    html_content = response.text
    soup = BeautifulSoup(html_content, 'html.parser')

    info_art = {}

    content = soup.find('article', class_="obj_article_details")

    # Título do artigo
    titulo = content.h1.text.strip()
    info_art['titulo'] = titulo
    print(f"Artigo: {titulo}")

    info = content.find('div', class_="main_entry")

    # Autores
    aut = []
    autores = info.find_all('span', class_="name")

    for autor in autores:
        aut.append(autor.text.strip())

    info_art['autores'] = aut

    # Doi
    doi = info.find('section', class_="item doi")
    if doi != None:
        doi = doi.a['href']
    info_art['doi'] = doi

    # Keywords
    key = info.find('section', class_="item keywords")
    if key != None:
        k = key.span.text.strip().split(",")
        keys = [ke.replace("\t", "") for ke in k]
        info_art['keywords'] = keys


    abstract = info.find('section', class_="item abstract")
    abs_list = []
    if abstract != None:
        abs = abstract.find_all('p')

        for ab in abs:
            abs_list.append(ab.text.strip().replace("­", ""))

        info_art['abstract']= abs_list

    return info_art


if __name__ == '__main__':
    procura_pags(link=LINK)

    with open('revista.json', 'w', encoding='utf-8') as file:
        json.dump(INFO, file, indent=4, ensure_ascii=False)