# Classe Gato que herda de Animal (Herança)
from classes.animal import Animal

class Gato(Animal):
    def __init__(self, nome, cor):
        # Chamando o construtor da classe pai
        super().__init__(nome)
        self.cor = cor

    # Implementação do método abstrato (Polimorfismo)
    def fazer_som(self):
        return "Miau!"
