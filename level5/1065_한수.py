"""
양의 정수 x가 등차수열을 이루어야 한다.
전에 4673 다른 풀이에서 본 정수를 문자열로 바꿔서 각 자릿수에 접근하는 방법을 사용하자
문자열의 길이를 받은 다음 for문에 넣어서 비교하는 작업을 하자

"""
def check_han(n):
    str_ = str(n)
    len_ = len(str_)
    if len_ <= 2:
        return True
    interval = int(str_[0]) - int(str_[1])
    for i in range(1, len_ - 1):
        if interval != int(str_[i]) - int(str_[i + 1]):
            return False
    return True


n = int(input())
count = 0

for i in range(1, n + 1):
    if check_han(i):
        count += 1

print(count)
