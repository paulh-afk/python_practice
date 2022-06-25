import requests

url = "https://www.gov.uk/search/news-and-communications"
page = requests.get(url)

print(page.content) 