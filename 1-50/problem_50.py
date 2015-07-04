__author__ = 'Yann'

from utils.Primes import Primes

primes_tools = Primes()

max_limint = 1000000
primes = primes_tools.find_less_n_primes(max_limint)
max_val = 0
max_counter = 0
max_start = 0
current_val = 2
n = 0
size = len(primes)

while n < size - 1:
    current_val = primes[n]
    i = n
    counter = 1
    start = current_val
    while current_val < max_limint:
        i += 1
        counter += 1
        current_val += primes[i]

        # 这里很重要，减少耗时操作
        if counter < max_counter:
            continue

        if current_val in primes:
            if counter > max_counter:
                max_counter = counter
                max_val = current_val
                max_start = start

    n += 1
    if (size - n) < max_counter:
        break


print('max value:', max_val, 'max counter:', max_counter, 'max_start', max_start)
