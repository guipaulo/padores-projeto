import os
from pathlib import Path
from pymongo import MongoClient

class Buscador:
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
        print(f'Foram encontrados {contador} arquivos!')

class Interface():
    pass

class CadastrarArquivos():
    pass

class Facade:
    '''Fachada com os subsistemas'''
    def __init__(self):
        client = MongoClient()
        client = MongoClient('mongodb://localhost:8000')
        self.buscador = Buscador.BuscarPDF()

if __name__ == "__main__":
    Aplicacao = Facade()