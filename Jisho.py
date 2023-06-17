import pandas as pandas
from bs4 import BeautifulSoup
import requests

def jishoDict(Jword):
    #request the name of the dictionary followed by the Jword, allowing for the URL to be that of word being looked up
    html_get_jisho = requests.get('https://jisho.org/search/'+ Jword)

    #pulls all HTML text from the webpage about the Jword
    soup = BeautifulSoup(html_get_jisho.text, features="html.parser")
    #finds all pieces of text in the HTML code
    words = soup.find_all('span', class_ = 'text')
    counter = 0
    KanjiForWord = []
    #goes through each character in text to check if it is, a space or not. The purpose of the counter is just to get around the fact that every other character in the pure HTML text is seperated by a space.
    for i in words:
        counter = counter + 1
        for j in i:
            if counter == 2:
                for k in j:
                    if k != " ":
                        #adds the individual characters to the list of Kanji or Katakana which compose the Jword.
                        KanjiForWord.append(k)

    #removes some access formatted which is left from the textboxes
    for i in KanjiForWord:
        if i == '\n':
            KanjiForWord.remove(i)
    #output to terminal the kanji or katakana for Jword
    print( "The kanji for " + Jword + " is: " + "".join(KanjiForWord))
