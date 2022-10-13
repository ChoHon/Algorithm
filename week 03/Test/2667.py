import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
arr = [list(map(int, list(input().strip()))) for x in range(n)]


def solution(arr):
    def dfs(start):
        dx = [1, -1, 0, 0]
        dy = [0, 0, 1, -1]

        que = [start]
        cnt = 0

        while que:
            cur_v = que.pop()
            x, y = cur_v

            if arr[x][y] == 0:
                continue
            arr[x][y] = 0
            cnt += 1

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if 0 <= nx < n and 0 <= ny < n and arr[nx][ny] == 1:
                    que.append((nx, ny))

        return cnt

    result = 0
    house = []
    for i in range(n):
        for j in range(n):
            if arr[i][j]:
                result += 1
                house.append(dfs((i, j)))

    return result, house


result, house = solution(arr)
print(result)
for temp in sorted(house):
    print(temp)

"""
7
0110100
0110101
1110101
0000111
0100000
0111110
0111000
"""
