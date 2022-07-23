import sys

n = int(sys.stdin.readline())

i = 0
n_ = n
while True:
    i += 1
    n = (n % 10) * 10 + (n // 10 + n % 10) % 10
    if n_ == n:
        break
print(i)