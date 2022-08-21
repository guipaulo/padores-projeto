import os
from urllib import response
import requests
from observer import Observador

class Downloader:
    def Download(Observador):
        user = os.getlogin()
        dir = f"C:\\Users\\{user}\\Documents"
        urls = []
        entrada = str(input('Insira o(s) URL(s) do arquivo(s) desejado(s) '))
        entrada.split(',')
        urls.append(entrada)

        for url in urls:
            response = requests.get(url)

            if response.status_code == 200:
                arq_path = os.path.join(dir, os.path.basename(url))
                with open(arq_path, 'wb') as f:
                    f.write(response.content)
        

Downloader.Download()