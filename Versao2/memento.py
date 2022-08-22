#!/usr/bin/python
# -*- coding: latin-1 -*-

import os
import shutil

user = os.getlogin()
class Memento:   
    def ExcluiMemento(filename):
        shutil.copy2 (f'C:\\Users\\{user}\\Repositorio\\{filename}', f'C:\\Users\\{user}\\Memento')
        os.remove(f'C:\\Users\\{user}\\Repositorio\\{filename}')

    def RetornaMemento(filename):
        shutil.copy2 (f'C:\\Users\\{user}\\Memento\\{filename}', f'C:\\Users\\{user}\\Repositorio')
        os.remove(f'C:\\Users\\{user}\\Memento\\{filename}')

    def ExcluiPermanente(filename):
        os.remove(f'C:\\Users\\{user}\\Memento\\{filename}')