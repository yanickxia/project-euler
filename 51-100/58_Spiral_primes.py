__author__ = 'Yann'

from utils.math_tools import *

step_len, start_num = 2, 1

spiral_prime = []


def per_primes(ls: list):
    p_counter = 0
    s = len(ls)
    for i in range(0, s):
        if ls[i] == -1 or is_probable_prime(ls[i]):
            p_counter += 1
            ls[i] = -1

    return p_counter / len(ls)


p_counter = 0
n_counter = 1
while True:
    crycle = 4
    while crycle:
        start_num += step_len
        crycle -= 1
        # spiral_prime.append(start_num)
        if is_probable_prime(start_num):
            p_counter += 1
    step_len += 2
    n_counter += 4

    # per = per_primes(spiral_prime)
    per = p_counter / n_counter
    print(per, step_len)
    if per < 0.1:
        break

print(step_len + 1)
