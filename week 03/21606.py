import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**8)

n = int(input())
a = input().strip()
arr = [sorted(list(map(int, input().split()))) for x in range(n - 1)]
arr.sort()

graph = [[] for x in range(n + 1)]
for v1, v2 in arr:
    graph[v1].append(v2)
    graph[v2].append(v1)

visited = [False] * (n + 1)
is_inside = [False] * (n + 1)
for i in range(n):
    if a[i] == "1":
        is_inside[i + 1] = True

result = []


def dfs(graph, v, route):
    route.append(v)

    if len(route) > 1 and is_inside[v]:
        result.append(route)
        return

    visited[v] = True

    for node in graph[v]:
        if not visited[node]:
            dfs(graph, node, route[:])

    return


for i in range(1, n + 1):
    if is_inside[i]:
        visited = [False] * (n + 1)
        dfs(graph, i, [])

print(len(result))


"""
5
10111
1 2
2 3
2 4
4 5
"""
