import random
from zoo_simulator.animals.base import Animal


class Omnivore(Animal):
    SUCCESS_CHANCE_WHEN_HUNTING = 0.55

    def __init__(self, name, energy=100):
        super().__init__(name, energy)

    def graze(self):
        self.eat(3)
        self.decay(1)

    def hunt(self, prey):
        self._hunt(prey, reward=15, fail_cost=3)

    def day_action(self, ecosystem):
        self.graze()

        prey_list = list(self._iter_available_prey(ecosystem))
        if prey_list:
            hunt_prob = self._calculate_hunt_probability(ecosystem, 0.5)
            if random.random() < hunt_prob:
                self.hunt(random.choice(prey_list))
