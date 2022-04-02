import argparse
import numpy as np
from pprint import pprint
from utils import file
from src.genalg import GeneticAlgorithm

def main(args: argparse.Namespace) -> None:
    input_file = args.input_file
    
    ga = GeneticAlgorithm(20, 100)
    pprint([np.sum(a) for a in ga.population])
    
    # for instance in file.get_instance_from_file(input_file):
    #     pprint(instance)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    
    parser.add_argument(
            '-i', '--input-file', type=str, default=None,
            help='Path to the file with input instances',
            dest='input_file')
    
    args, _ = parser.parse_known_args()
    
    main(args)
    
