__author__ = 'Yann'


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
