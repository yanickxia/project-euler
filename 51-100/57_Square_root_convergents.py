__author__ = 'Yann'


class Fractional(object):
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator

    def __str__(self):
        return 'numerator: ' + str(self.numerator) + ' , denominator: ' + str(self.denominator)


def fractional_plus(x: Fractional, y: Fractional):
    denominator = x.denominator * y.denominator
    s = x.numerator * y.denominator + y.numerator * x.denominator

    return Fractional(s, denominator)


def fractional_divide(divided: Fractional, divided_by: Fractional):
    numerator = divided.numerator * divided_by.denominator
    denominator = divided.denominator * divided_by.numerator

    return Fractional(numerator, denominator)


counter = 0

for i in range(1, 1000):
    base = Fractional(5, 2)
    for j in range(1, i):
        base = fractional_plus(fractional_divide(Fractional(1, 1), base), Fractional(2, 1))

    base = fractional_plus(Fractional(1, 1), fractional_divide(Fractional(1, 1), base))
    if len(str(base.numerator)) > len(str(base.denominator)):
        counter += 1

print(counter)