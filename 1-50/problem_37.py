__author__ = 'Yann'


def find_prime_less_n_v2(n):
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


primes = find_prime_less_n_v2(9999999)

sum_n = 0
count = 0
for i in range(9, 9999999):
    if primes[i] != 0:  # is primes

        # left to right
        k = primes[i]
        flag = 1
        while k > 0:
            # primes[k] != 0
            if primes[k] == 0:
                flag = 0
            k = int(k / 10)

        if flag == 1:
            # right to letf
            j = primes[i]
            while j > 0:
                if primes[j] == 0:
                    flag = 0
                if j > 9:
                    j = int((str(j))[1:])
                else:
                    j = int(j / 10)

        if flag == 1:
            sum_n += primes[i]
            count += 1
        if count == 11:
            break

print(count, sum_n)
