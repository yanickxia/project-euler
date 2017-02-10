# -*- coding:utf-8 -*-


MAX = 5
COUNT = 0
n_array = [0] * MAX


def put_n_in_index(n, array, count):
    if sum(array) == MAX:
        global COUNT
        COUNT+=1

    """
    before n is set
    :param n: int
    :return:
    """
    max_n = MAX - sum(array[0:n])
    for i in range(max_n, 0, -1):
        array[n] = i
        put_n_in_index(n + 1, array, count)


print(put_n_in_index(0, n_array, COUNT))
print(COUNT)
