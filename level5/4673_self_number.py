"""
생성자가 없는 양의 정수를 셀프 넘버라고 한다. 예를 들어 51은 57의 생성자이다. 
d(n) 은 n 과 n 의 모든 자릿수의 합이다. n 은 d(n)의 생성자이다.
10000보다 작거나 같은 셀프 넘버를 모두 출력하는 프로그램을 작성하시오

만개짜리 리스트를 만든 다음에 전
"""
def Kaprekar(n):
    result = n
    while n != 0:
        result += n % 10
        n //= 10
    return result

list_ = []
for n in range(1, 10001):
    list_.append(n)

n = 1
while n != 10000:
    if Kaprekar(n) > 10000:
        n += 1
        continue
    list_[Kaprekar(n) - 1] = 0
    n += 1

for n in list_:
    if n != 0:
        print(n)