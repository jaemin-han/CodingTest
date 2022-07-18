"""
2884 알람 시계 문제와 비슷함
일단 h, m 을 변수로 받고, 두 번째로 time을 받아온다
그리고 time 을 m 에 더해준 후 60으러 나눈 나머지를 분에 할당하고
몫을 시에 더해준다. 그 값이 24보다 크거나 같다면 24로 나눈 나머지를 시간에 할당한다
"""
h, m = map(int, input().split(' '))
time = int(input())

h += (m + time) // 60
m = (m + time) % 60

if h >= 24:
    h %= 24

print(h, m)