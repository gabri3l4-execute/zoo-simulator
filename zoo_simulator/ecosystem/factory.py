from zoo_simulator.animals import Herbivore, Carnivore, Omnivore

def create_animal(species: str, name: str, energy_level: int):
    animal_types = {
        "herbivore": Herbivore,
        "carnivore": Carnivore,
        "omnivore": Omnivore,
    }

    species = species.lower()
    return animal_types[species](species, name, energy_level)