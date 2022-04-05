from dataclasses import dataclass
from typing import Union
import numpy as np

# Data class to represent a solution (chromosome)
@dataclass
class Chromosome:
    data: Union[list, np.ndarray]
    score: float
    
    def copy(self):
        return Chromosome(self.data.copy(), self.score)
        
    def __len__(self):
        return len(self.data)
    
    def __getattr__(self, name):
        # print(name)
        return getattr(self.data, name)
    
    def __getitem__(self, items):
        return self.data[items]
    
    def __setitem__(self, items, values):
        self.data[items] = values