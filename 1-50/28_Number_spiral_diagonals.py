__author__ = 'Yann.Xia'

start_l = 1
start_r = 1

count = 1

s_sum = 0


while count < 1001:
    start_l += count * 2
    if count % 2 == 1:
        start_r += (count + 1) * 2
    else:
        start_r += count * 2
    count += 1
    s_sum += start_l
    s_sum += start_r
    print(start_l, start_r)

print(s_sum + 1)