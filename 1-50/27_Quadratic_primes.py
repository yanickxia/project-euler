__author__ = 'Yann'

import math


def find_prime_less_n(n):
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
        if n != 0 and n != 1:
            new_primes.append(n)
    return new_primes


def find_prime_less_n_v2(n):
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
    return primes


def is_prime(number):
    for i in range(2, int(math.sqrt(number) + 1)):
        if number % i == 0:
            return False
    return True


def is_prime_v2(number, primes):
    if primes[number] != 0:
        return True
    return False


max_count = 0
max_a = 0
max_b = 0

# Main

# Find all primes

primes = find_prime_less_n_v2(2001000)

primes_less_than_1000 = find_prime_less_n(1000)
primes_less_than_1000 = set(primes_less_than_1000)
primes_less_than_1000_c = []
for n in primes_less_than_1000:
    primes_less_than_1000_c.append(n)

for a in range(-999, 1000):
    for b in primes_less_than_1000_c:
        n = 0
        count = 0
        if (1 + a + b) % 2 == 0:
            b += 1
            continue
        while True:
            n += 1
            y = n * n + a * n + b
            if y > 0 and is_prime_v2(y, primes):
                count += 1
            else:
                break
        if count > max_count:
            max_count = count
            max_a = a
            max_b = b

print(max_a * max_b)