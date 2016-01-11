from operator import xor


class GrayConversion:
    def __init__(self, bin_number):
        assert type(bin_number) == str
        self.bin_number = bin_number

    def to_gray(self):
        num = self.bin_number
        tmp = num[0]
        for i, j in enumerate(num[1:]):
            tmp += str(xor(eval(num[i]), eval(num[i+1])))
        return tmp

    def from_gray(self):
        num = self.bin_number
        tmp = num[0]
        for i, j in enumerate(num[1:]):
            if tmp[i] == num[i+1]:
                tmp += '0'
            else:
                tmp += '1'
        return tmp
