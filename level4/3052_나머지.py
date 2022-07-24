import sys

input_list = []

for _ in range(10):
    input_list.append(int(sys.stdin.readline()))

mod_set = set()

for n in input_list:
    mod_set.add(n % 42)

print(len(mod_set))