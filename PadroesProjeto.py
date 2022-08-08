import os
from pathlib import Path
import pymongo

class Facade():
    '''Fachada com os subsistemas'''
    def __init__(self):
        self.insert_arq = Arquivos.Inserir('1', 'Arquivo exemplo')
        palavra = str(input('Digite a palavra-chave: '))
        self.buscador = Buscador.BuscarPDF('exemplo')

class Buscador():
    def BuscarPDF(palavra):
        for item in colecao.find({'text': palavra}):
            print(item)

class InterfaceGUI():
    pass

class Arquivos(Facade):
    def Inserir(id = '', text = ''):
        documento = {"id": id, "texto": text}
        d = colecao.insert_one(documento)
    def Remover(id = ''):
        documento = {"id ": id}
        colecao.delete_one(documento)

if __name__ == "__main__":
    cliente = pymongo.MongoClient("mongodb://localhost:27017/")
    BancoDados = cliente['banco_de_dados']
    colecao = BancoDados['documentos']
    Aplicacao = Facade()