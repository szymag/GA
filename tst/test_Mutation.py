import cProfile
import numpy as np
def do_cprofile(func):
    def profiled_func(*args, **kwargs):
        profile = cProfile.Profile()
        try:
            profile.enable()
            result = func(*args, **kwargs)
            profile.disable()
            return result
        finally:
            profile.print_stats()

    return profiled_func
@do_cprofile
def fun():
    tmp = 0
    for i in range(10000):
        tmp += i
    return tmp

@do_cprofile
def fun1():
    return np.sum(np.arange(1000000))

print(fun1())

print(fun())