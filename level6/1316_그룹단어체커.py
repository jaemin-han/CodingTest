"""
하...이걸 어캐 구현하지?? 머리가 아프네..
find와 rfind 로 처음, 마지막을 찾고 그 둘이 같거나, 그 사이의 charater들이 모두 같은 문자임을 판별하자

아니면 각 위 기능을 그냥 구현할 수도.. find, rfind 안 쓰고 구현해보자
"""
import sys
N = int(input())
word_list = []
for _ in range(N):
    word_list.append(sys.stdin.readline().rstrip())

abc_list = ""
for i in range(ord('z') - ord('a') + 1):
    abc_list += chr(ord('a') + i)

group_number = 0

for word in word_list:
    check = True
    for abc in abc_list:
        if abc not in word:
            continue

        start = 0
        for char in word:
            if char == abc:
                break
            start += 1

        end = len(word) - 1
        for char in word[::-1]:
            if char == abc:
                break
            end -= 1
        
        if end - start > 1:
            for i in range(start + 1, end + 1):
                if word[i] != abc:
                    check = False # 해당 word는 그룹 단어가 아님을 나타내야하는데..
                    break
        
        if not check:
            break
    if check:
        group_number += 1

print(group_number)