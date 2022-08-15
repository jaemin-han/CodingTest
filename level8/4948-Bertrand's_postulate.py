"""
계산을 위해, 문제 범위인 123456 내부의 모든 소수를 미리 구해놓고 사용
"""
def check_prime(n):
    if n == 1:
        return False
    
    sqrt = int(n ** 0.5)
    for i in range(2, sqrt + 1):
        if n % i == 0:
            return False

    return True

prime_list = [i for i in range(1, 2 * 123456 + 1) if check_prime(i)]
1
while True:
    n = int(input())
    if n == 0:
        break
    count = 0
    for i in prime_list:
        if n < i <= 2 * n:
            count += 1

    print(count)