# -*- coding:utf-8 -*-

import math

factorials = {}

for i in range(0, 10):
    factorials[str(i)] = math.factorial(i)

def next_number(n):
    x_sum = 0
    for x in str(n):
        x_sum += factorials[x]
    return x_sum


def longest_non_repeating_chain(start):
    """
    :param start: int
    :return:
    """
    numbers = set()
    next_n = start
    numbers.add(next_n)
    for i in range(0, 59):
        next_n = next_number(next_n)
        numbers.add(next_n)
        if i != len(numbers) - 2:
            return len(numbers)

    return len(numbers)


print(longest_non_repeating_chain(540))
print(longest_non_repeating_chain(78))
print(longest_non_repeating_chain(69))

i, count = 2, 0
while i < 100 * 10000:
    if longest_non_repeating_chain(i) == 60:
        count += 1
    i += 1
print(count)