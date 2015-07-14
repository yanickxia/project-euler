__author__ = 'Yann'

def find_prime_less_n_v3(n):
    # init primes to [0 ... n]
    primes = [1] * n

    # Find all primes
    i = 2
    while i != 0 and n > i:
        j = i + i
        while j < n:
            primes[j] = 0
            j += i
        # Find next not null number
        i += 1
        while i < n and primes[i] == 0:
            i += 1
    primes[1] = 0
    primes[0] = 0

    return primes


def is_pandigital(x):
    count = 0
    x_char_set = set()
    while x > 0:
        x_char_set.add(x % 10)
        x = int(x / 10)
        count += 1

    if count == len(x_char_set):
        return True
    return False


x_max = 0
lst = find_prime_less_n_v3(999999999)
for x in range(0, len(lst)):
    if (lst[x] == 1 and is_pandigital(x)):
        x > x_max
        x_max = x

print(x_max)
