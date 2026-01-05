import random
from zoo_simulator.animals.base import Animal


class Carnivore(Animal):
    def __init__(self, name, energy=100):
        super().__init__(name, energy)

    def hunt(self, prey):
        """Carnivores hunt herbivores easily, omnivores with moderate difficulty."""
        from zoo_simulator.animals.herbivore import Herbivore
        from zoo_simulator.animals.omnivore import Omnivore

        if isinstance(prey, Herbivore):
            success_chance = 0.40
        elif isinstance(prey, Omnivore):
            success_chance = 0.25
        else:
            return  # carnivores do NOT hunt carnivores

        self._hunt(prey, success_chance, reward=20, fail_cost=4)

    def day_action(self, ecosystem):
        """Carnivores hunt each day."""
        prey_list = list(self._iter_available_prey(ecosystem))
        if prey_list:
            hunt_prob = min(1.0, self._calculate_hunt_probability(ecosystem, 1.0))
            if random.random() < hunt_prob:
                self.hunt(random.choice(prey_list))
