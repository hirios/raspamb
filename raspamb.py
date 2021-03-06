import os
import re
import platform
import importlib

def bible(lib):
    try:
        if importlib.import_module(lib):
            return importlib.import_module(lib)
    except:
        try:
            os.system(f'pip install {lib}')
            return importlib.import_module(lib)
        except:
            os.system(f'sudo pip install {lib}')
            return importlib.import_module(lib)
        
requests = bible('requests')
bs4 = bible('bs4')        
selenium = bible('selenium')
from bs4 import BeautifulSoup
from selenium import webdriver
from urllib.request import urlopen
from selenium.common.exceptions import WebDriverException


def drive_download():
    '''
        Esta função é responsavel por localizar a versão mais recente do Chrome Driver na internet e realiza o download
    '''

    version = requests.get("http://chromedriver.storage.googleapis.com/LATEST_RELEASE").text
    
    if platform.system() == "Windows":
        zipp = requests.get(f"https://chromedriver.storage.googleapis.com/{version}/chromedriver_win32.zip")
    else:
        zipp = requests.get(f"https://chromedriver.storage.googleapis.com/{version}/chromedriver_linux64.zip")

    with open("chromedriver.zip", "wb") as r:
        r.write(zipp.content)

    if platform.system() == "Windows":  
        os.system("tar -xf chromedriver.zip")
        os.system("cls")
    else:
        os.system("unzip chromedriver.zip")
        os.system("clear")
    os.remove("chromedriver.zip")


def localizar_driver():
    '''
        Esta função localiza o driver no computador do usuário
    '''

    if os.path.isfile('chromedriver') or os.path.isfile('chromedriver.exe'):
        if os.name == 'posix':
            # Retorna o driver nos sistas operacionais posix(ubuntu, etc...)
            return webdriver.Chrome(os.getcwd() + '/chromedriver')
        elif platform.system() == 'Windows':
            # Retorna o driver no sistema operacional windows
            return webdriver.Chrome(executable_path=os.getcwd() + '\chromedriver.exe')
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
    global lista_com_links
    lista_com_links = []
    for link in soup.find_all(href=re.compile('zippyshare.com')):
        lista_com_links.append(link['href'])
    return lista_com_links


if os.path.isfile("chromedriver.exe") or os.path.isfile("chromedriver") :
    pass
else:
    drive_download()
    

print('A execução do código pode demorar de acordo com a internet\n')
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

def retornar_busca():
    global driver
    global list_animes
    
    quantidade_anime = 0
    list_animes = []
    tv_anbient = []
    while quantidade_anime == 0:
        anime = input('Nome do anime: ').lower().strip()

        for c in range(0, len(lista)):
            names = lista[c].find(anime)
            if names != (-1):
                list_animes.append(lista[c])
                tv_anbient.append(tv[c].get('href'))
                quantidade_anime = len(list_animes)
        if len(list_animes) == 0:
            print('\nCertifique-se que o nome está correto!\n')


    # Imprime a lista de animes
    for i in range(0, len(list_animes)):
        print(f'[{i + 1}] {list_animes[i].title()}')
    print()

    lista_numero_animes = []
    while True:
        try:
            numero = int(input('Digite um número (-1 para voltar): '))

            if numero == -1:
                print()
                retornar_busca()
            if (numero - 1) < len(list_animes):
                link = 'https://www.anbient.com{}'.format(tv_anbient[numero - 1])
                # print(link)
                break
            else:
                print('Numero invalido!!!\n')
                print()
        except ValueError:
            print('!!!!! USE APENAS NUMEROS !!!!!!')
            print()
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
    # Imprime a lista de animes
    print()
    for i in range(0, len(lista_links)):
        print(f'[{i + 1}] {lista_links[i]}')

    while True:
        # Le o numero do episódio que ira baixar
        while True:
            try:
                numero_episodio = int(input('Número do episódio (-1 para voltar): '))
                if numero_episodio == -1:
                    retornar_busca()
                elif numero_episodio <= len(lista_links):
                    link = lista_links[numero_episodio - 1]
                    break
                else:
                    print('Episódio invalido, escolha um numero entre 1 e {}'.format(len(lista_links)))
            except ValueError:
                print('''!!!! Atenção !!!! Erro no número''')

        print('Iniciando o download\n')
        driver.get(link)
        sopa = BeautifulSoup(driver.page_source, 'html.parser')
        zip_link = sopa.find_all("a", id=True)
        zip = zip_link[0].get('href')
        picotado = str(link).split('/')
        episode = 'https://{}{}'.format(picotado[2], zip)
        driver.get(episode)

retornar_busca()
