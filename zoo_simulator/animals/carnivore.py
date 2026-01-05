import random
from zoo_simulator.animals.base import Animal
from zoo_simulator.animals.herbivore import Herbivore

class Carnivore(Animal):
    def __init__(self, name, energy=100):
        super().__init__(name, energy)

    def can_be_hunted_by(self, predator):
        """Carnivores cannot be hunted by other carnivores."""
        return not isinstance(predator, Carnivore)

    def hunt(self, prey):
        success_chance = 0.4 if isinstance(prey, Herbivore) else 0.25
        self._hunt(prey, success_chance, reward=20, fail_cost=4)

    def day_action(self, ecosystem):
        """Carnivores hunt each day."""
        prey_list = list(self._iter_available_prey(ecosystem))
        if prey_list:
            hunt_prob = min(1.0, self._calculate_hunt_probability(ecosystem, 1.0))
            if random.random() < hunt_prob:
                self.hunt(random.choice(prey_list))
        else:
            self.decay(4)