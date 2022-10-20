import sys
from functools import cache

input = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().split())) for x in range(n)]


@cache
def dfs(x, y):
    if x == n - 1 and y == n - 1:
        return 1

    elif arr[x][y] == 0:
        return 0

    result = 0

    dx = [arr[x][y], 0]
    dy = [0, arr[x][y]]

    for i in range(2):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx < n and ny < n:
            result += dfs(nx, ny)

    return result


print(dfs(0, 0))
