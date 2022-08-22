import fileinput
import sys
import os
debug = True
class Buscador:
    def _init_(self,name):
        self.name = name
        self.lista = []
    def Busca(self,arquivo,palavra):
        self.arquivo = arquivo
        self.palavra = palavra
        user = os.getlogin()
        dir = f"C:\\Users\\{user}\\Documents"
        arq_path = os.path.join(dir, self.arquivo)
        ficheiro = open(arq_path, "r")
        line_num = 0
        for line in ficheiro.readlines():
            line_num += 1
            if self.palavra in line:
                self.lista.append(arquivo)
        ficheiro.close()
        print(self.lista)

b1 = Buscador('palavra')
palavra = input("Digite a palavra-chave:")
'''Falta adicionar no buscador a função de buscar em um arquivo, e depois em outro'''
arquivo = "arqdoc.txt"
b1.Busca(arquivo, palavra)