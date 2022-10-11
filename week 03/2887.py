import sys
from heapq import *

input = sys.stdin.readline

n = int(input())
arr = []
for i in range(n):
    x, y, z = map(int, input().split())
    arr.append([i, x, y, z])


def tunnel(arr):
    parent = [x for x in range(n)]

    def find(v):
        if parent[v] != v:
            parent[v] = find(parent[v])
        return parent[v]

    def union(v1, v2):
        v1 = find(v1)
        v2 = find(v2)

        if v1 > v2:
            parent[v1] = v2
        else:
            parent[v2] = v1

    edge_arr = []
    for i in range(1, 4):
        arr = sorted(arr, key=lambda x: x[i])
        edge_arr += [
            (abs(v1[i] - v2[i]), v1[0], v2[0]) for v1, v2 in zip(arr[:-1], arr[1:])
        ]

    result = 0
    edge_arr.sort()
    for cost, v1, v2 in edge_arr:
        if find(v1) != find(v2):
            union(v1, v2)
            result += cost

    return result


print(tunnel(arr))

"""
5
11 -15 -15
14 -5 -15
-1 -1 -5
10 -4 -1
19 -4 19

3
1 1 1
2 3 9
-1 9 5
"""
