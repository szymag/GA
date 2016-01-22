from src.Parameters import Parameters
from src.Roulette import Roulette
from src.EvalFunction import EvalFunction
from src.GrayConversion import GrayConversion
from src.Crossover import Xover
from src.Mutation import Mutation
import numpy as np
from  src.cProfiler import do_cprofile


class GeneticAlgorithm(Parameters):
    def __init__(self, steps_g, number_average):
        Parameters.__init__(self)
        self.g = 2  # number of generation
        self.steps_g = steps_g
        self.number_average = number_average

    def begin_population(self):
        func = lambda x: ''.join(str(i) for i in np.array(np.random.randint(2, size=(self.chrom_length)), dtype=str))
        population = list(map(func, np.zeros(self.pop_size)))
        population = GrayConversion(population).chrom_to_gray_representation()
        return population

    @do_cprofile
    def procedure(self):
        population = self.begin_population()
        tmp = np.zeros(self.steps_g)
        for i in np.nditer(tmp, op_flags=['readwrite']):
            population = Roulette(population).choice()
            population = Xover(population).swap()
            population = Mutation(population).mutation()
            i[...] = EvalFunction(population).total_fit()
        return tmp


    def average_results(self):
        tmp = self.procedure()
        for i in range(self.number_average - 1):
            tmp += self.procedure()
        return tmp / self.number_average


q = GeneticAlgorithm(1000, 2).average_results()
print(q)
