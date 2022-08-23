#!/usr/bin/python
# -- coding: latin-1 --
import os, sys
from typing import List

'''
Bancos Chain vai receber do documento o tipo de banco e pode ser exibido em buscar documento.
'''


class BancosChain():
    def __init__(self, nomebanco, titulo):
        self.nomebanco = nomebanco
        self.titulo = titulo


class BancoIa(BancosChain):
    def __init__(self,nome):
        self.nome = nome

    def exibe (self):
        path = 'bancoia'
        user = os.getlogin()
        dirPath = f"F:\RepositorioProjeto\BancoIA"
        result = [f for f in os.listdir(dirPath) if os.path.isfile(os.path.join(dirPath, f))]
        return result

class BancoMl(BancosChain):
    def __init__(self,nome):
        self.nome = nome

    def exibe (self):
        path = 'bancoml'
        user = os.getlogin()
        dirPath = f"F:\RepositorioProjeto\BancoML"
        result = [f for f in os.listdir(dirPath) if os.path.isfile(os.path.join(dirPath, f))]
        return result

class BancoPadroes(BancosChain):
    def __init__(self,nome):
        self.nome = nome

    def exibe (self):
        path = 'bancopadroes'
        user = os.getlogin()
        dirPath = f"F:\RepositorioProjeto\BancoPadroes"
        result = [f for f in os.listdir(dirPath) if os.path.isfile(os.path.join(dirPath, f))]
        return result
'''b1 = BancoIa('teste')
b1.exibe()
'''
