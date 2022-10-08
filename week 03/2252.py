import sys
from heapq import *
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())


def lineup():
    graph = [[] for x in range(n + 1)]
    in_degree = [0] * (n + 1)
    for i in range(m):
        start, end = map(int, input().split())
        graph[start].append(end)
        in_degree[end] += 1

    result = []
    heap = []

    for i in range(1, n + 1):
        if in_degree[i] == 0:
            heappush(heap, i)
            result.append(i)

    while heap:
        pop = heappop(heap)

        for end in graph[pop]:
            in_degree[end] -= 1
            if in_degree[end] == 0:
                heappush(heap, end)
                result.append(end)

    return result


for i in lineup():
    print(i, end=" ")

"""
3 2
1 3
2 3

4 2
4 2
3 1

3 3
2 1
3 2
3 1

3 3
1 3
2 3
1 2
"""
