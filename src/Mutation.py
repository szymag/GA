from src.Parameters import Parameters
import numpy as np
import random


class Mutation(Parameters):
    def __init__(self, list_chrom):
        Parameters.__init__(self)
        self.list_chrom = list_chrom

    def mutation(self):
        mask = np.vectorize(lambda x: np.random.choice([True, False], p=[1-self.p_mut, self.p_mut]))\
            (np.zeros(self.pop_size))
        mask_not = np.logical_not(mask)
        population_to_mutate = np.ma.array(self.list_chrom, mask=mask).compressed()  # element to mutate
        not_mutate = list(np.ma.array(self.list_chrom, mask=mask_not).compressed())  # element not to mutate
        for i in population_to_mutate:
            where_replace = random.randrange(1, self.chrom_length - 1)
            not_mutate.append(i[:where_replace] + str((eval(i[where_replace]) + 1) % 2) + i[where_replace + 1:])
        assert len(not_mutate) == self.pop_size
        return not_mutate