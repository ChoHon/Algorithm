import sys
from heapq import *
from collections import deque

input = sys.stdin.readline

n = int(input())
board = [list(input().strip()) for x in range(n)]


def make_maze(board):
    dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]
    visited = [[False] * n for x in range(n)]
    visited[0][0] = True
    heap = [[0, 0, 0]]

    while heap:
        cnt, x, y = heappop(heap)

        if x == n - 1 and y == n - 1:
            return cnt

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == False:
                if board[nx][ny] == "1":
                    heappush(heap, [cnt, nx, ny])
                else:
                    heappush(heap, [cnt + 1, nx, ny])

                visited[nx][ny] = True


print(make_maze(board))

"""
8
11100110
11010010
10011010
11101100
01000111
00110001
11011000
11000111
"""
