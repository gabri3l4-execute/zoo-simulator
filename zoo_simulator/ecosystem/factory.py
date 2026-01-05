from zoo_simulator.animals import Herbivore, Carnivore, Omnivore

def create_animal(diet: str, name: str, energy_level: int):
    animal_diet = {
        "herbivore": Herbivore,
        "carnivore": Carnivore,
        "omnivore": Omnivore,
    }

    diet = diet.lower()
    return animal_diet[diet](name, energy_level)