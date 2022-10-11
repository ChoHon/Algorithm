import sys
from collections import deque

input = sys.stdin.readline

m, n, l = map(int, input().split())
# arr[높이][행][열]
arr = [[list(map(int, input().split())) for x in range(n)] for y in range(l)]


def tomato(arr):
    dh = [1, -1, 0, 0, 0, 0]
    dx = [0, 0, 1, -1, 0, 0]
    dy = [0, 0, 0, 0, 1, -1]

    # 모든 익은 토마토 위치 탐색
    que = deque([])
    for i in range(l):
        for j in range(n):
            for k in range(m):
                if arr[i][j][k] == 1:
                    que.append([i, j, k])

    while que:
        h, x, y = que.popleft()

        for i in range(6):
            nh = h + dh[i]
            nx = x + dx[i]
            ny = y + dy[i]

            # 익은 토마토 주변의 안 익은 토마토가 익게 만듬
            if 0 <= nh < l and 0 <= nx < n and 0 <= ny < m and arr[nh][nx][ny] == 0:
                que.append([nh, nx, ny])
                # 자신이 익은 시간 + 1
                arr[nh][nx][ny] = arr[h][x][y] + 1

    max_dist = 0
    for i in arr:
        for j in i:
            for k in j:
                if k == 0:
                    return -1

                else:
                    max_dist = max(max_dist, k)

    return max_dist - 1


print(tomato(arr))


"""
5 3 1
0 -1 0 0 0
-1 -1 0 1 1
0 0 0 1 1

5 3 2
0 0 0 0 0
0 0 0 0 0
0 0 0 0 0
0 0 0 0 0
0 0 1 0 0
0 0 0 0 0
"""
