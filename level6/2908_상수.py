"""
두 수를 받은 다음에, 각 수를 거꾸로 만든 후 대를 비교한다
"""
A, B = input().split()

A = int(A[::-1])
B = int(B[::-1])

print(A if A > B else B)