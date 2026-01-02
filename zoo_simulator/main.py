from zoo_simulator.simulation import run_simulation

def main():
    populations, energies = run_simulation(days=100, total_animals=100)
    print("Daily population:", populations[:100])
    print("Daily average energy:", [round(e,2) for e in energies[:100]])

if __name__ == "__main__":
    main()