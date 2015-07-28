__author__ = 'Yann'

ls = []
for i in range(1, 10):
    n_power = 1
    while True:
        n = str(i ** n_power)
        if len(n) == n_power:
            ls.append([i, n_power])
        if len(n) < n_power:
            break
        n_power += 1

print(ls)
print(len(ls))

print(sum(len(str(i ** j)) == j for i in range(1, 50) for j in range(1, 50)))
