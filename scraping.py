import requests
from bs4 import BeautifulSoup

url = "https://scrapingclub.com/exercise/list_basic/?page=1"

response = requests.get(url)

soup = BeautifulSoup(response.text, "lxml")

data=soup.find("div", class_="w-full rounded border")

name=data.find("h4").text.replace ("/n", "")
print (name)

price = data.find ("h5").text

print (price)

url_img = "https://scrapingclub.com" + data.find ("img", class_ = "card-img-top img-fluid").get ("src")
print (url_img)