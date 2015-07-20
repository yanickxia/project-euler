__author__ = 'Yann'

from collections import deque

keys = []
f = open('p079_keylog.txt')
for line in f.readlines():
    keys.append(line.split('\n')[0])

# get all number
numbes = set()
for key in keys:
    for char in key:
        numbes.add(char)

# find index of number
size = 10
index_numbers = [None] * size

for key in keys:
    for char_index in range(len(key)):
        index = int(key[char_index])
        if index_numbers[index] == None:
            index_numbers[index] = set()
        for j in range(char_index + 1, len(key)):
            index_numbers[index].add(key[j])

sorted_numbers = {}

for i in range(size):
    if index_numbers[i] != None:
        index_numbers[i] = len(index_numbers[i])

for i in range(size):
    if index_numbers[i] != None:
        sorted_numbers[i] = index_numbers[i]

sorted_numbers = {value: key for key, value in sorted_numbers.items()}

sorted_number = ''
for key in sorted_numbers.keys():
    sorted_number += str(sorted_numbers[key])
sorted_number = sorted_number[::-1]

print(sorted_number)
