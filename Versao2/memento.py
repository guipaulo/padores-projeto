#!/usr/bin/python
# -*- coding: latin-1 -*-

import os
import shutil

user = os.getlogin()
class Memento:
    def ExcluiMemento(filename, banco):
        if banco == 'IA':
            shutil.copy2 (f'F:\RepositorioProjeto\\BancoIA\\{filename}', f'F:\Memento')
            os.remove(f'F:\RepositorioProjeto\\BancoIA\\{filename}')
        if banco == 'ML':
            shutil.copy2 (f'F:\RepositorioProjeto\\BancoML\\{filename}', f'F:\Memento')
            os.remove(f'F:\RepositorioProjeto\\BancoML\\{filename}')
        if banco == 'Padroes':
            shutil.copy2 (f'F:\RepositorioProjeto\\BancoPadroes\\{filename}', f'F:\Memento')
            os.remove(f'F:\RepositorioProjeto\\BancoPadroes\\{filename}')

    def RetornaMemento(filename):
        banco = input('Para qual banco quer retornar? ')
        if banco == 'IA':
            shutil.copy2 (f'F:\Memento\\{filename}', f'F:\RepositorioProjeto\\BancoIA')
            os.remove(f'F:\Memento\\{filename}')
        if banco == 'ML':
            shutil.copy2 (f'F:\Memento\\{filename}', f'F:\RepositorioProjeto\\BancoML')
            os.remove(f'F:\Memento\\{filename}')
        if banco == 'Padroes':
            shutil.copy2 (f'F:\Memento\\{filename}', f'F:\RepositorioProjeto\\BancoPadroes')
            os.remove(f'F:\Memento\\{filename}')

    def ExcluiPermanente(filename):
        os.remove(f'F:\Memento\\{filename}')