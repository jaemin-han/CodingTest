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

m = int(input())
n = int(input())

list_ = list(range(m, n + 1))
prime_list = [i for i in list_ if check_prime(i)]

print(f"{sum(prime_list)}\n{prime_list[0]}" if len(prime_list) != 0 else -1)
