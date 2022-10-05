from bisect import *
import sys

input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))


def longest_ascend_part(arr):
    anw_arr = [arr[0]]
    for i in range(1, len(arr)):
        if arr[i] > anw_arr[-1]:
            anw_arr.append(arr[i])

        else:
            anw_idx = bisect_left(anw_arr, arr[i])
            anw_arr[anw_idx] = arr[i]

    return len(anw_arr)


print(longest_ascend_part(arr))
