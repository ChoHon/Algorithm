n = int(input())
l = list(map(int, input().split()))
oper_l = list(map(int, input().split()))

max_ = -1e9
min_ = 1e9

def divide(a, b):
    if a < 0 and b > 0:
        return ((a * -1) // b) * -1
    else:
        return a // b

def insert_oper(o, n, l, oper_l, result):
    global max_, min_

    if o == n - 1:
        max_ = max(max_, result)
        min_ = min(min_, result)
    
    else:
        if oper_l[0] > 0:
            oper_l[0] -= 1
            insert_oper(o + 1, n, l, oper_l, result + l[o + 1])
            oper_l[0] += 1
        
        if oper_l[1] > 0:
            oper_l[1] -= 1
            insert_oper(o + 1, n, l, oper_l, result - l[o + 1])
            oper_l[1] += 1

        if oper_l[2] > 0:
            oper_l[2] -= 1
            insert_oper(o + 1, n, l, oper_l, result * l[o + 1])
            oper_l[2] += 1

        if oper_l[3] > 0:
            oper_l[3] -= 1
            insert_oper(o + 1, n, l, oper_l, divide(result, l[o + 1]))
            oper_l[3] += 1

insert_oper(0, n, l, oper_l, l[0])
print(max_, min_)