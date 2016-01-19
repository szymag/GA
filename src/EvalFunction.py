import numpy as np
from src.Parameters import Parameters


class EvalFunction(Parameters):

    def __init__(self, list_chrom):
        self.list_chrom = list_chrom

    def to_dec_conversion(self, list_chrom):
        return list(map(lambda x: int(x, 2), list_chrom))

    def first_string(self):
        return list(map(lambda x: x[:int(self.chrom_length / 2)], self.list_chrom))

    def second_string(self):
        return list(map(lambda x: x[int(self.chrom_length / 2):], self.list_chrom))

    def to_problem_range(self):
        list_x1 = np.array(self.to_dec_conversion(self.first_string()))
        list_x2 = np.array(self.to_dec_conversion(self.second_string()))
        tmp = (self.end_interval - self.begin_interval) / (2**int(self.chrom_length / 2) - 1)
        return tmp * list_x1 + self.begin_interval, tmp * list_x2 + self.begin_interval

    def problem_function(self):
        x = self.to_problem_range()
        return 0.5 + ((np.sin(np.sqrt(x[0]**2 + x[1]**2)))**2 - 0.5) / (1. + 0.001*(x[0]**2 + x[1]**2))**2

    def probability_choice(self):
        tmp = np.sum(self.problem_function())
        return np.cumsum(self.problem_function() / tmp)

    def total_fit(self):
        return np.sum(self.problem_function())