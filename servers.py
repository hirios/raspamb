import lxml.html
from pytest import importorskip
import requests
import re 


compilado = re.compile('("[\/A-z0-9\+(%)\-." ]+)')
# (\([1-9 % +]+\))

def zshared(link: str) -> str:
    response = requests.get(link)
    URL = response.url.split('/v')[0]
    parser = lxml.html.fromstring(response.text)

    javascript = parser.xpath('//script[@type="text/javascript"]')[5].text
    javascript = re.search(compilado, javascript).group(0).replace('+ (', '+ str(')
    download_path = eval(javascript)
    return URL + download_path

