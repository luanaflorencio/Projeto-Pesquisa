from bs4 import BeautifulSoup
import os
import Downloader
import GetSeeReviews 

#Passa-se o nome do arquivo html baixado 
def downloadCompleteReview(filename):
    with open(filename, "r", encoding='utf8') as file:
        contents = file.read()

    bsObj = BeautifulSoup(contents, "lxml")

    var = bsObj.find_all("a", string="see review")
    url_base = "https://www.goodreads.com"

    i = 0
    os.mkdir('comments')
    for tag in var:
        endereco = 'comments/'+str(i)
        os.mkdir(endereco)
        url = url_base + tag['href']
        a = Downloader.downloadHTML(url, endereco+'/'+str(i)+'.html')    
        i+=1
    

#Passe-se o diretório onde ficam armazenados os diretórios de comentários
#Normamente o 'comments'

def getImagesFromFolder():
    dir = 'comments/'
    directory = os.fsencode(dir)

    for file in os.listdir(directory):
        filename = os.fsdecode(file)        
        fold = os.fsdecode(dir+filename+"/")
        
        for f in os.listdir(fold):
            GetSeeReviews.getText(dir+filename+"/"+f, dir+filename+"/")

            path = dir+filename+"/"
            if('html' in f):
                getAllImages(f, path)
                
    print(" (☞ﾟヮﾟ)☞ ============> Download completo!")


def getAllImages(htmlFile, path):
    
    with open(path+htmlFile, "r", encoding='utf8') as file:
        contents = file.read()

    fileExtensions = ['jpg', 'png', 'gif', 'svg', 'jpeg']
    
    bsObj = BeautifulSoup(contents, "lxml")
    imgs = bsObj.find_all("img")
    idx = 0
    for i in imgs:

        if 'src' in str(i):
            #Condicional ternário
            url =  i['src'] if 'https' in str(i['src']) else 'https:'+str(i['src'])
            print(url)

            for extension in fileExtensions:
                if(extension in url):
                    Downloader.downloadImage(url, path+str(idx)+'.'+extension)
                    break
        idx +=1 
    file.close()


