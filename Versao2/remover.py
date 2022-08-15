import os

class Removerdor:
    def Remover():
        arq = str(input('Qual arquivo deseja remover? '))
        for file in os.listdir("/home/paulo/Documentos"):
            if os.path.exists(arq):
                os.remove(arq)
            else:
                print('O arquivo não existe!')
