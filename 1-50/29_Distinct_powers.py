__author__ = 'Yann'

import math

numbers = []

for i in range(2, 101):
    for j in range(2, 101):
        numbers.append(int(math.pow(i, j)))

numbers = list(set(numbers))
numbers.sort()

print(len(numbers))
