import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
m = int(input())
arr = [sorted(list(map(int, input().split()))) for x in range(m)]
arr.sort()

graph = [[] for x in range(n + 1)]
for v1, v2 in arr:
    graph[v1].append(v2)
    graph[v2].append(v1)

visited = [False] * (n + 1)
visited[0] = True


def dfs(graph, v):
    visited[v] = True

    for node in graph[v]:
        if not visited[node]:
            dfs(graph, node)

    return


def bfs(graph, v):
    que = deque([v])

    while que:
        pop = que.popleft()
        if visited[pop]:
            continue

        visited[pop] = True

        for node in graph[pop]:
            que.append(node)

    return


def virus(graph):
    cnt = 0

    dfs(graph, 1)
    # bfs(graph, 1)

    for temp in visited[1:]:
        if temp:
            cnt += 1

    return cnt - 1


print(virus(graph))

"""
7
6
1 2
2 3
1 5
5 2
5 6
4 7
"""
