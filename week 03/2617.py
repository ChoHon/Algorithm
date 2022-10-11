import sys

input = sys.stdin.readline

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for x in range(m)]


def bead(arr):
    mid = (n + 1) // 2
    anw = 0
    graph = {x: [[], []] for x in range(1, n + 1)}
    for v1, v2 in arr:
        graph[v2][0].append(v1)
        graph[v1][1].append(v2)

    def dfs(start, graph, k):
        visited = [False] * (n + 1)

        cnt = 0
        que = graph[start][k][:]

        while que:
            pop = que.pop()

            if visited[pop]:
                continue
            visited[pop] = True

            cnt += 1
            if cnt >= mid:
                return True

            for v in graph[pop][k]:
                if not visited[v]:
                    que.append(v)

        return False

    for i in range(1, n + 1):
        if dfs(i, graph, 0):
            anw += 1

        elif dfs(i, graph, 1):
            anw += 1

    return anw


print(bead(arr))

"""
5 4
2 1
4 3
5 1
4 2

5 4
2 1
2 1
2 1
2 1
"""
