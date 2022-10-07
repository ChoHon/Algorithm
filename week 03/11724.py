import sys
from collections import deque

sys.setrecursionlimit(10**8)
input = sys.stdin.readline

n, m = map(int, input().split())
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


def connected(graph):
    cnt = 0

    for i in range(len(visited)):
        if not visited[i]:
            dfs(graph, i)
            # bfs(graph, i)
            cnt += 1

    return cnt


print(connected(graph))

"""
6 5
1 2
2 5
5 1
3 4
4 6

6 8
1 2
2 5
5 1
3 4
4 6
5 4
2 4
2 3
"""
