import os
from pathlib import Path
from pymongo import MongoClient

class Facade():
    '''Fachada com os subsistemas'''
    def __init__(self):
        cliente = pymongo.MongoClient("mongodb://localhost:27017/")
        BancoDados = cliente['banco_de_dados']
        colecao = BancoDados['documentos']

        palavra = str(input('Digite a palavra-chave: '))
        self.buscador = Buscador.BuscarPDF(palavra)
        #self.CadastrarArquivos()

class Buscador():
    def BuscarPDF(palavra):
        for item in Facade.colecao.find({'text': palavra}):
            print(item)

class InterfaceGUI():
    pass

class Arquivos(Facade):
    def Inserir(id = '', text = ''):
        documento = {"id": id, "texto": text}
        d = Facade.colecao.insert_one(documento)
    def Remover(id = ''):
        documento = {"id ": id}
        Facade.colecao.delete_one(documento)

if __name__ == "__main__":
    Aplicacao = Facade()