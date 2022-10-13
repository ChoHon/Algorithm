import sys
from heapq import *

input = sys.stdin.readline

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for x in range(m)]
f1, f2 = map(int, input().split())

graph = [[] for x in range(n + 1)]
for v1, v2, w in arr:
    graph[v2].append((v1, w))
    graph[v1].append((v2, w))

for i in range(1, n + 1):
    graph[i].sort(key=lambda x: (x[0], -x[1]))

weight = [0] * (n + 1)


def limit_weight(f1, f2):
    weight[f1] = -2e9
    heap = [[weight[f1], f1]]

    while heap:
        cur_w, cur_v = heappop(heap)
        cur_w = -cur_w

        if cur_v == f2:
            break

        if cur_w < weight[cur_v]:
            continue

        for next_v, next_w in graph[cur_v]:
            temp_w = min(cur_w, next_w)

            if weight[next_v] < temp_w:
                weight[next_v] = temp_w
                heappush(heap, [-temp_w, next_v])


limit_weight(f1, f2)
print(weight[f2])
"""
9 9
1 4 11
1 5 2
4 5 4
4 3 10
4 2 7
5 2 10
5 6 13
3 2 9
2 6 8
1 6
"""
