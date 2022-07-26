"""
ord, chr, find, index
"""
s = input()

list_ = []

for i in range(ord('z') - ord('a') + 1):
    try:
        list_.append(s.index(chr(i + ord('a'))))
    except:
        list_.append(-1)

for i in list_:
    print(i, end=' ')