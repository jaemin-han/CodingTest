import sys

def check_prime(n):
    if n == 1:
        return False
    elif n <= 3:
        return True
    else:
        i = 2
        while i ** 2 <= n:
            if n % i == 0:
                return False
            else:
                i += 1
        return True

n = int(input())
if n == 1:
    sys.exit(0)
i = 0
while i ** 2 < n:
    i += 1
# 이제 i에 n의 제곱근보다 크면서 n의 제곱근과 가장 가까운 정수가 들어있음
prime_list = [j for j in range(1, i + 1) if check_prime(j)]
# prime_list에 i보다 작거나 같은 소수들이 들어있음
while not check_prime(n):
    for k in prime_list:
        if n % k == 0:
            print(k)
            n //= k
            break

print(n)