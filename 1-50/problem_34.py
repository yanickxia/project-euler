__author__ = 'Yann.Xia'

import math

factorial_lst = []

for i in range(0, 10):
    factorial_lst.append(math.factorial(i))

all_sum = 0
for i in range(145, 999999):
    i_sum = 0
    n = i
    while n > 0:
        j = n % 10
        i_sum += factorial_lst[j]
        n = int(n / 10)
    if i_sum == i:
        print(i_sum)
        all_sum += i_sum
print(all_sum)
