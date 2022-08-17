#!/usr/bin/python
# -*- coding: latin-1 -*-
import os, sys


class Removedor:
    def Remover():
        filename = str(input('Qual arquivo deseja remover? '))
        user = os.getlogin()
        file = f'C:\\Users\\{user}\\Documents\\{filename}'

        if os.path.exists(file):
            os.remove(file)
        else:
            print('O arquivo não existe!')


Removedor.Remover()
