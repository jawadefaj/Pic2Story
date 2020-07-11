#! python3

# https://towardsdatascience.com/how-to-web-scrape-with-python-in-4-minutes-bc49186a8460

import requests
import urllib.request
import time
from bs4 import BeautifulSoup
import glob, os
import csv
import pandas


os.chdir(r"C:\Users\abjaw\Documents\GitHub\Pic2Story\wikipedia-movie-plots")

df = pandas.read_csv('wiki_movie_plots_deduped.csv')
#print(df['Plot'])
temp = ''
f_target=open("combo.txt", "a+")
i = 0
for data in df['Title']:
    #temp += data
    i += 1
    print(data + " >> " + str(i))

# f_target=open("combo.txt", "a+")
# f_target.close()
# os.chdir(r"C:\Users\abjaw\Documents\GitHub\Pic2Story\clean\fairytale")

# for file in glob.glob("*.txt"):
#     print(file) 
    #f_temp = open(file, "r")
    #content = f_temp.read()
    #f_temp.close()
    #f_target.write(content)
#f_target.close()
    

# f_temp = open("merged_clean.txt", "r")
# content = f_temp.read()
# f_temp.close()
# content = content.split('\n\n')
# print(len(content))
# pronoun = ["We", "we", "You", "you", "He", "he", "She", "she", "It",
#            "it", "They", "they", "Him", "him", "Her", "her", "Them", "them"]
# print("Pronoun " + str(len(pronoun)))
# f_write = open("Output.txt", "a+")
# os.chdir(r"C:\Users\abjaw\Documents\GitHub\Pic2Story\clean")

# for temp in content:
#     count = 1
#     number_of_words = temp.split(" ")
#     number_of_stop = temp.count(".")
#     if number_of_stop > 5:
#         print("++ \n")
#         print(temp)

#     if len(temp) > 100:
#         for _pronoun in pronoun:
#             if _pronoun in temp:
#                 count += temp.count(_pronoun)
#         ratio = len(number_of_words) / count
#         print("len " + str(len(number_of_words)) + " ratio " + str(ratio))
#         if ratio < 3:
#             print(temp)
#             print("ratio " + str(ratio))

# f_write.close()


# if '*' in temp:
#     f_write.close()
#     temp = temp.replace("*", "")
#     temp = temp.replace("?", "")
#     temp = temp.replace("\n", "")
#     temp = temp.replace(" ", "")
#     temp = temp + ".txt"
#     print(temp)
#     f_write = open(temp, "a+")
# else:
#     f_write.write(temp + "\n")


# f_target = open("combo.txt", "a+")
# for file in glob.glob("*.txt"):
#     print(file)
#     f_temp = open(file, "r")
#     content = f_temp.read()
#     f_temp.close()
#     f_target.write(content)
# f_target.close()

# https: // www.cs.cmu.edu/~spok/grimmtmp/002.txt

# url = 'https://americanliterature.com/foodie-stories#foodie-stories-for-kids'
# response = requests.get(url)
# soup = BeautifulSoup(response.text, 'html.parser')
# soup.findAll('<li>')
# print(soup)

# write file
# f = open("fairy_tale.txt", "a+")
# f.write(soup.get_text())

# f.close()
# read file

# f = open("merged_clean.txt", "r")
# contents = f.read()
# f.close()
# names = contents.split("\n\n\n\n")
# f = open("test_merged.txt", "w+")
# i = int(0)
# for name in names:
#     n = name.split("*")
#     f.write(n[0])
#     i += int(1)
# f.close()
# for name in names:
#     if(name != ""):
#         link_text = name[10:17]
#         story_name = name[19:-5] + '.txt'
#         f = open(story_name, "w+")
#         url = 'https://www.cs.cmu.edu/~spok/grimmtmp/' + link_text
#         response = requests.get(url)
#         soup = BeautifulSoup(response.text, 'html.parser')
#         f.write(soup.get_text())
#         f.close()
#         print(story_name)
