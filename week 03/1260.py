import sys
from collections import deque

input = sys.stdin.readline

n, m, v = map(int, input().split())
arr = [sorted(list(map(int, input().split()))) for x in range(m)]
arr.sort()

graph = [[] for x in range(n + 1)]
for v1, v2 in arr:
    graph[v1].append(v2)
    graph[v2].append(v1)

visited = [False] * (n + 1)


def dfs(graph, v):
    print(v, end=" ")
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
        print(pop, end=" ")

        for node in graph[pop]:
            que.append(node)

    return


dfs(graph, v)
print("")
visited = [False] * (n + 1)
bfs(graph, v)

"""
4 5 1
1 2
1 3
1 4
2 4
3 4

5 5 3
5 4
5 2
1 2
3 4
3 1
"""
