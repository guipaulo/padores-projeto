#!/usr/bin/python
# -*- coding: latin-1 -*-
import os, pathlib
#from observer import ConcreteObserverA

class Removedor:
    def Remover():
        filename = str(input('Qual arquivo deseja remover? '))
        user = os.getlogin()
        file = f'C:\\Users\\{user}\\Documentos\\{filename}'

        try:
            file.unlink()
        except OSError as e:
            print(f"Error:{ e.strerror}")
Removedor.Remover()
