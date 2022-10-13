import sys
from collections import deque
from heapq import *

input = sys.stdin.readline

n, k = map(int, input().split())
arr = [list(map(int, input().split())) for x in range(n)]
s, tx, ty = map(int, input().split())


def virus(arr, k):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    heap = []

    for i in range(n):
        for j in range(n):
            if arr[i][j]:
                heappush(heap, [0, arr[i][j], i, j])
                arr[i][j] = 0

    while heap:
        t, vi, x, y = heappop(heap)

        if t == s + 1:
            break

        if arr[x][y]:
            continue
        arr[x][y] = vi

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n and arr[nx][ny] == 0:
                if not arr[nx][ny]:
                    heappush(heap, [t + 1, vi, nx, ny])

    return arr[tx - 1][ty - 1]


print(virus(arr, k))

"""
3 3
1 0 2
0 0 0
3 0 0
2 3 2
"""
