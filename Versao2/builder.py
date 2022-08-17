import buscador
import downloader
import remover
from abc import ABC, abstractmethod

'''DIRETOR É IMPLEMENTADO NA FACHADA, QUE DEFINE A ORDEM
DE INICIALIZAÇÃO DE CADA MÓDULO'''

class Builder(ABC):

    def Buscar(self) -> None:
        pass

    def Download(self) -> None:
        pass

    def Remover(self) -> None:
        pass

class ConcreteBuilder:

    def __init__(self) -> None:
        self.buscador = buscador.Buscador()
        self.downloader = downloader.Downloader()
        self.remover = remover.Removedor()

    def Buscar():
        return buscador.Buscador.Busca()

    def Download():
        return downloader.Downloader.Download()

    def Remover():
        return remover.Removedor.Remover()