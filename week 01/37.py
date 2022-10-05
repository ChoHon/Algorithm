from itertools import permutations
from copy import deepcopy

def cul_diff(n, l):
    temp_l = [abs(l[x] - l[x - 1]) for x in range(1, n)]
    return sum(temp_l)

def cul_diff_one(sum_, pre, new):
    return sum_ + abs(pre - new)

anw = 0
def max_diff(o, n, l, sum_, pre):
    global anw

    if o == n:
        anw = max(anw, sum_)

    else:
        for i in l:
            temp_l = deepcopy(l)
            temp_l.remove(i)

            if o == 0:
                max_diff(o + 1, n, temp_l, 0, i)
                continue

            max_diff(o + 1, n, temp_l, cul_diff_one(sum_, pre, i), i)

n = int(input())
l = list(map(int, input().split()))

# anw = [cul_diff(n, x) for x in permutations(l)]

max_diff(0, n, l, 0, 0)
print(anw)