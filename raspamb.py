# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
from urllib.request import urlopen
from selenium import webdriver
from selenium.common.exceptions import WebDriverException
import os

def localizar_driver():
    if os.path.isfile('chromedriver') or os.path.isfile('chromedriver.exe'):
        if os.name == 'posix':
            # Retorna o driver nos sistas operacionais posix(ubuntu, etc...)
            return webdriver.Chrome(os.getcwd() + '/chromedriver')
        elif os.name == 'nt':
            # Retorna o driver no sistema operacional windows 
            return webdriver.Chrome(executable_path = os.getcwd() + '\chromedriver.exe')
        else:
            print('Sistema operacional, não reconhecido.')
            print('Envie o resultado abaixo para os desenvolvedores em https://github.com/hirios/raspamb/') 
            print(os.name)
            exit()
    else:
        print('Nao encontrei o driver na mesma pasta do arquivo\nTentarei pela path do sistema')
        return webdriver.Chrome()

def links_zippyshare():
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    # Busca optimizada, retorna uma div com todos os links de todas fontes de download
    busc = soup.find_all('div', class_='servidores-wrapper')
    # txt tem uma parte do html que contem tbm os links dos animes
    txt = str(soup.find_all("li")).split('"')
    lista_links = []
    for c in range(0, len(txt)):
        fim = txt[c].find('zippyshare.com')
        if fim != -1:
            lista_links.append(txt[c])
    if len(lista_links) == 0:
        print('Provavelmente o serviço de download zippyshare não está disponível')
        exit()
    return lista_links

print('A execução do código pode demorar de acordo com a internet')
url = 'https://www.anbient.com/anime/lista'

html = urlopen(url)

bs = BeautifulSoup(html, 'html.parser')

data = bs.find(class_="list")

dat = data.find_all("a")

tv = data.find_all("a", href=True)

# epi = data.find_all("td", {'class':  'epi'})

lista = []

for c in range(0, len(dat)):
    d = dat[c].text
    lista.append(str(d).lower())

cont_erro = 0
while cont_erro == 0:
    anime = input('Nome do anime: ').lower().strip()

    list_animes = []
    num_do_anime = []
    tv_anbient = []

    for c in range(0, len(lista)):
        names = lista[c].find(anime)
        if names != (-1):
            list_animes.append(lista[c])
            num_do_anime.append(c)
            num_do_anime_final = len(num_do_anime)
            tv_anbient.append(tv[c].get('href'))

            cont_erro = len(list_animes)
            if cont_erro > 0:
                print(f'[{num_do_anime_final}] {lista[c].title()}')

    if len(list_animes) == 0:
        print('Certifique-se que o nome está correto!')
        print()

lista_numero_animes = []

for animeszinhos in range(0, len(tv_anbient)):
    lista_numero_animes.append(animeszinhos)

while True:
    try:
        numero = int(input('Digite um número(-1 para sair): '))
        if numero == -1:
            print('Saindo')
            driver.close()
            exit()
        if (numero - 1) in lista_numero_animes:
            link = 'https://www.anbient.com{}'.format(tv_anbient[numero - 1])
            # print(link)
            break
        else:
            print('!!!!Atenção!!!! \nTalvez tenha digitado um numero errado')
    except ValueError:
        print('!!!!! USE APENAS NUMEROS !!!!!!')
    except Exception as e:
        print('Tem outra coisa dando bosta aq')
        print(e)

print('Capturando links dos episódios...')

print('Recomenda-se que o chromedriver esteja na mesma pasta que este script')

try:
    driver = localizar_driver()
    driver.get(link)
except WebDriverException as e:
    print('Ocorreu um erro')
    print(e)
    exit()

lista_links = links_zippyshare()

for i in range(0, len(lista_links)):
    print(f'[{i + 1}] {lista_links[i]}')

while True:

    while True:
        try:
            numero_episodio = int(input('Número do episódio(-1 para sair): '))
            if numero_episodio == -1:
                print('Saindo')
                driver.close()
                exit()
            else:
                link_escolhido = lista_links[numero_episodio - 1]
            break
        except ValueError:
            print('''!!!! Atenção !!!! Erro no número''')

    print('Iniciando o download')
    driver.get(link_escolhido)
    id = driver.page_source
    # driver.close()

    sopa = BeautifulSoup(id, 'html.parser')
    # print(sopa)
    zip_link = sopa.find_all("a", id=True)
    # print(zip_link)
    zip = zip_link[0].get('href')
    picotado = str(link_escolhido).split('/')
    # print(picotado)
    # print(zip)
    driver.get('https://{}{}'.format(picotado[2], zip))
