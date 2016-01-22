from operator import xor
from src.Parameters import Parameters
import numpy as np

class GrayConversion(Parameters):
    def __init__(self, list_chrom):
        self.list_chrom = list_chrom

    def to_gray(self, num):
        tmp = num[0]
        for i, j in enumerate(num[1:]):
            tmp += str(xor(eval(num[i]), eval(num[i+1])))
        return tmp

    def from_gray(self, num):
        tmp = num[0]
        for i, j in enumerate(num[1:]):
            if tmp[i] == num[i+1]:
                tmp += '0'
            else:
                tmp += '1'
        return tmp

    def chrom_to_gray_representation(self):
        return list(map(self.to_gray, self.list_chrom))

    def chrom_to_bin_representation(self):
        return list(map(self.from_gray, self.list_chrom))
