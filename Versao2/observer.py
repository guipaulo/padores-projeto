from remover import Removedor
from downloader import Downloader

class Observer(ABC):
    @abstractmethod
    def update (self, subject: Removedor()) -> None:
        pass
    def update2 (self, subject: Downloader()) -> None:
        pass

class ConcreteObserverA(Observer):
    def update(self, subject: Removedor) -> None:
        if subject.Remover() == True:
            return True

class ConcreteObserverB(Observer):
    def update(self, subject: Downloader) -> None:
        if subject.Download() == True:
            return True