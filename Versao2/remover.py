#!/usr/bin/python
# -*- coding: latin-1 -*-
import os, sys
from observer import Observer

class Removedor:
    Observers = Observer()

    def Remover():
        filename = str(input('Qual arquivo deseja remover? '))
        user = os.getlogin()
        file = f'C:\\Users\\{user}\\Documentos\\{filename}'

        if os.path.exists(file):
            os.remove(file)
            return True
        else:
            print('O arquivo nao existe!')

    def Notificar(self, *args, **kwargs):
        if Removedor.Remover() == True:
            Observer.notify1()

Removedor.Remover()
