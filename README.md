# Zoo Ecosystem Simulator

A Python-based ecosystem simulation that models the interactions between herbivores, omnivores, and carnivores in a virtual zoo environment. The simulation tracks population dynamics, energy levels, and survival patterns over time.

## Features

- **Three Animal Types**:
  - **Herbivores**: Graze on vegetation to maintain energy
  - **Omnivores**: Can both graze and hunt prey
  - **Carnivores**: Hunt other animals for survival

- **Dynamic Ecosystem**: 
  - Animals consume energy over time
  - Hunting and predator-prey interactions
  - Population-dependent birth rates (logistic growth)
  - Stochastic death events
  - Reproduction system

- **Simulation Metrics**:
  - Daily population tracking
  - Average energy levels
  - Configurable simulation duration

## Requirements

- Python 3.10 or higher
- Dependencies listed in `requirements.txt`

## Installation

### Option 1: Install as a Package (Recommended)

1. Navigate to the project directory:
   ```bash
   cd c:\Users\gkgab\Dev\Python-AI\lesson9\zoo-simulator
   ```

2. Install the package in editable mode:
   ```bash
   pip install -e .
   ```

### Option 2: Install Dependencies Only

If you just want to run the code without installing the package:

```bash
pip install -r requirements.txt
```

## Usage

### Running the Simulation

After installing the package, you can run the simulation using the command-line interface:

```bash
zoo-sim
```

### Command-Line Options

- `--days N`: Set the number of days to simulate (default: 100)
  ```bash
  zoo-sim --days 200
  ```

- `--stats`: Display detailed population and energy statistics
  ```bash
  zoo-sim --days 100 --stats
  ```

### Example Commands

```bash
# Run a 100-day simulation (default)
zoo-sim

# Run a 50-day simulation
zoo-sim --days 50

# Run a 200-day simulation with statistics output
zoo-sim --days 200 --stats
```

### Running Without Package Installation

If you haven't installed the package, you can run the simulation directly:

```bash
python -m zoo_simulator.main
python -m zoo_simulator.main --days 150
python -m zoo_simulator.main --days 100 --stats
```

## Project Structure

```
zoo-simulator/
├── README.md
├── pyproject.toml          # Project configuration and metadata
├── requirements.txt        # Python dependencies
└── zoo_simulator/          # Main package directory
    ├── __init__.py
    ├── main.py            # CLI entry point
    ├── animals/           # Animal classes
    │   ├── __init__.py
    │   ├── base.py        # Base animal class
    │   ├── herbivore.py   # Herbivore implementation
    │   ├── omnivore.py    # Omnivore implementation
    │   └── carnivore.py   # Carnivore implementation
    ├── ecosystem/         # Ecosystem generation
    │   ├── __init__.py
    │   ├── factory.py     # Animal factory
    │   └── generator.py   # Ecosystem generator
    └── simulation/        # Simulation logic
        ├── __init__.py
        └── run.py         # Main simulation runner
```

## How It Works

1. **Initialization**: The simulation generates an initial population of 100 animals distributed among herbivores, omnivores, and carnivores.

2. **Daily Cycle**:
   - Herbivores graze to restore energy
   - Omnivores graze and hunt prey
   - Carnivores hunt herbivores and omnivores
   - Random death events occur based on population density
   - Reproduction occurs with probability based on logistic growth model

3. **Energy System**: All animals start with energy and lose it over time. They must hunt or graze to survive.

4. **Population Dynamics**: Birth rates decrease as population approaches carrying capacity, while death rates increase with population density.

## Example Output

Without `--stats` flag:
```
(Simulation runs silently)
```

With `--stats` flag:
```
Daily population: [100, 98, 102, 105, ...]
Daily average energy: [85.5, 82.3, 79.8, ...]
```

## Development

### Author
Gabriela Gonzalez

### Version
0.1.0

## License

This project is for educational purposes.

## Future Enhancements

- Add visualization of population trends
- Implement more complex food chain dynamics
- Add environmental factors (seasons, weather)
- Create GUI for interactive simulation control
- Export simulation data to CSV/JSON
