import lxml.html
import requests
import re
import math


compilado = re.compile('("[\/A-z0-9\+(%)\-." ]+)')
# (\([1-9 % +]+\))


def zshared(link: str) -> str:
    response = requests.get(link)
    URL = response.url.split('/v')[0]
    parser = lxml.html.fromstring(response.text)

    javascript = parser.xpath('//script[@type="text/javascript"]')[5].text
    base = int(javascript.split()[3].replace(';', ''))
    before_path = javascript.split()[-3].split('"')[1]
    after_path = javascript.split()[-2].split('"')[1]
    number_path = str(int(math.pow(base, 3) + 3))

    return URL + before_path + number_path + after_path
    

#breakpoint()
zshared('https://www38.zippyshare.com/v/zHYZqNnZ/file.html')
