#import pandas as pandas
#rom bs4 import BeautifulSoup
#import requests
#
#def tangorinDict(Jword):
#    print("running tangorin")
#    html_get_tangorin = requests.get('https://tangorin.com/words?search='+ Jword)
#    soup = BeautifulSoup(html_get_tangorin.text, features="html.parser")
#    wordsTangorin = soup.find_all(class_ = "w-jp")
#    print(wordsTangorin)
