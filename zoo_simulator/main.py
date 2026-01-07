from zoo_simulator.simulation import run_simulation
import argparse

def cli():
    parser = argparse.ArgumentParser(
        description="Run the Zoo Ecosystem Simulation"
    )

    parser.add_argument(
        "--days",
        type=int,
        default=100,
        help="Number of days to run the simulation (default: 100)"
    )

    parser.add_argument(
        "--stats",
        action="store_true",
        help="Print population and energy stats"
    )

    args = parser.parse_args()

    populations, energies, stats_by_diet = run_simulation(days=args.days, total_animals=100)

    if args.stats:
        print("Daily population:", populations[:args.days])
        print("Daily average energy:", [round(e, 2) for e in energies[:args.days]])
        print("herbivore",stats_by_diet["herbivore"])
        print("omnivore",stats_by_diet["omnivore"])
        print("carnivore",stats_by_diet["carnivore"])

def main():
    # Optional: keep this for direct python execution
    cli()

if __name__ == "__main__":
    main()