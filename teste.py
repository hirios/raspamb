# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
from urllib.request import urlopen
from selenium import webdriver
from selenium.common.exceptions import WebDriverException
import os

driver = webdriver.Chrome(os.getcwd() + '/chromedriver')
driver.get('https://www.anbient.com/TV/Accel-World')

soup = BeautifulSoup(driver.page_source, 'html.parser')
# busc = soup.find_all("div")
busc = soup.find_all('div', class_='servidores-wrapper')
# print(busc)

arq = open('site2.html', 'w')

for x in busc:
    arq.write(str(x))

arq.close()


# for div in busc:
#     if div["class"] == "servidor  zippyshare active":
#         print(div)

#txt tem uma parte do html que contem tbm os links dos animes
lista_links = []
txt = str(soup.find_all("li")).split('"')

arq = open('txt.html', 'w')

for x in busc:
    arq.write(str(x))

arq.close()

for c in range(0, len(txt)):
    fim = txt[c].find('zippyshare.com')
    if fim != -1:
        lista_links.append(txt[c])
if len(lista_links) == 0:
    print('Provavelmente o serviço de download zippyshare não está disponível')
    exit()

print(txt)

driver.close()
