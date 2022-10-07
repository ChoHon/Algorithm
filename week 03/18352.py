import sys
from collections import deque

input = sys.stdin.readline
INF = sys.maxsize

n, m, k, x = map(int, input().split())
arr = [list(map(int, input().split())) for x in range(m)]


def find_city(arr, x):
    graph = [[] for x in range(n + 1)]
    for v1, v2 in arr:
        graph[v1].append(v2)

    visited = [-1] * (n + 1)
    que = deque([[x, 0]])

    while que:
        pop, d = que.popleft()
        if visited[pop] == -1 or visited[pop] > d:
            visited[pop] = d

        for next in graph[pop]:
            if visited[next] == -1:
                que.append([next, d + 1])

    return visited


result = find_city(arr, x)
flag = True
for i in range(len(result)):
    if result[i] == k:
        print(i)
        flag = False

if flag:
    print(-1)
"""
4 4 2 1
1 2
1 3
2 3
2 4

4 3 2 1
1 2
1 3
1 4

4 4 1 1
1 2
1 3
2 3
2 4
"""
