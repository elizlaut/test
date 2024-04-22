import requests
from bs4 import BeautifulSoup

url = 'https://www.finam.ru/'
response = requests.get(url)
print(response.status_code)

soup = BeautifulSoup(response.text, "lxml")

data = soup.find_all("div", class_="Item__container--2AY undefined")

for i in data:
    name = i.find("a").text.replace("\n", "")
    print(name)


