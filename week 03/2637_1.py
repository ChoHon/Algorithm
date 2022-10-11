import sys
from heapq import *

input = sys.stdin.readline

n = int(input())
m = int(input())


def assemble_toy():
    graph = [[] for x in range(n + 1)]
    in_degree = [0] * (n + 1)
    for i in range(m):
        start, end, cnt = map(int, input().split())
        graph[start].append([end, cnt])
        in_degree[end] += 1

    rank_order = []
    heap = []
    for i in range(1, n + 1):
        if in_degree[i] == 0:
            heappush(heap, i)
            rank_order.append(i)

    while heap:
        pop = heappop(heap)

        for end, cnt in graph[pop]:
            in_degree[end] -= 1
            if in_degree[end] == 0:
                heappush(heap, end)
                rank_order.append(end)

    anw = {x: 0 for x in range(1, n + 1)}
    anw[n] = 1

    basic = []
    for v in rank_order:
        # 진입차수가 0 = 기본 부품
        if not graph[v]:
            basic.append(v)

        # 위상 정렬 역순으로 부품 수 계산
        for comp, cnt in graph[v]:
            anw[comp] += cnt * anw[v]

    return [[x, anw[x]] for x in sorted(basic)]


for i in assemble_toy():
    print(i[0], i[1])

"""
7
8
5 1 2
5 2 2
7 5 2
6 5 2
6 3 3
6 4 4
7 6 3
7 4 5
"""
