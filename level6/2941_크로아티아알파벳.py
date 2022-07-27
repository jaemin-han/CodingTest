"""
c=, c-, dz=, d-, lj, nj, s=, z= 각각은 하나의 크로아티아 알파벳으로 취급한다
입력된 문자열에 들어간 크로아티아 알파벳의 갯수를 구해라
c = 
  -

d z = 
  -

l j

n j

s =

z =
"""
croa = ["dz=", "c=", "c-", "d-", "lj", "nj", "s=", "z="]

string = input()

for sep in croa:
    string = string.replace(sep, "!")

print(len(string))