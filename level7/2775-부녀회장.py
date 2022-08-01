"""
부녀회장이랑은 아무 상관이 없는 것 같은데.??
recursion 방법으로 풀었더니 시간 초과가 떳다.
"""
def resident(k, n):
    if k == 0:
        return n
    elif n == 1:
        return 1
    return resident(k, n - 1) + resident(k - 1, n)
    
import sys
t = int(input())

list_ = []
for _ in range(t):
    k = int(sys.stdin.readline())
    n = int(sys.stdin.readline())
    list_.append(resident(k, n))

for i in list_:
    print(i)
