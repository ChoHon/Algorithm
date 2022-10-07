import sys
from heapq import *

input = sys.stdin.readline
INF = 1000000

v, e = map(int, input().split())
arr = [list(map(int, input().split())) for x in range(e)]

# 크루스칼
def kruskalMST(arr):
    parent = [x for x in range(v + 1)]

    # 자신이 속한 트리의 root 찾기
    def find(parent, v):
        if parent[v] != v:
            parent[v] = find(parent, parent[v])
        return parent[v]

    # 서로 다른 트리를 합치기
    def union(parent, v1, v2):
        v1 = find(parent, v1)
        v2 = find(parent, v2)
        if v1 < v2:
            parent[v2] = v1
        else:
            parent[v1] = v2

    # 비용 기준으로 정렬
    # 배열 앞에서부터 하나씩 확인 -> 비용이 작은 것부터 찾아감
    arr = [[x[2], x[0], x[1]] for x in arr]
    arr.sort()

    anw = 0
    for i in range(e):
        cost, v1, v2 = arr[i]
        # 선택한 edge의 두 점 검사
        # 두 점이 같은 트리 안에 있으면 사이클 생성되서 트리가 깨짐
        if find(parent, v1) != find(parent, v2):
            union(parent, v1, v2)
            anw += cost

    return anw


# 프림
def primMST(start, arr):
    arr = [[x[2], x[0], x[1]] for x in arr]
    visited = [False] * (v + 1)
    heap = []

    board = [[INF for x in range(v + 1)] for y in range(v + 1)]
    for tmp in arr:
        board[tmp[1]][tmp[2]] = tmp[0]
        board[tmp[2]][tmp[1]] = tmp[0]

    # 모든 노드를 방문했는지 확인
    def check(visited):
        for i in visited[1:]:
            if not i:
                return True

        return False

    anw = 0
    visited[start] = True
    while check(visited):
        dist = board[start]

        # 현재 노드에서 방문하지 않은 다른 노드 검색
        # 발견한 노드를 min heap에 저장
        for i, d in enumerate(dist):
            if d < INF and not visited[i]:
                heappush(heap, [d, i])

        # 방문하지 않은 노드로 가는 edge가 나올 때까지 heap pop
        pop = heappop(heap)
        while visited[pop[1]]:
            pop = heappop(heap)

        anw += pop[0]
        visited[pop[1]] = True

        start = pop[1]

    return anw


print(kruskalMST(arr))
print(primMST(1, arr))

"""
3 3
1 2 1
2 3 2
1 3 3

7 9
1 2 29
1 6 10
2 3 16
2 7 15
3 4 12
4 5 22
4 7 18
5 6 27
5 7 25

6 9
1 2 5
1 3 4
2 3 2
2 4 7
3 4 6
3 5 11
4 5 3
4 6 8
5 6 8
"""
