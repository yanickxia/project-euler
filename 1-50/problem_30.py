__author__ = 'Yann'

import math

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
init_sum = 0
result_sum = 0
power_number = []

for n in numbers:
    power_number.append(int(math.pow(n, 5)))

# for n in numbers:
#     new_number = numbers.copy()
#     new_number.remove(n)
#     n_number = new_number.copy()
#     n_sum = init_sum + n * 10000
#     for k in n_number:
#         n_number.remove(k)
#         s_number = n_number.copy()
#         k_sum = n_sum + k * 1000
#         for j in s_number:
#             s_number.remove(j)
#             j_number = s_number.copy()
#             j_sum = k_sum + j * 100
#             for l in j_number:
#                 l_number = j_number.remove(l)
#                 l_number = j_number.copy()
#                 l_sum = j_sum + l * 10
#                 for z in l_number:
#                     z_sum = z + l_sum
#                     if z_sum == math.pow(n, 5) + math.pow(k, 5) + math.pow(j, 5) + math.pow(l, 5) + math.pow(z, 5):
#                         print(z_sum, '= ', math.pow(n, 5), '+', math.pow(k, 5), '+', math.pow(j, 5), '+',
#                               math.pow(l, 5), '+', math.pow(z, 5))
#                     else:
#                         print(z_sum, '!= ', math.pow(n, 5), '+', math.pow(k, 5), '+', math.pow(j, 5), '+',
#                               math.pow(l, 5), '+', math.pow(z, 5))


for n in range(2, 5 * int(math.pow(9, 5))):
    x = 0
    i = n
    while i > 0:
        x += math.pow(i % 10, 5)
        i = int(i / 10)
    if x == n:
        result_sum += x


print(result_sum)
