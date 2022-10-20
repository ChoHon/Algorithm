import sys
from heapq import *


input = sys.stdin.readline

n, k = map(int, input().split())
j_arr = [tuple(map(int, input().split())) for x in range(n)]
b_arr = [int(input()) for x in range(k)]


def jewel_thief(j_arr, b_arr):
    heapify(j_arr)
    b_arr.sort()

    result = 0
    temp_arr = []
    for bag_w in b_arr:
        while j_arr and j_arr[0][0] <= bag_w:
            weight, value = heappop(j_arr)
            heappush(temp_arr, -value)

        if temp_arr:
            result -= heappop(temp_arr)

    return result


print(jewel_thief(j_arr, b_arr))

"""
4 2
4 100
5 110
6 90
7 80
5
7

4 4
1 100
2 200
13 300
10 500
10
10
10
14

1100
"""
