import sys
from heapq import *

input = sys.stdin.readline

n = int(input())
arr = [list(input().strip()) for x in range(n)]

reversed_graph = [[] for x in range(n + 1)]
out_degree = [0] * (n + 1)

for i in range(n):
    for j in range(n):
        if arr[i][j] == "1":
            reversed_graph[j + 1].append(i + 1)
            out_degree[i + 1] += 1

# 역방향 graph와 진출차수 리스트
def modify_graph(reversed_graph, out_degree):
    heap = []
    result = []

    for i in range(1, n + 1):
        if not out_degree[i]:
            # 큰 수부터 역으로 순서를 정한다
            heappush(heap, -i)

    while heap:
        pop = -heappop(heap)
        result.append(pop)

        for end in reversed_graph[pop]:
            out_degree[end] -= 1
            if out_degree[end] == 0:
                heappush(heap, -end)

    # 사이클 존재 유무 확인
    for i in out_degree[1:]:
        if i > 0:
            return [-1]

    result.reverse()
    result = sorted(enumerate(result), key=lambda x: x[1])
    return [i + 1 for i, v in result]


for v in modify_graph(reversed_graph, out_degree):
    print(v, end=" ")


"""
5
00001
00010
00000
00001
00100

10
0000001000
1000100010
0000001000
1010000100
0000000101
0101000000
0000000000
0000000000
0000000100
0000001000
4 2 5 3 6 1 8 10 9 7

5
00110
00001
00000
01000
00000
1 3 4 2 5

5
00100
00100
00001
11000
00000
2 3 4 1 5

2
10
01
-1

1
1
-1
"""
