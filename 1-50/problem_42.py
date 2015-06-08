__author__ = 'Yann'

import sys

f = open('p042_words.txt')
words = []
for line in f.readlines():
    words = line.split(",")

for i in range(len(words)):
    words[i] = words[i].split('"')[1];

# print(words)




def word_value(word):
    value = 0
    for i in range(len(word)):
        value += ord(word[i]) - 64
    return value


def is_has_value(value, values):
    for i in range(len(values)):
        if value == values[i]:
            return True


def get_values(n):
    values = []
    for i in range(1, n + 1):
        values.append(int(0.5 * i * (i + 1)))

    return values


values = get_values(100)

count = 0
for word in words:
    if is_has_value(word_value(word), values):
        count += 1

print(count)
