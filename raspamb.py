import requests.packages.urllib3.util.connection as urllib3_cn
from urllib.parse import unquote
from vlc import start_stream
from servers import zshared
from thefuzz import fuzz
import lxml.html
import requests
import socket
import base64


def allowed_gai_family():
    return socket.AF_INET


urllib3_cn.allowed_gai_family = allowed_gai_family


def get_index(input_text:str, size: int):
    index = None 

    try:
        index = int(input(input_text)) - 1
    except ValueError:
        pass

    # CASO SEJA PASSADO UMA LETRA
    if index == None:
        print('!! Use apenas números !!')
        return True

    # CASO SEJA USADO -1 PARA VOLTAR
    elif index == -2:
        # break
        return False

    # SE FOR MAIOR QUE SIZE OU MENOR QUE 0
    elif index <= -1 or index >= size:
        print('!! Número inválido !!')
        return True
    
    else:
        return index


def download_episode(download_link: str) -> None:
    print('[+] Iniciando download do episódio...')
    video_content = requests.get(download_link, stream=True)
        
    if 'Content-Disposition' in video_content.headers:
        videoname = video_content.headers['Content-Disposition'].split("'")[-1]
    else:
        videoname = 'anime.mkv'

    with open(videoname, "wb") as r:
        r.write(video_content.content)    
    
    print('[+] Download concluído !!')
    print(f'[+] Download salvo como: {videoname}')


class Raspamb:
    def __init__(self):
        self.URL_ANIMES_LIST = 'https://www.anbient.com/anime/lista'
        self.URL_ANBIENT = 'https://www.anbient.com'

        self.animes_list = self.get_anime_list()

        self.matchs: list[list[str], int] = None
        self.selected: list[str] = None
        self.episodes: list[str] = None


    def get_anime_list(self) -> list[list[str, str]]:        
        response = requests.get(self.URL_ANIMES_LIST)
        parser = lxml.html.fromstring(response.text)
        elements = parser.xpath('//td/a') 
        animes_list = []

        for x in elements:
            href = x.get('href')
            title = x.text
            animes_list.append([title, href])

        return animes_list


    def search(self, anime_name: str) -> None:
        matchs = []
        
        for x in self.animes_list:
            ratio = fuzz.partial_ratio(anime_name, x[0])
            if ratio > 70:
                matchs.append([x, ratio])

        matchs.sort(key = lambda x: x[1], reverse = True)
        self.matchs = matchs


    def select_anime(self) -> None:
        size = len(self.matchs)
        cont = 1 

        for x in self.matchs:
            print([cont], x[0][0])
            cont += 1
        
        while True:
            index = get_index(input_text='\nEscolha o anime: (-1 voltar): ', size=size)  
            
            if type(index) == int:
                self.selected = self.matchs[index][0]
                break

            elif not index:
                return 'continue' 


    def get_episode_list(self) -> None:
        url_of_title = self.URL_ANBIENT + self.selected[1] 
        response_of_title = requests.get(url_of_title)
        parser_of_title = lxml.html.fromstring(response_of_title.text)
        url_base64 = parser_of_title.xpath('//a[@class="ajax padrao"]')[0].get('href')

        url_of_episodes = self.URL_ANBIENT + base64.b64decode(url_base64).decode()

        SERVER = 'zippyshare'
        response_episodes = requests.get(url_of_episodes)
        parser_episodes = lxml.html.fromstring(response_episodes.text)
        
        episodes = parser_episodes.xpath(f'//div[contains(@class, "servidor  {SERVER}") or contains(@class, "servidor  {SERVER} active")]/li/a/@href')

        if len(episodes) == 0:
            print('ERRRROO AO EXTRAIR EPISÓDIOS')
            exit()

        self.episodes = episodes


    def select_episode(self):
        size = len(self.episodes)

        cont = 1 
        for x in self.episodes:
            print([cont], x)
            cont += 1

        while True:
            index = get_index(input_text='\nSelecione o episódio: (-1 voltar): ', size=size)

            if type(index) == int:
                download_link = zshared(self.episodes[index])
                print('\n[+] Direct_Link: ', download_link)
                print('[+] Tentando iniciar strem com VLC')
                if not start_stream(download_link):
                    download_episode(download_link)

            elif not index:
                return 'continue'           


if __name__ == '__main__':
    animes = Raspamb()

    while True:
        anime_name = input('\nDigite um anime: ')
        animes.search(anime_name)

        if animes.select_anime() == 'continue':
            continue

        animes.get_episode_list()
        if animes.select_episode() == 'continue':
            continue


