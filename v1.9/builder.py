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
        b1 = buscador.Buscador('palavra')
        bancobusca = input(
            "Digite em qual banco deseja buscar: \n IA: Para buscar em Inteligencia Artificial\n ML: Para buscar em Machine Learning\n Padroes: Para buscar em Padroes de Projeto\n")
        palavra = input("Digite a palavra-chave: ")
        b1.Busca(palavra, bancobusca)

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