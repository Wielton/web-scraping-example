from bs4 import BeautifulSoup
import requests

url = 'https://www.pro-football-reference.com/'

response = requests.get(url)

page = BeautifulSoup(response.text, 'html')
print(page)