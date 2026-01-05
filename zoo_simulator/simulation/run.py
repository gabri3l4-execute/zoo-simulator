import random
from zoo_simulator.ecosystem.generator import generate_ecosystem

def run_simulation(days=100, total_animals=20):
    animals = generate_ecosystem(total=total_animals)
    daily_populations = []
    daily_energy = []

    for _ in range(days):
        alive_animals = [a for a in animals if a.alive]
        current_pop = len(alive_animals)

        # Each animal performs its daily action (polymorphism)
        for a in alive_animals:
            a.day_action(animals)

        # Stochastic deaths
        for a in alive_animals:
            death_chance = 0.01 * (current_pop / total_animals)
            if random.random() < death_chance:
                a.die()

        # Reproduction (logistic)
        growth_rate = 0.15
        birth_prob = growth_rate * (1 - current_pop / total_animals)
        birth_prob = max(birth_prob, 0)

        for a in alive_animals:
            if random.random() < birth_prob:
                animals.append(type(a)(f"{a.name}_Jr", 100))

        # Stats
        alive_animals = [a for a in animals if a.alive]
        daily_populations.append(len(alive_animals))
        avg_energy = sum(a.energy for a in alive_animals) / len(alive_animals) if alive_animals else 0
        daily_energy.append(avg_energy)

    return daily_populations, daily_energy