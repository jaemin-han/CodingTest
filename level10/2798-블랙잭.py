def combination(num_list):
    l = len(num_list)
    result = []

    i = 0
    for i in range(l):
        for j in range(i + 1, l):
            for k in range(j + 1, l):
                result.append([num_list[i],
                num_list[j],
                num_list[k]])
    return result

n, m = map(int, input().split())

num_list = list(map(int, input().split()))

comb_list = combination(num_list)

sum_list = [sum(i) - m for i in comb_list if sum(i) - m <= 0]

sum_list.sort(reverse=True)

print(m + sum_list[0])