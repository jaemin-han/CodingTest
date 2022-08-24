def hanoi(n, a, b, c):
    if n == 1:
        print(a, b)
        return

    hanoi(n - 1, a, c, b)
    print(a, b)
    hanoi(n - 1, c, b, a)

def count(n):
    if n == 1:
        return 1
    return 2 * count(n - 1) + 1

n = int(input())
print(count(n))
hanoi(n, 1, 3, 2)