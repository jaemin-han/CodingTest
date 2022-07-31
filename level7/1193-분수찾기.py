"""
i 번째 껍질에는 i 개의 원소가 들어있다. 일단 X 번째 분수를 구하기 위해서는 얘가 몇 번쨰 껍질에 속한지 부터 구한다.
i 번째 껍질은 1 ~ i - 1 을 합한 수 보다 크고 1 ~ i 를 합한 수 보다 작거나 같다.
"""
def main():
    n = int(input())
    orbital = 0
    while n > sum(range(orbital + 1)):
        orbital += 1
    n -= sum(range(orbital)) # 이제 orbital이 껍질 수가 되고, n은 껍질에서의 몇 번째 수 인지를 나타냄
    numerator = n
    denominator = orbital - n + 1
    print(numerator, '/', denominator, sep='')

while True:
    main()