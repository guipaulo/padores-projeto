#!/usr/bin/python
# -- coding: latin-1 --
import os, sys
from adapter import Listadocumentos

import adapter

'''
Bancos Chain vai receber do documento o tipo de banco e pode ser exibido em buscar documento.
'''

class BancosChain():
    def  __init__(self, nomebanco, titulo):
        self.nomebanco = nomebanco
        self.titulo = titulo


class BancoIa(BancosChain):
    def __init__(self,nomebanco, titulo):
        super().__init__(nomebanco, titulo)
        self.nomebanco = nomebanco
        bancoia = []
        self.bancoia = bancoia
        if self.nomebanco == "IA":
            self.bancoia.append(self.titulo)
    def exibe(self):
        print(self.bancoia)

class BancoMl(BancosChain):
    def  __init__(self, nomebanco, titulo):
        super().__init__(nomebanco, titulo)
        self.nomebanco = nomebanco
        self.bancoml = []
        if self.nomebanco == "ML":
            self.bancoml.append(self.titulo)

    def exibe(self):
        print(self.bancoml)

nomebanco = Listadocumentos.banco
titulo = Listadocumentos.titulo
b1 = BancoIa(nomebanco,titulo)
#b2 = BancoMl()
#b3 = BancoIa()
#b4 = BancoMl()

b1.exibe()
'''
b2.exibe()
b3.exibe()
b4.exibe()'''