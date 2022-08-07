import os
from pathlib import Path
from pymongo import MongoClient

class Facade():
    '''Fachada com os subsistemas'''
    def __init__(self):
        self.buscador = Buscador.BuscarPDF()
        self.CadastrarArquivos()

class Buscador():
    def BuscarPDF():
        contador = 0
        palavra = str(input('Digite a palavra-chave: '))
        for file in os.listdir("/home/paulo/Downloads"):
            if file.endswith(".pdf"):
                file_name = Path(file).stem
                if palavra in file_name:
                    print(os.path.join(file_name))
                    print(' ')
                    contador+=1

class Interface():
    pass

class CadastrarArquivos():
    client = MongoClient('mongodb://localhost:8000')
    banco = client.crawler_db
    dados_crawler = banco.dados_crawler
    documento1 = Buscador.BuscarPDF()
    dados_crawler.insert_one(documento1)

if __name__ == "__main__":
    Aplicacao = Facade()