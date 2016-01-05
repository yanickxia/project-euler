# -*- coding:utf-8 -*-

ns = []
n_m = {}
res = []

for i in range(100, 9999):
    n = sorted(str(i * i * i))
    ns.append(n)
    n_m[i] = n

ns = sorted(ns)

i = 0
while i < len(ns) - 1:
    s = ns[i]
    j, count = i + 1, 1
    while s == ns[j]:
        j += 1
        count += 1
    if count == 5:
        res.append(s)
    i = j

kes = []

for rs in res:
    for key, val in n_m.items():
        if val == rs:
            kes.append(key)

print(sorted(kes)[0])
v = sorted(kes)[0] * sorted(kes)[0] * sorted(kes)[0]
print(v)

for key, val in n_m.items():
    if val == sorted(str(v)):
        print(key)

