__author__ = 'Yann'


def square_digit(number: int):
    square = 0
    for n in str(number):
        square += int(n) ** 2
    return square


def chains_number(start_number: int):
    while start_number != 1 and start_number != 89:
        start_number = square_digit(start_number)

    return start_number

limit = 1000001
count = 0
for i in range(1, limit):
    if chains_number(i) == 89:
        count += 1

print(count)
