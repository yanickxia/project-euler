__author__ = 'Yann'

def find_prime_less_n(n):
    # init primes to [0 ... n]
    primes = []
    for i in range(0, n):
        primes.append(i)
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

    return primes


def next_circular_number(n):
    last_number = n % 10
    n = int(n / 10)
    j = n
    while j > 0:
        last_number *= 10
        j = int(j / 10)
    return last_number + n


def all_circular_numbers(n):
    all_circular_number = []
    s = str(n)
    s_size = len(s)
    for i in range(0, s_size):
        s = s[s_size - 1] + s
        s = s[0:s_size]

        if not n_larger_than_i_one(n, int(s)):
            all_circular_number.append(int(s))

    return all_circular_number


# if n = 123, i = 23 return True
def n_larger_than_i_one(n, i):
    count_1 = 0
    while n > 0:
        n = int(n / 10)
        count_1 += 1
    while i > 0:
        i = int(i / 10)
        count_1 -= 1
    if count_1 > 0:
        return True
    return False


print(all_circular_numbers(101))

all_n = 1000000
primes = find_prime_less_n(all_n)

i = 2
while i < all_n:
    if primes[i] == 0:
        i += 1
        continue
    print(i)

    all_circular_number = all_circular_numbers(i)

    for n in all_circular_number:
        # if exist one not primes, set all to 0
        if primes[n] == 0:
            for j in all_circular_number:
                primes[j] = 0
            break
    i += 1

ss = set(primes)
ss.remove(0)
primes = list(ss)

print(primes)
print(len(primes))
