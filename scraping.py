import requests
from bs4 import BeautifulSoup

url = "https://scrapingclub.com/exercise/list_basic/?page=1"

response = requests.get(url)

soup = BeautifulSoup(response.text, "lxml")

data=soup.find("div", class_="w-full rounded border")

name=data.find("h4", class_="")
print(data)