import sys
from heapq import *

input = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().split()))[:-1] for x in range(n)]


def game(arr):
    time = [0] * (n + 1)
    arr = [[x[0], x[1:]] for x in arr]
    in_degree = [0 for x in range(n + 1)]
    graph = [[] for x in range(n + 1)]
    for i in range(1, n + 1):
        for j in arr[i - 1][1]:
            graph[j].append(i)
            in_degree[i] += 1

    heap = []
    result = []

    for i in range(1, n + 1):
        if in_degree[i] == 0:
            heappush(heap, i)

    while heap:
        pop = heappop(heap)

        max_time = 0
        for v in arr[pop - 1][1]:
            max_time = max(max_time, time[v])
        time[pop] = max_time + arr[pop - 1][0]

        for end in graph[pop]:
            in_degree[end] -= 1
            if in_degree[end] == 0:
                heappush(heap, end)

    return time


for temp in game(arr)[1:]:
    print(temp)

"""
5
10 -1
10 1 -1
4 1 -1
4 3 1 -1
3 3 -1

5
10 -1
20 1 -1
30 2 -1
40 3 5 -1
100 -1

10
30
60
140
100

5
10 -1
10 1 -1
4 1 -1
4 3 1 -1
3 3 2 -1
"""
