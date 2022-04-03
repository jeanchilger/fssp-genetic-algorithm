from dataclasses import dataclass
from typing import Union
import numpy as np

# Data class to represent a solution (chromosome)
@dataclass
class Chromosome:
    data: Union[list, np.ndarray]
    score: float
