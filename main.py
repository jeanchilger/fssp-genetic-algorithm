import argparse
import re
import numpy as np
import statistics
from tqdm import tqdm
from utils import file
from src.genalg import GeneticAlgorithm

def main(args: argparse.Namespace) -> None:
    input_file = args.input_file
    n_runs = args.n_runs
    population_size = args.population_size
    num_generations = args.num_generations
    
    scores = []
    
    instance = next(file.get_instance_from_file(input_file))
    n_tasks = int(re.findall(r'\d+', input_file.split('.')[0].split('_')[0])[0])
    
    for _ in tqdm(range(n_runs)):
        ga = GeneticAlgorithm(
                n_tasks, population_size,
                selection_type='only_elites')
        ga.run(instance, num_generations)
    
        scores.append(ga.population[0].score)

    print(f'MEAN MAKESPAN: {statistics.mean(scores)}')
    print(f'STDEV MAKESPAN: {statistics.stdev(scores)}')


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    
    parser.add_argument(
            '-i', '--input-file', type=str, default=None,
            help='Path to the file with input instances',
            dest='input_file')
    
    parser.add_argument(
            '-p', '--population-size', type=int, default=100,
            help='Max size for the population.',
            dest='population_size')
    
    parser.add_argument(
            '-g', '--num-generations', type=int, default=300,
            help='Max number of generations (iterations) to execute.',
            dest='num_generations')
    
    parser.add_argument(
            '-n', '--n-runs', type=int, default=10,
            help='Number of times the algorithm should be executed',
            dest='n_runs')
    
    args, _ = parser.parse_known_args()
    
    main(args)
    
