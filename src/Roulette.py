from src.EvalFunction import EvalFunction
from src.Parameters import Parameters
import numpy as np


class Roulette(Parameters):
    def __init__(self, list_chrom):
        self.list_chrom = list_chrom
        self.eval = EvalFunction(self.list_chrom)

    def b(self):
        p = np.random.rand(self.pop_size)
        q = np.cumsum(self.eval.probability_choice())
        q = [np.select(q > i, q) for i in p]
        return q
