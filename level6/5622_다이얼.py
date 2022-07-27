"""
일단 대문자 알파벳 문자열을 받음
그걸 숫자로 변환해야함
딕셔너리에 변환표를 저장함

"""
phone_number = input()

number_alphabet = {2:"ABC", 3:"DEF", 4:"GHI", 5:"JKL", 6:"MNO", 7:"PQRS", 8:"TUV", 9:"WXYZ"}

phone_number_converted = []
for char in phone_number:
    for key, value in number_alphabet.items():
        if char in value:
            phone_number_converted.append(key)
            break  

print(sum(phone_number_converted) + len(phone_number_converted))