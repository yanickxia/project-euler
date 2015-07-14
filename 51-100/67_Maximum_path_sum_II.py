__author__ = 'Yann'

# read numbers
input_file = open('p067_triangle.txt')
numbers = []

for line in input_file.readlines():
    line_number = line.split('\n')[0].split(' ')
    numbers.append(line_number)

size = len(numbers)

for i in range(size - 2, -1, -1):
    for j in range(0, i + 1):
        sum_1 = int(numbers[i][j]) + int(numbers[i + 1][j])
        sum_2 = int(numbers[i][j]) + int(numbers[i + 1][j + 1])
        if sum_1 > sum_2:
            numbers[i][j] = sum_1
        else:
            numbers[i][j] = sum_2

print(numbers[0][0])
