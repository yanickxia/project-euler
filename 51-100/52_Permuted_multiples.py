__author__ = 'Yann'


def int_to_char_set(int):
    int = str(int)

    int_set = set()
    for c in int:
        int_set.add(c)

    return int_set


i = 1
while True:

    if str(i)[0] != '1':
        i += 1
        continue

    if sorted(str(i)) == sorted(str(2 * i)) == sorted(str(3 * i)) == sorted(str(4 * i)) == sorted(str(5 * i)) == sorted(
            str(6 * i)):
        break

    i += 1

#
print(i)