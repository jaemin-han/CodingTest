import sys

n = int(input())

nlist = list(map(int, sys.stdin.readline().split(' ')))
nlist.sort()
print(nlist[0], nlist[n - 1])