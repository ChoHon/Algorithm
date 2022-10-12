import sys
from heapq import *
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
arr = [list(input().strip()) for x in range(n)]


def break_wall_maze(arr):
    visited = [[[0] * 2 for x in range(m)] for y in range(n)]

    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    heap = [[1, 1, 0, 0]]

    while heap:
        cnt, chance, x, y = heappop(heap)
        visited[x][y][chance] = 1

        if x == n - 1 and y == m - 1:
            return cnt

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m and visited[nx][ny][chance] == 0:
                if arr[nx][ny] == "0" or (arr[nx][ny] == "1" and chance):
                    visited[nx][ny][chance] = 1
                    if arr[nx][ny] == "1":
                        heappush(heap, [cnt + 1, 0, nx, ny])
                    else:
                        heappush(heap, [cnt + 1, chance, nx, ny])

    return -1


print(break_wall_maze(arr))

"""
6 4
0100
1110
1000
0000
0111
0000
"""
