import random


class Animal:
    MIN_ENERGY = 0
    MAX_ENERGY = 100

    def __init__(self, name, energy=100):
        self.name = name
        self._energy = None  # Initialize private attribute first
        self.energy = energy  # Use property setter (applies clamping)
        self.alive = True

    @property
    def energy(self):
        """Get the current energy level."""
        return self._energy

    @energy.setter
    def energy(self, value):
        """Set energy with automatic clamping to [MIN_ENERGY, MAX_ENERGY] range."""
        self._energy = max(self.MIN_ENERGY, min(self.MAX_ENERGY, value))
        # Auto-trigger death if energy reaches minimum
        if self._energy <= self.MIN_ENERGY and self.alive:
            self.die()

    def day_action(self, ecosystem):
        """Perform this animal's daily action. Override in subclasses."""
        raise NotImplementedError

    def _iter_available_prey(self, ecosystem):
        """Yield animals that can be hunted by this predator."""
        for animal in ecosystem:
            if animal.is_alive() and animal is not self:
                yield animal

    def _hunt(self, prey, success_chance, reward, fail_cost):
        """Shared hunting helper to reduce duplication in subclasses."""
        if not self.is_alive() or not prey.is_alive():
            return

        if random.random() < success_chance:
            prey.die()
            self.eat(reward)
        else:
            self.decay(fail_cost)

    def _calculate_hunt_probability(self, ecosystem, multiplier=1.0):
        """Calculate hunt probability based on population ratio and multiplier."""
        alive_animals = [a for a in ecosystem if a.is_alive()]
        current_pop = len(alive_animals)
        total_animals = len(ecosystem)
        return multiplier * (current_pop / total_animals)

    def decay(self, amount):
        """Decrease energy by amount. Property handles clamping and death."""
        if self.alive:
            self.energy -= amount

    def die(self):
        self.alive = False
        self._energy = self.MIN_ENERGY  # Set directly to avoid triggering death again

    def eat(self, amount):
        """Increase energy by amount. Property handles clamping to max."""
        if self.alive:
            self.energy += amount

    def is_alive(self):
        return self.alive and self.energy > self.MIN_ENERGY
