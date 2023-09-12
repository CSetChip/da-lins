from abc import ABC, abstractmethod

class Passaro(ABC):

    @abstractmethod
    def voar(self):
        pass

    @abstractmethod
    def emitir_som(self):
        pass

class Pato(Passaro):

    def voar(self):
        return 'Pato \nVoando...'

    def emitir_som(self):
        return 'Pato emitindo som... \nQuack Quack'

class Pardal(Passaro):

    def voar(self):
        return 'Pardal \nVoando...'

    def emitir_som(self):
        return 'Pardal emitindo som.. \nPiu Piu'

pardal = Pardal()
pato = Pato()

print(pato.voar())
print(pato.emitir_som())
print(pardal.voar())
print(pardal.emitir_som())
