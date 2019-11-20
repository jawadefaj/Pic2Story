#! python3

# https://towardsdatascience.com/how-to-web-scrape-with-python-in-4-minutes-bc49186a8460

import requests
import urllib.request
import time
from bs4 import BeautifulSoup
import glob, os


os.chdir(r"C:\Users\abjaw\Documents\GitHub\Pic2Story\clean\fairytale")
f_target=open("combo.txt", "a+")
for file in glob.glob("*.txt"):
    print(file)
    f_temp = open(file, "r")
    content = f_temp.read()
    f_temp.close()
    f_target.write(content)
f_target.close()
    

# https://www.cs.cmu.edu/~spok/grimmtmp/002.txt

#url = 'https://americanliterature.com/foodie-stories#foodie-stories-for-kids'
#response = requests.get(url)
#soup = BeautifulSoup(response.text, 'html.parser')
#soup.findAll('<li>')
#print(soup)

#write file
#f= open("fairy_tale.txt","a+")
#f.write(soup.get_text())

#f.close()     

#read file
#
#f=open("merged_clean.txt", "r")
#contents = f.read()
#f.close()
#names = contents.split("\n\n\n\n")
#f = open("test_merged.txt", "w+")
#i = int(0)
#for name in names:
#    n = name.split("*")
#    f.write(n[0])
#    i += int(1)
#f.close()

#for name in names:
#    if(name != ""):
#        link_text = name[10:17]
#        story_name = name[19:-5] + '.txt'
#        f = open(story_name, "w+")
#        url = 'https://www.cs.cmu.edu/~spok/grimmtmp/' + link_text
#        response = requests.get(url)
#        soup = BeautifulSoup(response.text, 'html.parser')
#        f.write(soup.get_text())
#        f.close()
#        print(story_name)

