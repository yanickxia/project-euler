__author__ = 'Yann'

import random


def is_prime(n, random_cycle):
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


def gen_pandigital_numbers(numbers:list, number:str, gen_numbers:list):
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


def is_dived_by_primes(n:int, primes:list, counters:int):
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
