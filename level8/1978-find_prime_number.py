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

list_ = list(map(int, input().split()))

print(sum(map(check_prime, list_)))