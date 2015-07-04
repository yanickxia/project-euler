__author__ = 'Yann.Xia'


class Primes:
    def find_less_n_primes(self, n):
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
        s = set(primes)
        primes = list(s)
        primes.remove(0)
        primes = sorted(primes)

        return primes
