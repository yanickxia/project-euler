import math

mark_number = '1_2_3_4_5_6_7_8_9_0'


def is_matcher_n(n):
    flag = True
    for i in range(0, len(mark_number)):
        if mark_number[i] == n[i] or mark_number[i] == '_':
            pass
        else:
            return False

    return flag


min_n = 1000000000
max_n = 1400000000
n = min_n

square_n = n * n
while not is_matcher_n(str(square_n)):
    n += 10
    square_n = n * n
    print n, square_n

print n
