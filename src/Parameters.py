


class Parameters(object):

    p_mut = 0.1
    p_xover = 0.25
    begin_interval = -100
    end_interval = 100
    accuracy = 10000
    chrom_length = 2 * ((end_interval - begin_interval) * accuracy).bit_length()
    pop_size = 35
