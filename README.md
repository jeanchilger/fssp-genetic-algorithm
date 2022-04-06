# Flow-shop Scheduling with Genetic Algorithms

Solution to the flow-shop scheduling problem using genetic algorithms.

## Running

The entry point for the program is the `main.py` file. It executes a single instance from the Flow-shop scheduling problem at a time. The following options are available:

```
-i INPUT_FILE, --input-file INPUT_FILE
                    Path to the file with input instances
-p POPULATION_SIZE, --population-size POPULATION_SIZE
                    Max size for the population.
-g NUM_GENERATIONS, --num-generations NUM_GENERATIONS
                    Max number of generations (iterations) to execute.
-n N_RUNS, --n-runs N_RUNS
                    Number of times the algorithm should be executed
-o OUTPUT_FILE, --output-file OUTPUT_FILE
                    Path where the output report should be stored.
```

For instance, to run for the `tai20_5` setup, using a population of 100 individuals for 200 generations, one can use the command:

```
python main.py -i data/tai20_5.txt -p 100 -g 200
```

A few other options should be changed inside the script.

## Folder structure

Each of the following folders corresponds to a step in the genetic algorithm: `initialization/`, `fitness/`, `selection/`, `crossover/` and `mutation/`. Each directory comprises different strategies for the respective steps.

**Note:** The file `results/report.pdf` contains a table summarizing the results.