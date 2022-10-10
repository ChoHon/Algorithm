import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
m = int(input())
arr = [list(map(int, input().split())) for x in range(m)]
start, finish = map(int, input().split())


def critical_path(arr):
    graph = [[] for x in range(n + 1)]
    in_degree = [0 for x in range(n + 1)]
    for v1, v2, cost in arr:
        graph[v1].append([v2, cost])
        in_degree[v2] += 1

    cost = [0 for x in range(n + 1)]
    route = [[] for x in range(n + 1)]
    que = deque([start])

    while que:
        cur_city = que.popleft()

        for next_city, next_cost in graph[cur_city]:
            in_degree[next_city] -= 1

            if cost[next_city] < cost[cur_city] + next_cost:
                cost[next_city] = cost[cur_city] + next_cost
                route[next_city] = [cur_city]
            elif cost[next_city] == cost[cur_city] + next_cost:
                route[next_city].append(cur_city)

            if in_degree[next_city] == 0:
                que.append(next_city)

    que = deque([finish])
    result = set()

    while que:
        cur_city = que.popleft()

        for prev_city in route[cur_city]:
            if (prev_city, cur_city) not in result:
                result.add((prev_city, cur_city))
                que.append(prev_city)

    return cost[finish], len(result)


for i in critical_path(arr):
    print(i)

"""
7
9
1 2 4
1 3 2
1 4 3
2 6 3
2 7 5
3 5 1
4 6 4
5 6 2
6 7 5
1 7
"""
