
import sys

n, x = map(int, sys.stdin.readline().split(' '))

list_ = list(map(int, sys.stdin.readline().split(' ')))

for i in list_:
    if i < x:
        print(i, end=' ')
