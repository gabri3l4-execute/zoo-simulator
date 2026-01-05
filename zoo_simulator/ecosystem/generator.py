import random
from zoo_simulator.ecosystem.factory import create_animal

def generate_ecosystem(total=20):
    ratios = {"herbivore": 0.6, "omnivore": 0.25, "carnivore": 0.15}
    animals = []

    for diet, ratio in ratios.items():
        count = int(total * ratio)
        for _ in range(count):
            name = f"{diet.capitalize()}_{random.randint(1,999)}"
            animals.append(create_animal(diet, name, 100))

    return animals