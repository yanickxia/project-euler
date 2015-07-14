__author__ = 'Yann'

import math


def find_all_right_angle_triangle(p):
    lst = []
    for x in range(int(p / 3), int(p / 2)):
        for y in range(int((p - x) / 2), x):
            z = p - x - y
            if z < y and x + y > z and x + z > y and z + y > x:
                if math.pow(x, 2) == math.pow(y, 2) + math.pow(z, 2):
                    lst.append([x, y, z])
    return lst


max_solutions = 0
number = 0
for i in range(3, 1001):
    solutions = len(find_all_right_angle_triangle(i))
    if solutions > max_solutions:
        max_solutions = solutions
        number = i
print(max_solutions, number)
