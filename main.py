import argparse
import numpy as np
import statistics
from pprint import pprint
from utils import file
from src.genalg import GeneticAlgorithm

def main(args: argparse.Namespace) -> None:
    input_file = args.input_file
    n_runs = args.n_runs
    
    scores = []
    
    instance = next(file.get_instance_from_file(input_file))
    
    for _ in range(n_runs):
        ga = GeneticAlgorithm(20, 100)
        ga.run(instance, 100)
    
        scores.append(ga.population[0].score)

    print('MEAN MAKESPAN')
    pprint(scores)
    pprint(statistics.mean(scores))


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    
    parser.add_argument(
            '-i', '--input-file', type=str, default=None,
            help='Path to the file with input instances',
            dest='input_file')
    
    parser.add_argument(
            '-n', '--n-runs', type=int, default=10,
            help='Number of times the algorithm should be executed',
            dest='n_runs')
    
    args, _ = parser.parse_known_args()
    
    main(args)
    
