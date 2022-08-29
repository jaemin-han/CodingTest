def digit_sum(n):
    sum = n
    while n:
        sum += n % 10
        n //= 10
    return sum

n = int(input())
m = n - 1
gen = 0
while m:
    if digit_sum(m) == n:
        gen = m
    m -= 1

print(gen)