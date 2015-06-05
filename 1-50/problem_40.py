__author__ = 'Yann'

s = ''

for i in range(0, 1000000):
    s += str(i)

i = 1
s_s = 1
while i <= 1000000:
    s_s *= int(s[i])
    i *= 10

print(s_s)
