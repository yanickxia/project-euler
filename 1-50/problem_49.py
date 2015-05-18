__author__ = 'Yann'

import math


s = 1000000
sn = ''

s_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

for i in range(10, 0, -1):
    if math.factorial(i) < s:
        if( s % math.factorial(i) == 0):
            sn += str(int(s / math.factorial(i)))
        else:
            sn += str(int(s / math.factorial(i) + 1))
        s %= math.factorial(i)
        if s == 0:
            break
sn_w = ''
for i in sn:
    sn_w += str(s_list[int(i) - 1])
    s_list.remove(s_list[int(i) - 1])

for i in range(len(s_list) - 1, -1, -1):
    sn_w += str(s_list[i])

print(sn_w)
