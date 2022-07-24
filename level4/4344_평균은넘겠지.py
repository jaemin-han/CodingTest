import sys

case_number = int(input())

mean_list = []
for _ in range(case_number):
    student_number, *score_list = map(int, sys.stdin.readline().split(' '))
    mean = sum(score_list) / student_number
    count = 0
    for score in score_list:
        if score > mean:
            count += 1
    mean_list.append(count / student_number * 100)

for percent in mean_list:
    print(f"{round(percent, 3):.3f}%")