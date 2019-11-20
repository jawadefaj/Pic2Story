#! python3

# https://towardsdatascience.com/how-to-web-scrape-with-python-in-4-minutes-bc49186a8460

import requests
import urllib.request
import time
from bs4 import BeautifulSoup

# https://www.cs.cmu.edu/~spok/grimmtmp/002.txt

url = 'https://www.cs.cmu.edu/~spok/grimmtmp/001.txt'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
soup.findAll('body')

f= open("fairy_tale.txt","a+")
f.write(soup.get_text() + "+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

f.close()     

#print(soup)