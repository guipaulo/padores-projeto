import requests 

class Downloader:
    def Download():
        url = str(input('Insira o URL do arquivo desejado'))
        endereco = '/home/paulo/Documentos'
        resposta = requests.get(url)
        if resposta.status_code == requests.codes.OK:
            with open(endereco, 'wb') as novo_arquivo:
                novo_arquivo.write(resposta.content)
        print("Download finalizado. Arquivo salvo em: {}".format(endereco))

Downloader.Download()