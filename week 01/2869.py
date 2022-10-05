import sys

def climb(a, b, v):
    cnt = 1

    once = v - a
    day = a - b

    dnn = once // day

    if dnn * day + a < v:
        dnn += 1

    return cnt + dnn

ipt = sys.stdin.readline()
a, b, v = map(int, ipt.split())
print(climb(a, b, v))
