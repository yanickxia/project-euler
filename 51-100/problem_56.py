__author__ = 'Yann'

import math

max_digit = 0
max_number = 0
for i in range(90, 100):
    for j in range(90, 100):
        digit = sum(int(digit) for digit in str(i ** j))

        if digit > max_digit:
            max_digit = digit
            max_number = [i, j]

print(max_digit, max_number)
