__author__ = 'Yann'

loop = 1001
i, j, i_sum, sum = 0, 0, 0, 0

for i in range(1, loop):
    i_sum = i
    for j in range(1, i):
        i_sum = (i_sum * i) % 1000000000000
    sum = (sum + i_sum) % 1000000000000

print(sum)