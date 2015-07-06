__author__ = 'Yann'


def is_integer(n):
    n = str(n)
    ns = n.split('.')
    if len(ns) == 1:
        return True
    return ns[1] == '0'
