__author__ = 'Yann'


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
