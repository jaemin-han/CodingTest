subject_number = int(input())

score_list = list(map(int, input().split(' ')))

revised_score = [n / max(score_list) * 100 for n in score_list]

print(sum(revised_score) / subject_number)