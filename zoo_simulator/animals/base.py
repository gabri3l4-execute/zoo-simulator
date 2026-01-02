class Animal:
    def __init__(self, species, name, energy=100):
        self.species = species
        self.name = name
        self.energy = energy
        self.alive = True
        self.capabilities = []

    def decay(self, amount):
        if self.alive:
            self.energy -= amount
            if self.energy <= 0:
                self.die()

    def die(self):
        self.alive = False
        self.energy = 0

    def eat(self, amount):
        if self.alive:
            self.energy += amount
            if self.energy > 100:
                self.energy = 100

    def is_alive(self):
        return self.alive