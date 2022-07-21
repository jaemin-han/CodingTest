import  sys
n = int(sys.stdin.readline())

list_ = []
for i in range(1, n + 1):
    a, b = map(int, sys.stdin.readline().split(' '))
    list_.append((a, b))

for i, set_ in enumerate(list_):
    print(f"Case #{i + 1}: {set_[0]} + {set_[1]} = {set_[0] + set_[1]}")