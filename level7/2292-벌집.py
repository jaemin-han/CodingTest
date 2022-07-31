"""
시작을 1번째 껍질이라고 한다면 2째 껍질, 3쨰 껍질 ... 이런 식으로 숫자 n이 몇 번째 껍질에 해당하는지를 출력하는 문제
규칙은 1 -> 6 -> 12 -> 18 -> 24 즉 6의 배수만큼 증가함
이제 규칙을 찾았으니 몇 번째 껍질인지 어떻게 알꺼냐.. 
일단 N = 1 일 때는 1 번째 껍질, 아닌 경우는 N 에 1을 뺴줌
그리고 6보다 작다면 2 번쨰, 아니면 N에 6을 빼줌
그리고 12보다 작다면 3 번쨰, 아니면 N에 12를 빼줌
"""
def main(N):
    if N == 1:
        return 1
    N -= 1
    orbital = 1
    while True:
        if N <= 6 * orbital:
            return orbital + 1
        else:
            N -= 6 * orbital
            orbital += 1

N = int(input())

print(main(N))