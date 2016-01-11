import numpy as np
from src.Parameters import Parameters


class EvalFunction(Parameters):

    def __init__(self, list_chrom):
        self.list_chrom = list_chrom

    def to_dec_conversion(self, list_chrom):
        return list(map(lambda x: int(x, 2), list_chrom))

    def first_string(self):
        return list(map(lambda x: x[:self.chrom_length], self.list_chrom))

    def second_string(self):
        return list(map(lambda x: x[self.chrom_length:], self.list_chrom))

    def to_problem_range(self):
        list_x1 = np.array(self.to_dec_conversion(self.first_string()))
        list_x2 = np.array(self.to_dec_conversion(self.second_string()))
        tmp = (self.end_interval - self.begin_interval) / (2**self.chrom_length - 1)
        return tmp * list_x1 + self.begin_interval, tmp * list_x2 + self.begin_interval

    def problem_function(self):
        x = self.to_problem_range()
        return 0.5 + ((np.sin(np.sqrt(x[0]**2 + x[1]**2)))**2 - 0.5) / (1. + 0.001*(x[0]**2 + x[1]**2))**2

    def full_fit_generation(self):
        return np.sum(self.problem_function())

    def probability_choice(self):
        return self.problem_function() / self.full_fit_generation()
