import sys

nlist = []

for _ in range(9):
    nlist.append(int(sys.stdin.readline()))

print(max(nlist))
print(nlist.index(max(nlist)) + 1)