import Main
import Downloader



'''
1 - usar Downloader.downloadHTML passando a url do livro que você deseja baixar no goodReads e o nome
    do arquivo que será salvo no diretório do projeto.

2- chamar a Main.downloadCompleteReview -> este método cria uma pasta 'comments' contento pastas
   para cada um cometário. Esse método utiliza o nome do arquivo baixado na etapa anterior, então, 
   passe o nome do aquivo.

3- por fim, usar a Main.getImagesFromFolder passando o diretório 'comments'. Esse método percorre
   cada pasta de comentários, separa o texto, nome de usuário e data de comentário em um arquivo com 
   nome 'file.txt' e faz o download de todas as imagens presentes no html e os armazena na respectiva
   pasta do comentário.

4- MÉTODO EM DESENVOLVIMENTO @TODO ==> getVideosFromFolder

   Aproveite
   ⊂_ヽ
   　 ＼＼ seu
   　　 ＼( ͡° ͜ʖ ͡°)
   　　　 >　⌒ヽ
   　　　/ 　 へ＼
   　　 /　　/　＼＼Webscrapping
   　　 ﾚ　ノ　　 ヽ_つ
   　　/　/
   　 /　/| 
   　(　(ヽ
   　|　|、＼
   　| 丿 ＼ ⌒)
   　| |　　) /
   ノ )　　Lﾉ
   (_／#Python

'''
url = "https://www.goodreads.com/book/show/3.Harry_Potter_and_the_Sorcerer_s_Stone?from_search=true&qid=DRP5hw4EFq&rank=1"
downloadedFileName = 'harry.html'


# Downloader.downloadHTML(url, downloadedFileName)
# Main.downloadCompleteReview(downloadedFileName)
Main.getImagesFromFolder()