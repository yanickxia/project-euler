__author__ = 'Yann'

import math
import time


# http://b.hiphotos.baidu.com/baike/c0%3Dbaike92%2C5%2C5%2C92%2C30/sign=bb9aa6898bd4b31ce4319ce9e6bf4c1a/adaf2edda3cc7cd97c6789133901213fb90e91b6.jpg

def find_prime_less_n(n):
    time_start = time.time()

    # init primes to [0 ... n]
    primes = []
    for i in range(0, n):
        primes.append(i)
    # Find all primes
    i = 2
    while i != 0 and n > i:
        j = i + i
        while j < n:
            primes[j] = 0
            j += i
        # Find next not null number
        i += 1
        while i < n and primes[i] == 0:
            i += 1
    new_primes = []
    for n in primes:
        if n != 0:
            new_primes.append(n)

    time_end = time.time()
    print('find primes use time: ', time_end - time_start)
    return new_primes


def divisors_sum(n, primes):
    i = 0
    n_divisors_sum = 1
    while primes[i] <= n and i < len(primes) - 1:
        count = 0
        while n % primes[i] == 0:
            count += 1
            n = int(n / primes[i])
        n_divisors_sum *= (math.pow(primes[i], count + 1) - 1) / (primes[i] - 1)
        i += 1
    return int(n_divisors_sum / 2)


def is_perfect_number(n, primes):
    if n == divisors_sum(n, primes):
        return True
    return False


def is_deficient_number(n, primes):
    if n > divisors_sum(n, primes):
        return True
    return False


def is_abundant_number(n, primes):
    if n < divisors_sum(n, primes):
        return True
    return False

# Main

n_len = 28123

# find primes less than n_len
primes = find_prime_less_n(n_len)
primes.remove(1)
abundant_numbers = [0] * n_len

# find all aboudant numbers
time_start = time.time()
for i in range(2, n_len):
    if is_abundant_number(i, primes):
        abundant_numbers[i] = 1

time_end = time.time()
print('select aboudant number use times: ', time_end - time_start)

# find all index
abundant_numbers_index = []
for i in range(0, n_len):
    if abundant_numbers[i] == 1:
        abundant_numbers_index.append(i)

# version 1
# find all can sum by tow abundant number
# can_as_two_abundant_numbers = [0] * n_len
# time_start = time.time()
# for i in range(0, n_len):
#     for j in range(i, n_len):
#         if (abundant_numbers[i] and abundant_numbers[j]) and i + j < n_len:
#             can_as_two_abundant_numbers[i + j] = 1
# time_end = time.time()
# print('select all aboudant can not sum by two abouant number use times: ', time_end - time_start)


# version 2
can_as_two_abundant_numbers = [0] * n_len * 2
time_start = time.time()
for i in range(0, len(abundant_numbers_index)):
    for j in range(i, len(abundant_numbers_index)):
        can_as_two_abundant_numbers[abundant_numbers_index[i] + abundant_numbers_index[j]] = 1
time_end = time.time()
print('select all aboudant can not sum by two abouant number use times: ', time_end - time_start)

# cal sum of can't write by two abundant number
n_sum = 0
for i in range(0, n_len):
    if can_as_two_abundant_numbers[i] == 0:
        n_sum += i

print(n_sum)
