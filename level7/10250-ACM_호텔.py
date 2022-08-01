"""
무조건 각 층의 1호부터 방이 나간다는 알고리즘
1 ~ h 까지는 xx01 호, h + 1 ~ 2h 까지는 xx02호
"""
def find_room(h, w, n):
    number = n % h * 100 if n % h != 0 else h * 100
    number += n // h + 1 if n % h != 0 else n // h
    return number
    
import sys
t = int(input())

room = []
for i in range(t):
    h, w, n = map(int, sys.stdin.readline().split())
    room.append(find_room(h, w, n))

for i in room:
    print(i)