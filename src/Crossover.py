import random
from src.Parameters import Parameters
import numpy as np


class Xover(Parameters):
    def __init__(self, list_chrom):
        self.list_chrom = list_chrom

    def swap(self):
        mask = np.vectorize(lambda x: np.random.choice([True, False], p=[1-self.p_xcover, self.p_xcover]))\
            (np.zeros(self.pop_size))
        mask_not = np.logical_not(mask)
        x = np.ma.array(self.list_chrom, mask=mask).compressed() # element to swap
        y = np.ma.array(self.list_chrom, mask=mask_not).compressed() # element not to swap
        if len(x) % 2 == 1:
            if random.random() > 0.5:
                ind = random.randrange(0, self.chrom_length-1)
                x = np.insert(x, ind, y[ind])
                y = np.delete(y, ind)
            else:
                ind = random.randrange(0, self.chrom_length-1)
                y = np.insert(y, ind, x[ind])
                x = np.delete(x, ind)
        assert len(x) + len(y) == self.pop_size
        return np.concatenate((y, x))
