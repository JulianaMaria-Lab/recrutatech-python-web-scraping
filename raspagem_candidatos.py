import requests
from bs4 import BeautifulSoup

link = "http://localhost:8000"
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36"}
requisicao = requests.get(link, headers=headers)
site = BeautifulSoup(requisicao.text, "html.parser")
pesquisa = site.findAll("pre")
# print(site.prettify())
print(pesquisa)