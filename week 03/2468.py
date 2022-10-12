import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().split())) for x in range(n)]


def safe_area(arr):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    max_h = 0

    graph = dict()
    for x in range(n):
        for y in range(n):
            max_h = max(max_h, arr[x][y])
            linked = []

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if 0 <= nx < n and 0 <= ny < n:
                    linked.append((nx, ny))

                graph[(x, y)] = [arr[x][y], linked, False]

    def bfs(graph, start, h):
        que = deque([start])

        while que:
            cur_v = que.popleft()

            if graph[cur_v][2]:
                continue
            graph[cur_v][2] = True

            for next_v in graph[cur_v][1]:
                if not graph[next_v][2] and graph[next_v][0] > h:
                    que.append(next_v)

        return True

    result = 0
    for h in range(max_h):
        cnt = 0
        for v in graph.keys():
            graph[v][2] = False

        for v in graph.keys():
            if not graph[v][2] and graph[v][0] > h and bfs(graph, v, h):
                cnt += 1
        result = max(result, cnt)
    return result


print(safe_area(arr))


"""
5
6 8 2 6 2
3 2 3 4 6
6 7 3 3 2
7 2 5 3 6
8 9 5 2 7

7
9 9 9 9 9 9 9
9 2 1 2 1 2 9
9 1 8 7 8 1 9
9 2 7 9 7 2 9
9 1 8 7 8 1 9
9 2 1 2 1 2 9
9 9 9 9 9 9 9
"""
