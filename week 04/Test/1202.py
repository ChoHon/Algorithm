# 시간초과
# 틀림

import sys
from heapq import *
from bisect import *


input = sys.stdin.readline

n, k = map(int, input().split())
j_arr = [tuple(map(int, input().split())) for x in range(n)]
b_arr = [int(input()) for x in range(k)]


def jewel_thief(j_arr, b_arr):
    j_arr = [(-y, x) for x, y in j_arr]
    b_arr.sort()
    heapify(j_arr)

    result = 0
    while b_arr and j_arr:
        value, jewel_w = heappop(j_arr)
        value = -value

        idx = bisect_left(b_arr, jewel_w)
        if idx > len(b_arr) - 1:
            continue

        result += value
        del b_arr[idx]

    return result


print(jewel_thief(j_arr, b_arr))
