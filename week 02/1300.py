from bisect import *
import sys

input = sys.stdin.readline

n = int(input())
k = int(input())


def count_below(num):
    cnt = 0
    for row in range(1, n + 1):
        cnt += min((num - 1) // row, n)
    return cnt


def find_kth(n, k):
    start = 1
    end = n * n
    anw = 0

    while start <= end:
        mid = (start + end) // 2

        if count_below(mid) >= k:
            end = mid - 1

        else:
            start = mid + 1
            anw = mid

    return anw


print(find_kth(n, k))
