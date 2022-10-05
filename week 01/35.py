def snowwhite(l):
    over = sum(l) - 100

    for i in l:
        if (over / 2) == i:
            continue
        elif (over - i) in l:
            l.remove(i)
            l.remove(over-i)
            return sorted(l)

def snowwhite2(l):
    over = sum(l) - 100

    for i in range(9):
        for j in range(i + 1, 9):
            if l[i] + l[j] == over:
                value1, value2 = l[i], l[j]
                break

    l.remove(value1)
    l.remove(value2)
    return sorted(l)

l = [int(input()) for x in range(9)]

for i in snowwhite2(l):
    print(i)