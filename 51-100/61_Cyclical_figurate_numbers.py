# -*- coding:utf-8 -*-


def polygonal_number(s, n):
    """
    calc polygonal_number
    :param s:  s-gonal
    :param n:  nth
    :return:
    """
    return int(((s - 2) * (n * (n - 1))) / 2 + n)


def find_match_number_in_index_array(ns, i, arrays):
    """
    find_match_number_in_index_array
    :param n:Str  number
    :param i:Int  index
    :return: n
    """
    match_n = []
    array = arrays[i]
    for n in ns:
        for item in array:
            if item[0:2] == n[2:4]:
                match_n.append(item)

    return match_n


s_list = [3, 4, 5, 6, 7, 8]
s_num_list = []

for s in s_list:
    i = 1
    n, n_arr = polygonal_number(s, i), []

    while n < 1000:
        i += 1
        n = polygonal_number(s, i)

    while 999 < n < 10000:
        n_arr.append(str(n))
        i += 1
        n = polygonal_number(s, i)

    s_num_list.append(n_arr)

first_array = s_num_list[0]
index_list = [1, 2, 3, 4, 5]

for n in first_array:
    ns = [n]
    for index_n in index_list:
        ns = find_match_number_in_index_array(ns, 1, s_num_list)
        if len(ns) == 0:
            break
