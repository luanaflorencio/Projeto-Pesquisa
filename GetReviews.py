
from bs4 import BeautifulSoup

with open("Harry.html", "r", encoding='utf8') as file:
    contents = file.read()


bsObj = BeautifulSoup(contents, "lxml")

aux = open("file.txt", "w", encoding='utf8')

officials  = bsObj.find_all('div', {'class' : 'bodycol'})

for text in officials:
    print(text.get_text())
    aux.write(text.get_text().format())

aux.close()
file.close()