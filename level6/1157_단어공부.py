word = input()

word = word.upper()

dict = dict()

for char in word:
    if char in dict.keys():
        dict[char] += 1
    else:
        dict[char] = 1
    
sorted = sorted(dict.items(), key=lambda x: x[1], reverse=True)

if len(dict) > 1:
    if sorted[0][1] == sorted[1][1]:
        print('?')
    else:
        print(sorted[0][0])
else:
    print(sorted[0][0])