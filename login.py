from bs4 import BeautifulSoup as bs4
from requests import Session
from lxml import html
#import downloader as dw ############
import requests
from dotenv import load_dotenv
import mechanize as mc
import os


load_dotenv()

class App:

    browser = mc.Browser()

    def login(self, login : str, senha: str) -> bytes:
        self.browser.open("https://www.goodreads.com/user/sign_in")
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


'''
TODO: refatorar
'''
def getGenders(browser : mc.Browser, url: str, name: str) -> None:
    res =  browser.open(url)
    aux = res.read()
    html2 = bs4(aux, 'html.parser')
    with open(name, "w", encoding='utf-8') as file2:
        file2.write( str( html2 ) )
        

def searchGenders( browser : mc.Browser, gender : str , page = 1) -> None:

    url = "https://www.goodreads.com/shelf/show/"+str(gender)+"?page="+str(page)
    res = browser.open(url)

    html = res.read()
    html = bs4( html, "html.parser" )

    pageCount = html.select("div[max_num_pages]")
    pageCount = pageCount[0].select(":not(:last-child)")

    maxPage = int(pageCount[ len(pageCount) -1 ].get_text())
    linkdata = open("links.html", "a")

    for i in range(maxPage + 1):
        if( i >= 1 ):
            print("===> getting page {}\n".format(i))
            url = "https://www.goodreads.com/shelf/show/"+str(gender)+"?page="+str(i)
            res = browser.open(url)

            html = res.read()
            html = bs4( html, "html.parser" )           
            booklinks = html.find_all('a', {'class' : 'bookTitle'})

            for link in booklinks:
                linkdata.write( "<a href='"+ str(url) + str( link['href'] ) +"' ></a>\n")
    
    print("Finalized!")




app = App()
app.login( os.getenv("EMAIL"), os.getenv("SENHA") )
br = app.getBrowser()
query = "programming-language"
searchGenders(br, query)



getLists(br)

with open("testeLists.html", "r", encoding='utf8') as file:
    contents = file.read()


    bsObj = bs4(contents, "lxml")

    aux = open("list.txt", "w", encoding='utf8')

    officials  = bsObj.find_all('div', {'class' : 'leftContainer'})

    for text in officials:
        print(text.get_text())
        aux.write(text.get_text().format())

    aux.close()
    file.close()

