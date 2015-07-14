__author__ = 'Yann'

ways = []


# it's too Brute Force  2*3*5*11*21*41*101*201 = 5768123130
# for x in range(2):
#     for y in range(3):
#         for z in range(5):
#             for k in range(11):
#                 for j in range(21):
#                     for i in range(41):
#                         for m in range(101):
#                             for p in range(201):
#
#                                 if 200 * x + 100 * y + 50 * z + 20 * k + 10 * j + 5 * i + 2 * m + 200 * p == 200:
#                                     one_way = [x, y, z, k, j, i, m, p]


target = 200
coins = [1, 2, 5, 10, 20, 50, 100, 200]
ways = [0] * (target + 1)
ways[0] = 1

for i in range(len(coins)):
    for j in range(coins[i], target + 1):
        ways[j] += ways[j - coins[i]]

print(ways[target])
