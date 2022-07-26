"""
문자열은 공백으로 시작하거나 끝날 수 있다.
"""
string = input().strip().split()
# string = input().strip()

print(len(string))

print(f">{string}<")
print(string)
if string:
    print("이거안비어있음")
"""

"""
# string = input()

# count = 0
# if string[0] != ' ':
#     count = 1

# for i, char in enumerate(string):
#     if i != len(string) - 1 and char == ' ' and string[i + 1] != ' ':
#         count += 1
# print(count)
