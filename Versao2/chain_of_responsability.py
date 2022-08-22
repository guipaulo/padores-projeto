#!/usr/bin/python
# -- coding: latin-1 --
import os, sys

'''
Bancos Chain vai receber do documento o tipo de banco e pode ser exibido em buscar documento.
'''

class BancosChain():
    def _init_(self, nomebanco, titulo):
        self.nomebanco = nomebanco
        self.titulo = titulo


class BancoIa(BancosChain):
    def _init_(self,nomebanco, titulo):
        super()._init_(nomebanco, titulo)
        self.nomebanco = nomebanco
        self.bancoia = []
        if self.nomebanco == "IA":
            self.bancoia.append(self.titulo)

    def exibe(self):
        print(self.bancoia)



class BancoMl(BancosChain):

    def _init_(self, nomebanco, titulo):
        super()._init_(nomebanco, titulo)
        self.nomebanco = nomebanco
        self.bancoml = []
        if self.nomebanco == "ML":
            self.bancoml.append(self.titulo)

    def exibe(self):
        print(self.bancoml)


b1 = BancoIa('IA', 'Agentes que pensam como humanos')
b2 = BancoMl('ML', 'aprendizado de máquina')
b3 = BancoIa('IA', 'Agentes que agem como humanos')
b4 = BancoMl('ML', 'aprendizado federado')

b1.exibe()
b2.exibe()
b3.exibe()
b4.exibe()