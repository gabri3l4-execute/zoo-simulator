import random
from zoo_simulator.animals.base import Animal


class Carnivore(Animal):
    SUCCESS_CHANCE_WHEN_HUNTING = 0.95

    def __init__(self, name, energy=100):
        super().__init__(name, energy)

    def hunt(self, prey):
        self._hunt(prey, reward=20, fail_cost=4)

    def day_action(self, ecosystem):
        prey_list = list(self._iter_available_prey(ecosystem))
        if prey_list:
            hunt_prob = min(1.0, self._calculate_hunt_probability(ecosystem, 1.0))
            if random.random() < hunt_prob:
                self.hunt(random.choice(prey_list))
