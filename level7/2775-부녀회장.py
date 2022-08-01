"""
부녀회장이랑은 아무 상관이 없는 것 같은데.??
recursion 방법으로 풀었더니 시간 초과가 떳다.

첫 번째 층 리스트를 만들고 층을 업데이트 하는 방식으로 진행하자.. 
나는 특별한 규칙이 있을 줄 알았는데 그냥 리스트에 때려박는 방식이었네
"""
def resident(k, n):
    each_floor = [i for i in range (1, n + 1)]
    for i in range(k):
        for j in range(1, n):
            each_floor[j] += each_floor[j - 1]
    return each_floor[-1]
            


import sys
t = int(input())

list_ = []
for _ in range(t):
    k = int(sys.stdin.readline())
    n = int(sys.stdin.readline())
    list_.append(resident(k, n))

for i in list_:
    print(i)
