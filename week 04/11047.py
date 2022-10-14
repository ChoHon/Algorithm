import sys
from bisect import *

input = sys.stdin.readline

n, k = map(int, input().split())
arr = [int(input()) for x in range(n)]


def coin(arr, k):
    cnt = 0

    while k:
        i = bisect_right(arr, k) - 1
        v, k = divmod(k, arr[i])
        cnt += v

    return cnt


print(coin(arr, k))
