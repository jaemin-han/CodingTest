import sys

T = int(input())

S_list = []

for _ in range(T):
    R, S = sys.stdin.readline().rstrip().split(' ')
    R = int(R)
    temp = []
    for char in S:
        temp.append(R * char)
    S_list.append("".join(temp))

for str in S_list:
    print(str)