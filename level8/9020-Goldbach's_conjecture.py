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

prime_list = [i for i in range(2, 10000) if check_prime(i)]

n = int(input())

for _ in range(n):
    m = int(input())
    m //= 2
    if m in prime_list:
        print(m, m)
        continue
    for i in range(1, m):
        if m - i in prime_list and m + i in prime_list:
            print(m - i, m + i)
            break
    
