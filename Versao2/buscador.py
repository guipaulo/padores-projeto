import os
from pathlib import Path

class Buscador:
    def Busca():
        opcao = str(input('Por qual palavra deseja buscar o documento? '))
        for file in os.listdir("/home/paulo/Documentos"):
            if file.endswith(".pdf"):
                file_name = Path(file).stem
                if opcao in file_name:
                    print(os.path.join(file_name))
                    print(' ')

Buscador.Busca()