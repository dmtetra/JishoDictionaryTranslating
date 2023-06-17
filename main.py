#imports neccessary library
import pandas as pandas 
from bs4 import BeautifulSoup
import requests
#imports the Jisho function from the file jishoDict
from Jisho import jishoDict
#from Tangorin import tangorinDict

#This part of the code will repeat until the program is stopped allowing for multiple words to be translated in a single session
while True:
    #Jword is the varible that stores the name of the word to be looked up
    Jword = input('What word do you want to look up: ')
    #runs jishoDict function
    jishoDict(Jword)
#tangorinDict(Jword)
