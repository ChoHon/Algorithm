import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
arr = [list(input().strip()) for x in range(n)]


def maze(arr):
    finish = [n - 1, m - 1]
    que = deque([[0, 0]])
    arr[0][0] = 1
    direction = [[1, 0], [-1, 0], [0, 1], [0, -1]]

    while que:
        x, y = que.popleft()

        for i in range(4):
            dx = x + direction[i][0]
            dy = y + direction[i][1]

            if 0 <= dx < n and 0 <= dy < m and arr[dx][dy] == "1":
                que.append([dx, dy])
                arr[dx][dy] = arr[x][y] + 1

    return arr[n - 1][m - 1]


print(maze(arr))

"""
4 6
101111
101010
101011
111011
"""
