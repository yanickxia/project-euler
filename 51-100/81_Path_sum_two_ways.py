__author__ = 'Yann.Xia'

f = open('p081_matrix.txt')

numbers = []

for line in f.readlines():
    number = line.split(',')
    number = [int(i) for i in number]
    numbers.append(number)

indexs = [[0, 0, numbers[0][0]]]
max_size = 79


def clean_point(indexs:list):
    for i in indexs:
        for j in indexs:
            if i != j and i[0] == j[0] and i[1] == j[1]:
                minin = min(i[2], j[2])
                i[2] = minin
                indexs.remove(j)


def check_point(indexs:list):
    flag = True
    for i in indexs:
        if i[0] != max_size or i[1] != max_size:
            flag = False
            break
    return flag


flag = True
while flag:
    new_indexs = []
    for index in indexs:
        if index[0] < max_size and index[1] < max_size:
            new_indexs.append([index[0] + 1, index[1], index[2] + numbers[index[0] + 1][index[1]]])
            new_indexs.append([index[0], index[1] + 1, index[2] + numbers[index[0]][index[1] + 1]])
        elif index[0] < max_size:
            new_indexs.append([index[0] + 1, index[1], index[2] + numbers[index[0] + 1][index[1]]])
        elif index[1] < max_size:
            new_indexs.append([index[0], index[1] + 1, index[2] + numbers[index[0]][index[1] + 1]])
        clean_point(new_indexs)

    indexs = new_indexs
    flag = not check_point(new_indexs)

print(indexs)
