"""
주사위 세 개를 던져서 같은 눈의 수가 몇 개인지 알아야 한다. 걍 간단하게 구현하자
"""
a, b, c = map(int, input().split(' '))

if a == b & b == c:
    print(1e4 + a * 1e3)
elif a == b:
    print(1e3 + a * 100)
elif b == c:
    print(1e3 + b * 100)
elif c == a:
    print(1e3 + c * 100)
else:
    if a > b & a > c:
        print()
