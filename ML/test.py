import re

import requests
from bs4 import BeautifulSoup

url = 'https://steamcommunity.com/market/listings/730/AWP%20%7C%20Safari%20Mesh%20(Minimal%20Wear)'

html = requests.get(url).text

#scripts = BeautifulSoup(html, 'html.parser').find('script', type="text/javascript")

scripts = BeautifulSoup(html, 'html.parser').find('div')
print(scripts)


# for script in scripts:
#     res = re.search("var line1 = '(.*)'", script.text)
# print(res)