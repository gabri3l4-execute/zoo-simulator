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
        alive_animals = [a for a in ecosystem if a.is_alive()]
        prey_list = [p for p in alive_animals if p.can_be_hunted_by(self) and p != self]
        if prey_list:
            current_pop = len(alive_animals)
            total_animals = len(ecosystem)
            hunt_prob = min(1.0, current_pop / total_animals)
            if random.random() < hunt_prob:
                self.hunt(random.choice(prey_list))