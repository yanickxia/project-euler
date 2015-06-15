__author__ = 'Yann'

lst = []
for i in range(10, 100):
    for j in range(10, 100):
        if i < j:
            if i % 10 == 0 and j % 10 == 0:
                break

            x = [str(i)[0], str(i)[1]]
            y = [str(j)[0], str(j)[1]]
            for x_i in x:
                if x_i in y:
                    x.remove(x_i)
                    y.remove(x_i)

                    x = int(x[0])
                    y = int(y[0])
                    if y != 0 and x / y == i / j:
                        lst.append([x, y])
                    break

print(lst)

n_s = 1
for i in lst:
    n_s *= i[1]
    n_s /= i[0]
print(n_s)