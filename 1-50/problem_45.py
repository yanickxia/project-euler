__author__ = 'Yann'

import math


def pentagonal(n):
    return int(n * (3 * n - 1) / 2)


def hexagonal(n):
    return int(n * (2 * n - 1))


def is_triangle(n):
    return str(get_x(1, 1, (-n) * 2)).split('.')[1] == '0'


def is_pentagonal(n):
    return str(get_x(3, -1, (-n) * 2)).split('.')[1] == '0'


def is_hexagonal(n):
    return str(get_x(2, -1, (-n) * 2)).split('.')[1] == '0'


def get_x(a, b, c):
    return (-b + abs(math.sqrt(math.pow(b, 2) - 4 * a * c))) / (2 * a)


notFound = True
start = 144
while notFound:
    s = hexagonal(start)
    if is_triangle(s) and is_pentagonal(s):
        notFound = False
        print(s, start)
    start += 1
