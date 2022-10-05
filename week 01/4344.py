def over_average(n, l):
    avg = sum(l) / n

    count = 0
    for i in l:
        if i > avg:
            count += 1

    return format(count / n * 100, '.3f')

t = int(input())
for i in range(t):
    l = list(map(int, input().split()))
    print(str(over_average(l[0], l[1:])) + '%')