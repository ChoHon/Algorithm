import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**8)

k = int(input())
arr = []
for _ in range(k):
    v, e = map(int, input().split())
    temp = [list(map(int, input().split())) for x in range(e)]
    arr.append([[v, e]] + temp)


def dfs(graph, v, color):
    global is_bipartite

    visited[v] = True

    if colored[v] == -1:
        colored[v] = color

    for node in graph[v]:

        if colored[node] == color:
            is_bipartite = False

        if not visited[node]:
            dfs(graph, node, (not color))

    return


for temp in arr:
    graph = [[] for x in range(temp[0][0] + 1)]
    for v1, v2 in temp[1:]:
        graph[v1].append(v2)
        graph[v2].append(v1)

    visited = [False] * (temp[0][0] + 1)
    colored = [-1] * (temp[0][0] + 1)
    is_bipartite = True

    for i in range(temp[0][0] + 1):
        if not visited[i]:
            dfs(graph, i, True)

    if is_bipartite:
        print("YES")
    else:
        print("NO")

"""
2
3 2
1 3
2 3
4 4
1 2
2 3
3 4
4 2

1
5 4
1 2
1 3
2 4
3 5
"""
