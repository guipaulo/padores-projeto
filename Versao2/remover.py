#!/usr/bin/python
# -*- coding: latin-1 -*-
import os, sys
from observer import ConcreteObserverA

class Removedor:
    def Remover():
        filename = str(input('Qual arquivo deseja remover? '))
        user = os.getlogin()
        file = f'C:\\Users\\{user}\\Documentos\\{filename}'

        if os.path.exists(file):
            os.remove(file)
            return True
            ConcreteObserverA.update()
        else:
            print('O arquivo nao existe!')
Removedor.Remover()
