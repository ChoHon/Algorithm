import sys
from heapq import *

input = sys.stdin.readline
INF = 1e7

n = int(input())
arr = [list(map(int, input().split())) for x in range(n)]

dist_arr = [[0] * (1 << n) for x in range(n)]


def traveling_salesman(start, route):
    if dist_arr[start][route]:
        return dist_arr[start][route]

    if route == (1 << n) - 1:
        return arr[start][0] if arr[start][0] > 0 else INF

    cost = INF
    for i in range(1, n):
        if not route & (1 << i) and arr[start][i]:
            value = traveling_salesman(i, route | (1 << i))
            cost = min(cost, value + arr[start][i])

    dist_arr[start][route] = cost
    return dist_arr[start][route]


print(traveling_salesman(0, 1))
