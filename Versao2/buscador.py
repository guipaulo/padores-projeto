#!/usr/bin/python
# -*- coding: latin-1 -*-
import fileinput
import sys
import os
import Chainofresponsability
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
            dir = f"C:\\Users\\{user}\\Documents\\BancoIa"
            arquivos = BancoIa(palavra)
        elif self.banco == "ML":
            dir = f"C:\\Users\\{user}\\Documents\\BancoMl"
            arquivos = BancoMl(palavra)
        elif self.banco == "Padroes":
            dir = f"C:\\Users\\{user}\\Documents\\BancoPadroes"
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

b1 = Buscador('palavra')
bancobusca = input("Digite em qual banco deseja buscar:\n IA: Para buscar em Inteligencia Artificial\n ML: Para buscar em Machine Learning\n Padroes: Para buscar em Padroes de Projeto")
palavra = input("Digite a palavra-chave:")
'''Falta adicionar no buscador a função de buscar em um arquivo, e depois em outro'''
b1.Busca(palavra,bancobusca)

