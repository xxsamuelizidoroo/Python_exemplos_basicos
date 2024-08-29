# Importando o módulo ABC (Abstract Base Classes) para criar classes abstratas
from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, nome):
        # Atributo privado (Encapsulamento)
        self.__nome = nome

    # Método getter para acessar o atributo privado (Encapsulamento)
    def get_nome(self):
        return self.__nome

    # Método abstrato (Abstração)
    @abstractmethod
    def fazer_som(self):
        pass
