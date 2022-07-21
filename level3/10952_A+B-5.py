import sys
list_ = []
while True:
    a, b = map(int, sys.stdin.readline().split(' '))
    if a == 0 and b == 0:
        break
    list_.append(a + b)

for i in list_:
    print(i)