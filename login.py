from bs4 import BeautifulSoup as bs4
from requests import Session
from lxml import html
import Downloader as dw
import requests

import mechanize as mc

class App:

    browser = mc.Browser()

    def login(self, login : str, senha: str) -> bytes:
        self.browser.open("https://www.goodreads.com/user/sign_in?source=home")
        self.browser.select_form(nr = 0)
        self.browser.form['user[email]'] = login
        self.browser.form['user[password]'] = senha
        r  = self.browser.submit()
        return r
    
    def getBrowser(self) -> mc.Browser:
        return self.browser




def getLists(browser: mc.Browser) -> None:

    res =  browser.open("https://www.goodreads.com/rating/voters/173429036?resource_type=Review")
    aux = res.read()
    html2 = bs4(aux, 'html.parser')
    with open("testeLists.html", "w", encoding='utf-8') as file2:
        file2.write( str( html2 ) )




app = App()

app.login("", "")

br = app.getBrowser()

getLists(br)

with open("testeLists.html", "r", encoding='utf8') as file:
    contents = file.read()


bsObj = bs4(contents, "lxml")

aux = open("list.txt", "w", encoding='utf8')

officials  = bsObj.find_all('div', {'class' : 'details'})

for text in officials:
    print(text.get_text())
    aux.write(text.get_text().format())
r
aux.close()
file.close()