__author__ = 'Yann'


def int_to_char_set(int):
    int = str(int)

    int_set = set()
    for c in int:
        int_set.add(c)

    return int_set


def int_to_char_list(int):
    int = str(int)

    int_lst = list()
    for c in int:
        int_lst.append(c)

    return int_lst


lst = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

m = 0
i = 9
j = 1
while i < 9999:

    ls = list()
    while j < 9:
        ls.extend(int_to_char_list(i * j))
        ls = sorted(ls)

        if len(ls) < 9:
            j += 1
        if len(ls) == 9 and j > 1 and ls == lst:
            m = i
            print(m)
            break
        if len(ls) > 9:
            break
    i += 1
    j = 1
