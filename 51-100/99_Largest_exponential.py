__author__ = 'Yann.Xia'

import math


def is_a_big_than_b_v2(a, b):
    n_a, e_a = int(a[0]), int(a[1])
    n_b, e_b = int(b[0]), int(b[1])

    x = math.log(n_b, n_a)
    x *= e_b

    if e_a > x:
        return True
    return False


print(is_a_big_than_b_v2([2, 11], [3, 7]))


def is_a_big_than_b(a, b):
    n_a, e_a = int(a[0]), int(a[1])
    n_b, e_b = int(b[0]), int(b[1])
    s = 1
    while e_a > 0 and e_b > 0:
        s *= (n_a / n_b)
        e_a -= 1
        e_b -= 1

        if s > 1 and e_a > e_b:
            return True

        if s < 1 and e_a < e_b:
            return False

        if s > 1:
            s /= n_b
            e_b -= 1

        if s < 1:
            s *= n_a
            e_a -= 1

    while e_a > 0:
        s *= n_a
        e_a -= 1
        if s > 1:
            return True

    while e_b > 0:
        s *= n_b
        e_b -= 1
        if s > 1:
            return True

    return False


f = open('p099_base_exp.txt')

exponentials = []
for line in f.readlines():
    exponentials.append(line.replace('\n', '').split(","))

top = [1, 1]

for n in exponentials:
    if is_a_big_than_b_v2(n, top):
        top = n

print(top)
