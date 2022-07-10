import requests
from bs4 import BeautifulSoup

url = "https://www.gov.uk/search/news-and-communications"
page = requests.get(url)
soup = BeautifulSoup(page.content, "html.parser")

titles = soup.find_all(
    "a", "gem-c-document-list__item-title")

for title in titles:
    print(title.string)
