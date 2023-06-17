import pandas as pandas
from bs4 import BeautifulSoup
import requests

def jishoDict(Jword):
    html_get_jisho = requests.get('https://jisho.org/search/'+ Jword)

    soup = BeautifulSoup(html_get_jisho.text, features="html.parser")
    words = soup.find_all('span', class_ = 'text')
    counter = 0
    KanjiForWord = []
    for i in words:
        counter = counter + 1
        for j in i:
            if counter == 2:
                for k in j:
                    if k != " ":
                        KanjiForWord.append(k)


    for i in KanjiForWord:
        if i == '\n':
            KanjiForWord.remove(i)

    print( "The kanji for " + Jword + " is: " + "".join(KanjiForWord))
