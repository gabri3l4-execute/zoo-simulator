import random
from zoo_simulator.animals.base import Animal

class Carnivore(Animal):
    def __init__(self, species, name, energy=100):
        super().__init__(species, name, energy)
        self.capabilities = ["hunt"]

    def hunt(self, prey):
        if not self.alive or not prey.alive:
            return
        if prey.species == "carnivore":
            return

        success_chance = 0.4 if prey.species == "herbivore" else 0.25

        if random.random() < success_chance:
            prey.die()
            self.eat(20)
        else:
            self.decay(4)