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


print(count_below(6))


def find_kth(n, k):
    start = 1
    end = n * n

    mid = (start + end) // 2

    if count_below(mid) > k:
        end = mid - 1

    else


    return


# print(find_kth(n, k))
