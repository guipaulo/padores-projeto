from builder import ConcreteBuilder
from adapter import Adapter
from adapter import Pdf


class Facade:
    opcao = int(input('Selecione a funcionalidade:\n 1 - Busca\n 2 - Download\n 3 - Excluir\n '))

    if opcao == 1:
        ConcreteBuilder.Buscar()
    elif opcao == 2:
        ConcreteBuilder.Download()
        d1 = Pdf('pdf')
        documentopdf = input("digite o nome do documento que deseja converter em formato pdf\n")
        d1.ler_documento(documentopdf)
        a1 = Adapter('documento')
        a1.ler_documento(documentopdf)
        documentotxt = input("digite o nome do documento que deseja salvar em formato txt\n")
        banco = input("digite o nome do banco em que deseja salvar o documento com formato txt\n")
        a1.gravar_documento(documentotxt, banco)
    elif opcao == 3:
        ConcreteBuilder.Remover()

Facade()