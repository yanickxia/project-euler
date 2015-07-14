__author__ = 'Yann'


def is_pandigital(multiplicand, multiplier, product):
    multiplicand = str(multiplicand)
    multiplier = str(multiplier)
    product = str(product)

    if len(multiplicand) + len(multiplier) + len(product) != 9:
        return False

    s = set()
    add_str_chars(s, multiplicand)
    add_str_chars(s, multiplier)
    add_str_chars(s, product)

    if len(s) == 9 and '0' not in s:
        return True
    return False


def add_str_chars(str_set, number):
    for i in range(0, len(number)):
        if number[i] in str_set:
            str_set.add('0')
        str_set.add(number[i])


print(is_pandigital(39, 186, 7254))

lst = []

for i in range(2, 100):
    start = 0
    start = 123 if i > 9 else 1234
    end = int(10000 / i) + 1

    for j in range(start, end):
        prod = i * j
        if is_pandigital(i, j, prod):
            lst.append([i, j, prod])

s_sum = 0

print(lst)

s_set =set()
for i in lst:
    s_set.add(i[2])
print(sum(s_set))
