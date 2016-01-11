import random


def mutation(chrom, p_mutate):
    tmp = ''
    for i in list(chrom):
        if random.random() <= p_mutate:
            tmp += str((eval(i) + 1) % 2)
        else:
            tmp = tmp + i
    return tmp
