import os
import re
import platform
import importlib
from pathlib import Path
import subprocess


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
webdriver_manager = bible('webdriver_manager')
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
from selenium import webdriver
from urllib.request import urlopen
from selenium.common.exceptions import WebDriverException



def popen(cmd):
    startupinfo = subprocess.STARTUPINFO()
    startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
    process = subprocess.Popen(cmd, shell=True, startupinfo=startupinfo, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
    return process.stdout.read()


def get_path_exe(exe_name, thirty_two=True):
    '''
        Retorna a path de um executável
    '''
    path_exe = None
    DISCO = popen('echo %WINDIR%').decode().split(':')[0]

    
    if thirty_two:
    	path_program_files = rf'{DISCO}:\Program Files (x86)'
    else:
    	path_program_files = rf'{DISCO}:\Program Files'


    for path in Path(path_program_files).rglob(exe_name):
    	path_exe = path

    return path_exe


def return_driver():
    '''
        Esta função baixa e retorna o driver no computador do usuário
    '''

    if get_path_exe('chrome.exe', False):
        return webdriver.Chrome(ChromeDriverManager().install())


    if get_path_exe('msedge.exe'):
    	return webdriver.Edge(EdgeChromiumDriverManager().install())


    print("Você precisa ter o Google Chrome ou Edge instalado")
    input("")
    quit()


def links_zippyshare():
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    global lista_com_links
    lista_com_links = []

    for link in soup.find_all(href=re.compile('/zippyshare/')):
        lista_com_links.append(link['href'])

    if len(lista_com_links) == 0:
        for link in soup.find_all(href=re.compile('zippyshare.com')):
            lista_com_links.append(link['href'])

    return lista_com_links


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
        driver = return_driver()
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
        episode = driver.find_element_by_xpath('//a[@id="dlbutton"]').get_attribute('href')


        # path_vlc = get_path_exe("vlc.exe", False)
        # if path_vlc:
        # 	popen(f'"{path_vlc}" {episode}')

        driver.get(episode)

retornar_busca()
