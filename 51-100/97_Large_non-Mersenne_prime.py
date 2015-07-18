__author__ = 'Yann'

mod_number = 10000000000
product = 1

i = 1

while i <= 7830457:
    product *= 2
    product %= mod_number
    i += 1
product = 28433 * product + 1
product = str(product)
size = len(product)
print(product[size - 10:size])
