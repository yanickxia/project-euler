# -*- coding:utf-8 -*-


MAX = 4
COUNT = 0
n_array = [0] * MAX


def put_n_in_index(n, array):
    if sum(array) == MAX:
        global COUNT
        COUNT += 1
        return
    """
    before n is set
    :param n: int
    :return:
    """
    max_n = MAX - sum(array[0:n])
    for i in range(array[n - 1], 0, -1):
        if i > max_n:
            continue

        array[n] = i
        put_n_in_index(n + 1, array)


def loop():
    for i in range(MAX - 1, 0, -1):
        n_array[0] = i
        put_n_in_index(1, n_array)


loop()
print(COUNT)
