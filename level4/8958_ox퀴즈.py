import sys

n = int(input())

ox_list = []
for _ in range(n):
    ox_list.append(sys.stdin.readline().rstrip())


score_list = []
for string in ox_list:
    count = 0
    score = 0
    for char in string:
        if char == 'X':
            count = 0
        elif char == 'O':
            count += 1
        score += count
    score_list.append(score)

for score in score_list:
    print(score)