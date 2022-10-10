import sys

input = sys.stdin.readline

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for x in range(n)]


def iceberg(arr):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    cnt = 0

    graph = dict()
    for x in range(n):
        for y in range(m):
            if arr[x][y]:
                linked = []

                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]

                    if 0 <= nx < n and 0 <= ny < m and arr[nx][ny]:
                        linked.append((nx, ny))

                graph[(x, y)] = [arr[x][y], linked, False]

    while graph:
        for ice in graph.keys():
            graph[ice][2] = False

        que = [list(graph.keys())[0]]

        while que:
            pop = que.pop()

            if graph[pop][2]:
                continue
            graph[pop][2] = True

            for ice in graph[pop][1]:
                que.append(ice)

        for ice in graph.keys():
            if not graph[ice][2]:
                return cnt

        cnt += 1
        for ice in graph.keys():
            graph[ice][0] -= 4 - len(graph[ice][1])

        for ice in list(graph.keys()):
            if graph[ice][0] <= 0:
                for near in graph[ice][1]:
                    graph[near][1].remove(ice)
                del graph[ice]

    return 0


print(iceberg(arr))

"""
5 7
0 0 0 0 0 0 0
0 2 4 5 3 0 0
0 3 0 2 5 2 0
0 7 6 2 4 0 0
0 0 0 0 0 0 0
"""
