n = int(input())

table = []
while n:
    n -= 1
    a, b = map(int, input().split())
    table.append((a, b))
    
l = len(table)
score_list = []
for i in range(l):
    score = 0
    for j in range(l):
        if j != i:
            if table[i][0] < table[j][0] and table[i][1] < table[j][1]:
                score += 1
    score_list.append(score + 1)

for i in score_list:
    print(i, end=' ')