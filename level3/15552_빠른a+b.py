import sys

test  = int(sys.stdin.readline())

list_ = []

for i in range(test):
    a, b = map(int, sys.stdin.readline().split(' '))
    list_.append(a + b)

for i in list_:
    print(i)