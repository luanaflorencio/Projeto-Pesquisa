import urllib.request
from pytube import YouTube
import urllib.request


def downloadImage(url, imageName):
    opener = urllib.request.URLopener()

    opener.addheader('User-Agent', 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11')
    opener.addheader('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',)
    opener.addheader('Accept-Charset', 'ISO-8859-1,utf-8;q=0.7,*;q=0.3')
    opener.addheader('Accept-Encoding', 'none')
    opener.addheader('Accept-Language', 'en-US,en;q=0.8')
    opener.addheader('Connection', 'keep-alive')
    try:
        opener.retrieve(url, imageName)
    except Exception :
        pass

def downloadVideo(url, videoName):
    print("Baixando o video")
    YouTube(url).streams.first().download('videos/')

def downloadHTML(url, htmlName):
    urllib.request.urlretrieve(url, htmlName)
