from src.EvalFunction import EvalFunction
from src.Parameters import Parameters
import numpy as np


class Roulette(Parameters):
    def __init__(self, list_chrom):
        self.list_chrom = list_chrom
        self.eval = EvalFunction(self.list_chrom).probability_choice()

    def choice(self):
        chosen = [np.select(self.eval > i, self.eval) for i in np.random.rand(self.pop_size)]
        chosen = [np.where(i == self.eval) for i in chosen]
        return [self.list_chrom[i[0][0]] for i in chosen]
