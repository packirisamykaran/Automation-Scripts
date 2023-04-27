import requests
from bs4 import BeautifulSoup

URL = "https://www.blockchaingrants.org/"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")


print(page.text)
