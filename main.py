import requests
from bs4 import BeautifulSoup

url = "https://www.gov.uk/search/news-and-communications"
page = requests.get(url)
soup = BeautifulSoup(page.content, "html.parser")

titles = soup.find_all(
    "a", "gem-c-document-list__item-title")

descriptions = soup.find_all("p", "gem-c-document-list__item-description")

# for title in titles:
# print(title.string)

for desc in descriptions:
    print(desc.string)
