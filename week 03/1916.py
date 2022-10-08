import sys
from heapq import *

input = sys.stdin.readline
INF = sys.maxsize

n = int(input())
m = int(input())
# 그래프를 dictionary로 구성하면 v1 -> v2로 가는 길이 여러개일 경우 중복처리가 힘듬
arr = [[] for _ in range(n + 1)]
for _ in range(m):
    v1, v2, w = map(int, input().split())
    arr[v1].append([v2, w])
start, finish = map(int, input().split())


def dijkstra(arr, start):
    # 출발지에서 다른 도시로 가는 최소비용표
    # 초기에는 INF로 초기화
    dist = [INF] * (n + 1)
    dist[start] = 0
    que = [[dist[start], start]]

    while que:
        cur_dist, cur_city = heappop(que)

        # 계산할 필요 없는 케이스 스킵
        if cur_dist > dist[cur_city]:
            continue

        else:
            for next_city, next_dist in arr[cur_city]:
                # 현재위치까지 거쳐온 비용 + 현재위치에서 다음 위치로 가는 비용
                d = next_dist + cur_dist

                if dist[next_city] > d:
                    dist[next_city] = d
                    heappush(que, [d, next_city])

    return dist


print(dijkstra(arr, start)[finish])


"""
5
8
1 2 2
1 3 3
1 4 1
1 5 10
2 4 2
3 4 1
3 5 1
4 5 3
1 5

5
9
1 2 2
1 2 1
1 3 3
1 4 1
1 5 10
2 4 2
3 4 1
3 5 1
4 5 3
1 5
"""
