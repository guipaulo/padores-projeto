import buscador
import downloader
import remover
import memento
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

    def ExcluiMemento(self) -> None:
        pass

    def RetornaMemento(self) -> None:
        pass

    def ExcluiPermanente(self) -> None:
        pass

class ConcreteBuilder:
    def Buscar():
        buscador.Buscador('palavra')
        palavra = input("Digite a palavra-chave:")
        arquivo = "ARQUIVO01.txt"
        buscador.Busca(arquivo,palavra)

    def Download():
        return downloader.Downloader.Download()

    def Remover():
        return remover.Removedor.Remover()

    def ExcluiMemento():
        return memento.Memento.ExcluiMemento()
    
    def RetornaMemento():
        return memento.Memento.RetornaMemento()

    def ExcluirPermamente():
        return memento.Memento.ExcluiPermanente()