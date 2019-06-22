from bs4 import BeautifulSoup
from urllib.request import urlopen
from selenium import webdriver


def retorno():
    url = 'https://www.anbient.com/anime/lista'

    html = urlopen(url)

    bs = BeautifulSoup(html, 'html.parser')

    data = bs.find(class_="list")

    dat = data.find_all("a")

    tv = data.find_all("a", href=True)

    # epi = data.find_all("td", {'class': 'epi'})

    le = len(dat)

    lista = []


    for c in range(0, le):
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
        print()

        cont_erro = len(erro)
        if cont_erro > 0:
            pass
        else:
            print('Certifique-se que o nome está correto!')
            print()


    select_anime = len(tv_anbient)
    lista_numero_animes = []

    for animeszinhos in range(0, select_anime):
        lista_numero_animes.append(animeszinhos)


    while True:
        try:
            numero = int(input('Digite um número: '))
            if numero - 1 in lista_numero_animes:
                link = f'https://www.anbient.com{tv_anbient[numero - 1]}'
                break
            else:
                print()
                print('!!!!Atenção!!!! \nTalvez tenha digitado um numero errado')
        except:
            print('!!!!! USE APENAS NUMEROS !!!!!!')
            print()


    print('Capturando links dos episódios...')

    driver = webdriver.Chrome()

    driver.get(link)

    ids = driver.page_source

    soup = BeautifulSoup(ids, 'html.parser')

    busc = soup.find_all("li")

    txt = str(busc).split('"')

    contar_lista_txt = len(txt)

    lista_links = []
    for c in range(0, contar_lista_txt):
        fim = txt[c].find('zippyshare.com')
        if fim != -1:
            lista_links.append(txt[c])
    if len(lista_links) == 0:
        print()
        print('Provavelmente o serviço de download zippyshare não está disponível')
        retorno()

    for empilhados in range(0, len(lista_links)):
        print(f'[{empilhados + 1}] {lista_links[empilhados]}')

    print()
    print()
    
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
        driver.get(f'https://{picotado[2]}{zip}')
retorno()



