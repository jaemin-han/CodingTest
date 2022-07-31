"""
특이사항으로 시간 제한이 0.15 s = 150 ms 이다. 이는 반복문? 형태로 풀 지 말라는 의미인 듯 하다.
일단 달팽이가 첫날 낮에 다 오르는 경우는 1을 출력한다
그리고 첫날에 다 오르지 못하는 경우,
일단 달팽이가 밤을 지나고 아침이 되었을 때 남은 높이가 a 이하라면 당일 낮에 다 오를 수 있다.
따라서 (v - a) // (a - b) + 1 이 답이 아닐까?

달팽이가 n날 밤을 지나고 남은 높이가 a 이하라면..인데 n날 밤이란?
일단 v 를 (a - b) 로 나눈 나머지가 0이라면, 그 몫보다 하나 작은 값이거나
아니면 그 몫
"""
# def main():
#     a, b, v = map(int, input().split())
#     if a >= v:
#         print(1)
#         return
#     if v % (a - b) == 0:
#         quotient = v // (a - b) - 1
#     else:
#         quotient = v // (a - b)
#     if v - (quotient - 1) * (a - b) <= a:
#         print(quotient)
#     else:
#         print(quotient + 1)
    
def main():
    a, b, v = map(int, input().split())
    if a >= v:
        print(1)
    elif v - a <= a - b:
        print(2)
    else:
        print((v - a) // (a - b) + 1)

while True:
    main()