import sys
from heapq import *

input = sys.stdin.readline

n, k = map(int, input().split())
arr = list(map(int, input().split()))


def schedule_multitap(n, arr):
    for i in range(k):
        for j in range(i + 1, k + 1):
            if j == k:
                arr[i] = (-101, arr[i])
                break

            if arr[i] == arr[j]:
                arr[i] = (-j, arr[i])
                break

    cnt = 0
    on_arr = []

    for order in arr:
        is_order_on = False
        for on_order in on_arr:
            if order[1] == on_order[1]:
                is_order_on = on_order
                break

        if is_order_on:
            on_arr.remove(is_order_on)
            heapify(on_arr)

        elif not is_order_on and len(on_arr) == n:
            heappop(on_arr)
            cnt += 1

        heappush(on_arr, order)

    return cnt


print(schedule_multitap(n, arr))

"""
4 20
1 2 3 4 5 1 2 3 4 5 1 2 3 4 5 1 2 3 4 5
4

3 14
1 4 3 2 5 4 3 2 5 3 4 2 3 4
4
"""
