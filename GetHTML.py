import requests
import os
def baixar_arquivo(url, endereco=None):
    if endereco is None:
        endereco = os.path.basename(url.split("?")[0])
    resposta = requests.get(url)
    if resposta.status_code == requests.codes.OK:
        with open(endereco, 'wb') as novo_arquivo:
            novo_arquivo.write(resposta.content)
        print("Download finalizado. Arquivo salvo em: {}".format(endereco))
    else:
        resposta.raise_for_status()
baixar_arquivo("https://www.goodreads.com/review/show/2047870291?book_show_action=true&from_review_page=1")


# https://www.goodreads.com/book/show/3.Harry_Potter_and_the_Sorcerer_s_Stone
# https://www.goodreads.com/review/show/173429036?book_show_action=true&from_review_page=1