from builder import Builder


class Facade:
    opcao = int(input('Selecione a funcionalidade:\n 1 - Busca\n 2 - Download\n 3 - Excluir: '))

    if opcao == 1:
        Builder.Buscar()
    elif opcao == 2:
        Builder.Download()
    elif opcao == 3:
        Builder.Remover()


Facade()