__author__ = 'Yann'

import math


def triangle(n):
    return int(n * (n + 1) / 2)


def pentagonal(n):
    return int(n * (3 * n - 1) / 2)


def hexagonal(n):
    return int(n * (2 * n - 1))


def is_triangle(n):
    return int(n * (n + 1) / 2)


def is_pentagonal(n):
    return int(n * (3 * n - 1) / 2)


def get_x(a, b, c):
    return (-b + abs(math.sqrt(math.pow(b, 2) - 4 * a * c))) / 2 * a
