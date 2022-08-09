a, b = map(list, input().split())

a.reverse()
b.reverse()

if len(a) != len(b):
    if len(a) > len(b):
        for i in range(len(a) - len(b)):
            b.append('0')
    if len(b) > len(a):
        for i in range(len(b) - len(a)):
            a.append('0')

c = []
C = 0
for A, B in zip(a, b):
    A, B = map(int, (A, B))
    sum = A + B + C
    c.append(sum if sum < 10 else sum % 10)
    if sum > 9:
        C = 1
    else:
        C = 0
    
if C:
    c.append(C)

c.reverse()
for i in range(len(c)):
    c[i] = str(c[i])

print("".join(c))