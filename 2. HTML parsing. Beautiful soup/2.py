# https://spb.hh.ru/vacancies/data-scientist

import requests
from bs4 import BeautifulSoup as BS
from pprint import pprint

url = 'https://spb.hh.ru'

suffix = '/vacancies/data-scientist'

response = requests.get(url+suffix)
headers = {'User-agent': 'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2224.3 Safari/537.36'}

dom = BS(response.text, 'html.parser')

1/23/36

