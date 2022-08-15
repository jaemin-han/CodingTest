def check_prime(n):
    if n == 1:
        return False
    
    sqrt = int(n ** 0.5)
    for i in range(2, sqrt + 1):
        if n % i == 0:
            return False

    return True


def main():
    m, n = map(int, input().split())
    for i in range(m, n + 1):
        print(f"{i}\n" if check_prime(i) else '', end='')

if __name__ == '__main__':
    main()