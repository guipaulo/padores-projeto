import buscador
import downloader
import remover

class Builder:

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