from zoo_simulator.animals.base import Animal

class Herbivore(Animal):
    def __init__(self, name, energy=100):
        super().__init__(name, energy)

    def graze(self):
        self.eat(4)
        self.decay(1)

    def day_action(self, ecosystem):
        """Herbivores graze each day."""
        self.graze()