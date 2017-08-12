import unittest


class Solution(object):
    def sum_s(self, n):
        c = 0
        for i in range(2, n):
            c += self.s(i)

        return c

    def s(self, n):
        return self.__s__(1, n)

    def __s__(self, i, n):
        while True:
            if n > i and n % i == 0:
                n /= i
            elif n <= i and i % n == 0:
                return i
            i += 1


class SolutionTest(unittest.TestCase):
    def test_s(self):
        s = Solution()
        self.assertEqual(s.s(10), 5)
        self.assertEqual(s.s(25), 10)

        print(s.sum_s(10 ** 8))
