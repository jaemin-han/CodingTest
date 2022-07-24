a = int(input())
b = int(input())
c = int(input())

abc = a * b * c

list_ = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

while abc != 0:
    list_[abc % 10] += 1
    abc //= 10


for i in list_:
    print(int(i))