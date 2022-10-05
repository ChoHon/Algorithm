from heapq import *
import sys

input = sys.stdin.readline

n = int(input())
arr = [int(input()) for x in range(n)]


def sort_card(arr):
    heapify(arr)
    anw = 0

    while len(arr) > 1:
        first = heappop(arr)
        second = heappop(arr)

        anw += first + second

        heappush(arr, first + second)

    return anw


print(sort_card(arr))
