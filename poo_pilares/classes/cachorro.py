# Classe Cachorro que herda de Animal (Herança)
from classes.animal import Animal

class Cachorro(Animal):
    def __init__(self, nome, raca):
        # Chamando o construtor da classe pai
        super().__init__(nome)
        self.raca = raca

    # Implementação do método abstrato (Polimorfismo)
    def fazer_som(self):
        return "Au au!"
