import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
arr = [list(input().strip()) for x in range(n)]


def maze(arr):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    finish = [n - 1, m - 1]
    arr[0][0] = 1

    que = deque([[0, 0]])
    while que:
        x, y = que.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m and arr[nx][ny] == "1":
                que.append([nx, ny])
                arr[nx][ny] = arr[x][y] + 1

    return arr[n - 1][m - 1]


print(maze(arr))

"""
4 6
101111
101010
101011
111011
"""
