from .base import Animal

class Herbivore(Animal):
    def __init__(self, species, name, energy=100):
        super().__init__(species, name, energy)
        self.capabilities = ["graze"]

    def graze(self):
        self.eat(4)
        self.decay(1)