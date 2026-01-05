import random


class Animal:
    MIN_ENERGY = 0
    MAX_ENERGY = 100
    SUCCESS_CHANCE_WHEN_HUNTED = 0.5

    def __init__(self, name, energy=100):
        self.name = name
        self._energy = None
        self.energy = energy
        self.alive = True

    @property
    def energy(self):
        return self._energy

    @energy.setter
    def energy(self, value):
        self._energy = max(self.MIN_ENERGY, min(self.MAX_ENERGY, value))
        # Auto-trigger death if energy reaches minimum
        if self._energy <= self.MIN_ENERGY and self.alive:
            self.die()

    def day_action(self, ecosystem):
        raise NotImplementedError

    def _iter_available_prey(self, ecosystem):
        for animal in ecosystem:
            if animal.is_alive() and animal is not self:
                yield animal

    def _hunt(self, prey, reward, fail_cost):
        if not self.is_alive() or not prey.is_alive():
            return

        if random.random() > prey.SUCCESS_CHANCE_WHEN_HUNTED:
            prey.die()
            self.eat(reward)
        else:
            self.decay(fail_cost)

    def _calculate_hunt_probability(self, ecosystem, multiplier=1.0):
        alive_animals = [a for a in ecosystem if a.is_alive()]
        current_pop = len(alive_animals)
        total_animals = len(ecosystem)
        return multiplier * (current_pop / total_animals)

    def decay(self, amount):
        if self.alive:
            self.energy -= amount

    def die(self):
        self.alive = False
        self._energy = self.MIN_ENERGY  # Set directly to avoid triggering death again

    def eat(self, amount):
        if self.alive:
            self.energy += amount

    def is_alive(self):
        return self.alive and self.energy > self.MIN_ENERGY
