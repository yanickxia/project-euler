__author__ = 'Yann'

from utils.math_tools import *

lychrels = 0

for i in range(1, 10000):
    lychrel = True
    for j in range(50):
        if isPalindrome(i) and j != 0:
            lychrel = False
            break
        else:
            i += int(str(i)[::-1])

    if lychrel:
        lychrels += 1

print(lychrels)
