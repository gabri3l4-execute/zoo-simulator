from zoo_simulator.animals.base import Animal


class Herbivore(Animal):
    SUCCESS_CHANCE_WHEN_HUNTING = 0.20

    def __init__(self, name, energy=100):
        super().__init__(name, energy)

    def graze(self):
        self.eat(4)
        self.decay(1)

    def day_action(self, ecosystem):
        self.graze()
