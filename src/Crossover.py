import random
from src.Parameters import Parameters
import numpy as np


class Xover(Parameters):
    def __init__(self, list_chrom):
        self.list_chrom = list_chrom

    def swap(self):
        mask = np.vectorize(lambda x: np.random.choice([True, False], p=[1-self.p_xover, self.p_xover]))\
            (np.zeros(self.pop_size))
        mask_not = np.logical_not(mask)
        x = np.ma.array(self.list_chrom, mask=mask).compressed()  # element to swap
        y = np.ma.array(self.list_chrom, mask=mask_not).compressed()  # element not to swap
        if len(x) % 2 == 1:
            ind1 = random.randrange(0, len(x))
            ind2 = random.randrange(0, len(y))
            if random.random() > 0.5:
                x = np.insert(x, ind1, y[ind2])
                y = np.delete(y, ind2)
            else:
                y = np.insert(y, ind2, x[ind1])
                x = np.delete(x, ind1)
        assert len(x) + len(y) == self.pop_size
        return np.concatenate((y, x))
