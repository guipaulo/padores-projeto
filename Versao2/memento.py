#!/usr/bin/python
# -*- coding: latin-1 -*-

import os
import shutil

user = os.getlogin()
class Memento:   
    def ExcluiMemento(filename):
        shutil.copy2 (f'F:\RepositorioProjeto\\{filename}', f'F:\Memento')
        os.remove(f'F:\RepositorioProjeto\\{filename}')

    def RetornaMemento(filename):
        shutil.copy2 (f'F:\Memento\\{filename}', f'F:\RepositorioProjeto')
        os.remove(f'F:\Memento\\{filename}')

    def ExcluiPermanente(filename):
        os.remove(f'F:\Memento\\{filename}')