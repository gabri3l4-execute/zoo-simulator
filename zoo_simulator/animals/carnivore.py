import random
from zoo_simulator.animals.base import Animal


class Carnivore(Animal):
    SUCCESS_CHANCE_WHEN_HUNTED = 0.95

    def __init__(self, name, energy=100, hunger_threshold=0.6):
        super().__init__(name, energy, hunger_threshold)

    def hunt(self, prey):
        if not self.is_hungry:
            return
        self._hunt(prey, reward=20, fail_cost=4)

    def day_action(self, ecosystem):

        prey_list = list(self._iter_available_prey(ecosystem))
        if prey_list:
            prey_count = len(prey_list)
            predator_count = sum(
                1 for a in ecosystem if isinstance(a, type(self)) and a.is_alive()
            )
            prey_preassure = prey_count / predator_count
            base_hunt_prob = min(1.0, self._calculate_hunt_probability(ecosystem, 1.0))
            final_hunt_prob = base_hunt_prob * prey_preassure
            print(">>",final_hunt_prob)
            print(random.random())
            if random.random() < final_hunt_prob:
                self.hunt(random.choice(prey_list))
