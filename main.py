import argparse
import csv
from pprint import pprint
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
    output_file = args.output_file
    
    scores = []
    exec_times = []
    history = []
    
    instance = next(file.get_instance_from_file(input_file))
    n_tasks = int(re.findall(r'\d+', input_file.split('.')[0].split('_')[0])[0])
    
    for _ in tqdm(range(n_runs)):
        ga = GeneticAlgorithm(
                n_tasks, population_size,
                selection_type='parent_elitism')
        ga.run(instance, num_generations, max_time=300)
    
        scores.append(ga.get_best_result().score)
        exec_times.append(ga.execution_time)
        history.append(ga.history)

    print(f'MEAN MAKESPAN: {statistics.mean(scores)}')
    print(f'STDEV MAKESPAN: {statistics.stdev(scores)}')
    print(f'LOWER BOUND: {min(scores)}')
    print(f'UPPER BOUND: {max(scores)}')
    print(f'MEAN EXEC TIME: {statistics.mean(exec_times)}')
    print(f'STDEV EXEC TIME: {statistics.stdev(exec_times)}')
    
    print([statistics.mean(scores), statistics.stdev(scores), min(scores), max(scores), statistics.mean(exec_times), statistics.stdev(exec_times)])

    _make_report(history, output_file)


def _make_report(history: list, output_path: str) -> None:
    """
    Produces a "report", with data from each generation, taken
    from the best runs regarding each of the N executions.

    Args:
        history (list): A list containg fitting score
            of the best result of each generation.
        output_path (str): Path to file where result
            should be stored.
    """

    # get transpose of history
    history = list(map(list, zip(*history)))
    
    with open(output_path, 'w') as output_file:
        csv_writer = csv.writer(output_file)
        
        csv_writer.writerow([
            '# generation',
            'lower_bound',
            'upper_bound',
            'mean',
            'stdev',
        ])
        
        for i in range(len(history)):
            row = [str(i + 1)]
            row.append('{:d}'.format(min(history[i])))
            row.append('{:d}'.format(max(history[i])))
            row.append('{:.5f}'.format(statistics.mean(history[i])))
            row.append('{:.5f}'.format(statistics.stdev(history[i])))
            
            csv_writer.writerow(row)


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
    
    parser.add_argument(
            '-o', '--output-file', type=str, default='report.csv',
            help='Path where the output report should be stored.',
            dest='output_file')
    
    args, _ = parser.parse_known_args()
    
    main(args)
    
