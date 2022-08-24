#!/usr/bin/python
# -*- coding: latin-1 -*-
import fileinput
import sys
import os
#import Chainofresponsability
from chain_of_responsability import BancoIa, BancoMl, BancoPadroes
debug = True
class Buscador:
    def __init__(self,name):
        self.name = name
        self.lista = []
    def Busca(self,palavra,banco):
        self.palavra = palavra
        self.banco = banco
        user = os.getlogin()
        if self.banco == "IA":
            dir = f"F:\RepositorioProjeto\BancoIA"
            arquivos = BancoIa(palavra)
        elif self.banco == "ML":
            dir = f"F:\RepositorioProjeto\BancoML"
            arquivos = BancoMl(palavra)
        elif self.banco == "Padroes":
            dir = f"F:\RepositorioProjeto\BancoPadroes"
            arquivos = BancoPadroes(palavra)
        larquivos = arquivos.exibe()
        for i in range(len(larquivos)):
            arquivo = larquivos[i]
            arq_path = os.path.join(dir, arquivo)
            ficheiro = open(arq_path, "r")
            for line in ficheiro.readlines():
                if self.palavra in line and arquivo not in self.lista :
                    self.lista.append(arquivo)
                    ficheiro.close()
                else:
                    ficheiro.close()
        print(self.lista)