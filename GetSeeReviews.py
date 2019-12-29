
from bs4 import BeautifulSoup

with open("review.html", "r", encoding='utf8') as file:
    contents = file.read()


bsObj = BeautifulSoup(contents, "lxml")

aux = open("file.txt", "w", encoding='utf8')

reviewuser = bsObj.find_all('span', {'class' : 'reviewer'})
date = bsObj.find_all('span' , {'itemprop' : 'datePublished'})
officials  = bsObj.find_all('div', {'class' : 'reviewText mediumText description readable'})
arr = reviewuser + date + officials

for element in arr:
    print(element.get_text())
    aux.write(element.get_text().format())

aux.close()
file.close()