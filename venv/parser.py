import os, json
from bs4 import BeautifulSoup
import nltk
from nltk import word_tokenize

#def parse(corpusPath):
#    corpus_size = len([direct for direct in os.listdir(corpusPath) if direct.endswith(".txt")])

print(os.listdir("DEV"))
count = 0
for direct in os.listdir("DEV"):
    for i in os.listdir("DEV\\" + direct):
        if i.endswith(".json"):
            count+=1

print(count)