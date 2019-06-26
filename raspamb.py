from bs4 import BeautifulSoup
from urllib.request import urlopen
from selenium import webdriver
import os

def retorno():
    url = 'https://www.anbient.com/anime/lista'

    html = urlopen(url) # Demora

    bs = BeautifulSoup(html, 'html.parser')

    data = bs.find(class_="list")

    dat = data.find_all("a")

    tv = data.find_all("a", href=True)

    # epi = data.find_all("td", {'class': 'epi'})

    lista = []

    for c in range(0, len(dat)):
        d = dat[c].text
        lista.append(str(d).lower())

    erro = []
    num_do_anime = []
    tv_anbient = []

    cont_erro = 0
    while cont_erro == 0:
        anime = input('Nome do anime: ').lower().strip()
        print()

        erro = []
        num_do_anime = []
        tv_anbient = []

        for c in range(0, len(lista)):
            names = lista[c].find(anime)
            if names != (-1):
                erro.append(lista[c])
                num_do_anime.append(c)
                num_do_anime_final = len(num_do_anime)
                tv_anbient.append(tv[c].get('href'))

                if len(erro) > 0:
                    print(f'[{num_do_anime_final}] {lista[c].title()}')
                # else:
                #     print(erro[0])

        if len(erro) == 0:
            print('Certifique-se que o nome está correto!')
            print()


    lista_numero_animes = []

    for animeszinhos in range(0, len(tv_anbient)):
        lista_numero_animes.append(animeszinhos)

    while True:
        try:
            numero = int(input('Digite um número: '))
            if (numero - 1) in lista_numero_animes:
                link = 'https://www.anbient.com{}'.format(tv_anbient[numero - 1])
                print(link)
                break
            else:
                print('!!!!Atenção!!!! \nTalvez tenha digitado um numero errado')
        except ValueError:
            print('!!!!! USE APENAS NUMEROS !!!!!!')
        except Exception as e:
            print('Tem outra coisa dando bosta aq')
            print(e)

    print('Capturando links dos episódios...')

    try:
        localDriver = os.getcwd() + '/chromedriver'
        driver = webdriver.Chrome(localDriver)
        driver.get(link)
    except WebDriverExeption as e:
        print('Nao foi possivel acessar o driver!')
        return

    ids = driver.page_source

    soup = BeautifulSoup(ids, 'html.parser')

    busc = soup.find_all("li")

    txt = str(busc).split('"')

    lista_links = []

    for c in range(0, len(txt)):
        fim = txt[c].find('zippyshare.com')
        if fim != -1:
            lista_links.append(txt[c])
    if len(lista_links) == 0:
        print()
        print('Provavelmente o serviço de download zippyshare não está disponível')
        return

    for empilhados in range(0, len(lista_links)):
        print(f'[{empilhados + 1}] {lista_links[empilhados]}')


    while True:

        numero_episodio_pra_baixar = int(input('Número do episódio: '))
        try:
            link_escolhido = lista_links[numero_episodio_pra_baixar - 1]
        except:
            print('''!!!! Atenção !!!!
Erro no número''')
            
            retorno()                        

        driver.get(link_escolhido)
        id = driver.page_source
        # driver.close()

        sopa = BeautifulSoup(id, 'html.parser')
        zip_link = sopa.find_all("a", id=True)
        zip = zip_link[0].get('href')

        picotado = str(link_escolhido).split('/')
        driver.get('https://{picotado[2]}{zip}')

retorno()


