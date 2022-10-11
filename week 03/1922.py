import sys
from heapq import *

input = sys.stdin.readline

n = int(input())
m = int(input())
arr = [list(map(int, input().split())) for x in range(m)]


def kruskalMST(arr):
    parent = [x for x in range(n + 1)]

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

    arr.sort(key=lambda x: x[2])
    result = 0

    for v1, v2, cost in arr:
        if find(v1) != find(v2):
            union(v1, v2)
            result += cost

    return result


print(kruskalMST(arr))
