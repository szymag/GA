from src.Parameters import Parameters
from src.Roulette import Roulette
from src.EvalFunction import EvalFunction
from src.GrayConversion import GrayConversion
from src.Crossover import Xover
from src.Mutation import Mutation
import numpy as np
from  src.cProfiler import do_cprofile


class GeneticAlgorithm(Parameters):
    def __init__(self, steps_g, number_average, p_mutation):
        Parameters.__init__(self)
        self.g = 2  # number of generation
        self.steps_g = steps_g
        self.number_average = number_average
        self.p_mutation = p_mutation

    def begin_population(self):
        func = lambda x: ''.join(str(i) for i in np.array(np.random.randint(2, size=(self.chrom_length)), dtype=str))
        population = list(map(func, np.zeros(self.pop_size)))
        population = GrayConversion(population).chrom_to_gray_representation()
        return population


    def procedure(self):
        population = self.begin_population()
        tmp1 = np.zeros(self.steps_g)
        tmp2 = np.zeros(self.steps_g)
        for i, j in np.nditer([tmp1, tmp2], op_flags=['readwrite']):
            population = Roulette(population).choice()
            population = Xover(population).swap()
            population = Mutation(population, self.p_mutation).mutation()
            i[...], j[...] = EvalFunction(population).total_fit()
        return tmp1, tmp2

    @do_cprofile
    def average_results(self):
        tmp1, tmp2 = self.procedure()
        for i in range(self.number_average - 1):
            tmp = self.procedure()
            tmp1 += tmp[0]
            tmp2 += tmp[1]
        return np.transpose([tmp1 / self.number_average, tmp2 / self.number_average])


for i in range(10):
    np.savetxt('Gray_repr_xover:0.35_p_mut:' + str(0.03 + (i / 50)) + '.dat', GeneticAlgorithm(16000, 10, 0.04 + (i / 25)).average_results(), fmt=['%.9f', '%.9f'])

for i in range(5):
    np.savetxt('Gray_repr_xover:0.35_p_mut:' + str(0.4 + (i / 50)) + '.dat', GeneticAlgorithm(16000, 10, 0.04 + (i / 25)).average_results(), fmt=['%.9f', '%.9f'])
