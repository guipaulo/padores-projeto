import fileinput
import sys
import os
debug = True
class Buscador:
    def __init__(self,name):
        self.name = name
        self.lista = []
    def Busca(self,arquivo,palavra):
        print(palavra)
        ficheiro = open(arquivo, "r")
        line_num = 0
        for line in ficheiro.readlines():
            line_num += 1
            if line.find(palavra):
                self.lista.append(arquivo)
        ficheiro.close()
        print(self.lista)

b1 = Buscador('palavra')
palavra = input("Digite a palavra-chave:")
arquivo = "ARQUIVO01.txt"
b1.Busca(arquivo,palavra)

