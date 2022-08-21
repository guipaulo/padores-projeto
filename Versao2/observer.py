import remover

class Observer:

    def __init__(self, observable):
        observable.subscribe(remover.Removedor.Remover())

    def notify1(self,observable,*args,**kwargs):
        print (f'O arquivo foi removido!')