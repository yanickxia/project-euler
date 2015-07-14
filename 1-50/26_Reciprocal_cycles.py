__author__ = 'Yann'


def quotient_and_remainder(dividend, divisor):
    if dividend < divisor:
        dividend *= 10

    quotient = int(dividend / divisor)
    remainder = int(dividend % divisor)

    return [quotient, remainder]


def find_reciprocal_cycles(n):
    quotients = []
    current = [0, 1]
    while True:
        current = quotient_and_remainder(current[1], n)
        if current in quotients:
            return quotients[quotients.index(current):]
        quotients.append(current)


max_cycles = []
max_i = 0

for i in range(1, 1000):
    cycles = find_reciprocal_cycles(i)
    if cycles is not None and len(cycles) > len(max_cycles):
        max_cycles = cycles
        max_i = i
print(max_i)
