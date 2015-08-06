__author__ = 'Yann'

import random


def is_prime_slow(n):
    if n == 2 or n == 3: return True
    if n < 2 or n % 2 == 0: return False
    if n < 9: return True
    if n % 3 == 0: return False
    r = int(n ** 0.5)
    f = 5
    while f <= r:
        if n % f == 0: return False
        if n % (f + 2) == 0: return False
        f += 6
    return True


def is_prime(n, random_cycle):
    if n == 1 or n == 3:
        return True

    if n == 2:
        return False

    src_n = n
    n, i = n - 1, 0
    random_cycle = random_cycle

    while n % 2 == 0:
        n /= 2
        i += 1
    m, q = int(n), i
    s = q

    a = random.randint(2, src_n - 2)
    x = a ** m

    while random_cycle > 0:
        x = (x * x)
        d = x % src_n
        if d == 1 and x != src_n - 1 and x != 1:
            return False
        random_cycle -= 1
    return True


def find_less_n_primes_bools(n):
    primes = [1] * (n + 1)

    i = 2
    while n > i:
        j = i + i
        while j < n:
            primes[j] = 0
            j += i
        # find next not 0 number
        i += 1
        while i < n and primes[i] == 0:
            i += 1
    primes[0] = 0
    primes[1] = 0
    return primes


def find_less_n_primes(n):
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
    primes[1] = 0
    s = set(primes)
    primes = list(s)
    primes.remove(0)
    primes = sorted(primes)

    return primes


def is_integer(n):
    n = str(n)
    ns = n.split('.')
    if len(ns) == 1:
        return True
    return ns[1] == '0'


def gen_pandigital_numbers(numbers: list, number: str, gen_numbers: list):
    if numbers == []:
        gen_numbers.append(int(number))
        return

    for i in numbers:
        copy_number = number
        copy_number += str(i)
        copy_numbers = numbers.copy()
        copy_numbers.remove(i)
        gen_pandigital_numbers(copy_numbers, copy_number, gen_numbers)

    return gen_numbers


def isPalindrome(n):
    return str(n)[::-1] == str(n)


def is_pandigital(x):
    x = int(x)
    count = 0
    x_char_set = set()
    while x > 0:
        x_char_set.add(x % 10)
        x = int(x / 10)
        count += 1

    if count == len(x_char_set):
        return True
    return False


def is_dived_by_primes(n: int, primes: list, counters: int):
    i = 0
    counter = 0
    divied = 0
    while i < len(primes):
        while n % primes[i] == 0:
            n = int(n / primes[i])
            if primes[i] != divied:
                counter += 1
                divied = primes[i]
        if n == 1 and counters == counter:
            return True
        if n < primes[i] and counter > counters:
            break
        i += 1
    return False

_mrpt_num_trials = 5
def is_probable_prime(n):
    assert n >= 2
    # special case 2
    if n == 2:
        return True
    # ensure n is odd
    if n % 2 == 0:
        return False
    # write n-1 as 2**s * d
    # repeatedly try to divide n-1 by 2
    s = 0
    d = n - 1
    while True:
        quotient, remainder = divmod(d, 2)
        if remainder == 1:
            break
        s += 1
        d = quotient
    assert (2 ** s * d == n - 1)

    # test the base a to see whether it is a witness for the compositeness of n
    def try_composite(a):
        if pow(a, d, n) == 1:
            return False
        for i in range(s):
            if pow(a, 2 ** i * d, n) == n - 1:
                return False
        return True  # n is definitely composite

    for i in range(_mrpt_num_trials):
        a = random.randrange(2, n)
        if try_composite(a):
            return False

    return True  # no base tested showed n as composite
