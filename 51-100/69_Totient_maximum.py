__author__ = 'Yann.Xia'

from utils import math_tools

limit = 1000000
# limit = 10
primes = math_tools.find_less_n_primes(limit)

n = 1
prime_factor = []
for prime in primes:
    n *= prime
    if n > limit:
        n /= prime
        break
print(n)


# max_counter, max_n = 0, 0
# for i in range(2, limit):
#     count, product = 0, 1
#     if i % 2 == 1:
#         continue
#     if i in primes:
#         continue
#     prime_factor = math_tools.prime_factorization(i, primes)
#     nums = set()
#
#     for x in prime_factor:
#         count += i / x
#
#     if count > max_counter:
#         max_counter = count
#         max_n = i
#         print(i, max_counter)


# for x in prime_factor:
#     y = x
#     while y <= i:
#         nums.add(y)
#         y += x
# count = i - len(nums)
#
# phi = i / count
# if phi > max_n:
#     print(i, phi)
#     max_n = phi
