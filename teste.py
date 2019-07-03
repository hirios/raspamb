# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
from urllib.request import urlopen
from selenium import webdriver
from selenium.common.exceptions import WebDriverException
import os
import re

driver = webdriver.Chrome(os.getcwd() + '/chromedriver')
driver.get('https://www.anbient.com/TV/Accel-World')

soup = BeautifulSoup(driver.page_source, 'html.parser')

# arq = open('site.html', 'w')
# arq.write(soup.prettify())
# arq.close()

# busc = soup.find_all('div', class_='servidores-wrapper')

lista_links = []
for c in soup.find_all(href=re.compile('zippyshare.com')):
    lista_links.append(c['href'])

print(lista_links)

# for c in range(0, len(txt)):
#     fim = txt[c].find('zippyshare.com')
#     if fim != -1:
#         lista_links.append(txt[c])
# if len(lista_links) == 0:
#     print('Provavelmente o serviço de download zippyshare não está disponível')
#     exit()
driver.close()
