import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**8)

n = int(input())
arr = [sorted(list(map(int, input().split()))) for x in range(n - 1)]
arr.sort()

graph = [[] for x in range(n + 1)]
for v1, v2 in arr:
    graph[v1].append(v2)
    graph[v2].append(v1)

visited = [False] * (n + 1)
result = [0] * (n + 1)


def find_parent(graph, v, parent):
    result[v] = parent
    visited[v] = True

    for node in graph[v]:
        if not visited[node]:
            find_parent(graph, node, v)

    return


find_parent(graph, 1, 0)
for temp in result[2:]:
    print(temp)

"""
7
1 6
6 3
3 5
4 1
2 4
4 7

12
1 2
1 3
2 4
3 5
3 6
4 7
4 8
5 9
5 10
6 11
6 12
"""
