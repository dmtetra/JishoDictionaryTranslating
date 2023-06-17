import pandas as pandas
from bs4 import BeautifulSoup
import requests
from Jisho import jishoDict
#from Tangorin import tangorinDict

while True:

    Jword = input('What word do you want to look up: ')
    jishoDict(Jword)
#tangorinDict(Jword)
