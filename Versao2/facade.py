from builder import ConcreteBuilder


class Facade:
    opcao = int(input('Selecione a funcionalidade:\n 1 - Busca\n 2 - Download\n 3 - Excluir: '))

    if opcao == 1:
        ConcreteBuilder.Buscar()
    elif opcao == 2:
        ConcreteBuilder.Download()
    elif opcao == 3:
        ConcreteBuilder.Remover()


Facade()