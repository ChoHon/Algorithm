a, b, c = [int(input()) for x in range(3)]

def count_number(a, b, c):
    n = a * b * c
    dic = {}
    for i in range(10):
        dic[i] = 0

    while n > 0:
        p_n = n % 10
        n = n // 10

        dic[p_n] += 1

    return dic

dic = count_number(a, b, c)
for p in dic:
    print(dic[p])
