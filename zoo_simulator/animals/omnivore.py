import random
from zoo_simulator.animals.base import Animal
from zoo_simulator.animals.herbivore import Herbivore

class Omnivore(Animal):
    def __init__(self, name, energy=100):
        super().__init__(name, energy)

    def graze(self):
        self.eat(3)
        self.decay(1)

    def hunt(self, prey):
        success_chance = 0.25 if isinstance(prey, Herbivore) else 0.15
        self._hunt(prey, success_chance, reward=15, fail_cost=3)

    def day_action(self, ecosystem):
        """Omnivores graze and hunt each day."""
        self.graze()
        
        alive_animals = [a for a in ecosystem if a.is_alive()]
        prey_list = [p for p in alive_animals if p.can_be_hunted_by(self) and p != self]
        if prey_list:
            current_pop = len(alive_animals)
            total_animals = len(ecosystem)
            hunt_prob = 0.5 * (current_pop / total_animals)
            if random.random() < hunt_prob:
                self.hunt(random.choice(prey_list))