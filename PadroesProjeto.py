import os
from pathlib import Path
from pymongo import MongoClient

class Facade():
    '''Fachada com os subsistemas'''
    def __init__(self):
        palavra = str(input('Digite a palavra-chave: '))
        self.buscador = Buscador.BuscarPDF(palavra)
        #self.CadastrarArquivos()

class Buscador():
    def BuscarPDF(palavra):
        contador = 0
        for file in os.listdir("/home/paulo/Downloads"):
            if file.endswith(".pdf"):
                file_name = Path(file).stem
                if palavra in file_name:
                    print(os.path.join(file_name))
                    print(' ')
                    contador+=1

class InterfaceGUI():
    pass

class CadastrarArquivos():
    pass

if __name__ == "__main__":
    Aplicacao = Facade()