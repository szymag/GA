from src.Parameters import Parameters
from src.Roulette import Roulette
from src.EvalFunction import EvalFunction
from src.GrayConversion import GrayConversion
from src.Crossover import Xover
from src.Mutation import Mutation
import numpy as np
from  src.cProfiler import do_cprofile


class GeneticAlgorithm(Parameters):
    def __init__(self):
        Parameters.__init__(self)
        self.g = 2  # number of generation

    def begin_population(self):
        func = lambda x: ''.join(str(i) for i in np.array(np.random.randint(2, size=(self.chrom_length)), dtype=str))
        population = list(map(func, np.zeros(self.pop_size)))
        return population

    #@do_cprofile
    def procedure(self):
        population = self.begin_population()
        print(EvalFunction(population).to_problem_range())
        print(EvalFunction(population).problem_function())
        for i in range(30000):
            population = Roulette(population).choice()
            population = Xover(population).swap()
            population = Mutation(population).mutation()
        return EvalFunction(population).to_problem_range(), EvalFunction(population).problem_function()


q = GeneticAlgorithm().procedure()
print(q)
