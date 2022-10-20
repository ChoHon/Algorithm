import sys
from functools import cache

input = sys.stdin.readline
sys.setrecursionlimit(10**9)

n = int(input())
arr = [list(map(int, input().split())) for x in range(n)]


@cache
def panda(x, y):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    max_move = 0

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < n and 0 <= ny < n and arr[nx][ny] > arr[x][y]:
            max_move = max(max_move, panda(nx, ny))

    return max_move + 1


result = 0
for i in range(n):
    for j in range(n):
        result = max(result, panda(i, j))

print(result)
