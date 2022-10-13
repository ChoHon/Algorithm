import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for x in range(m)]
f1, f2 = map(int, input().split())


def limit_weight(f1, f2):
    graph = [[] for x in range(n + 1)]
    for v1, v2, w in arr:
        graph[v1].append((v2, w))
        graph[v2].append((v1, w))

    def dfs(f1, f2, weight):
        visited = [False] * (n + 1)
        que = deque([f1])

        while que:
            cur_v = que.popleft()

            if cur_v == f2:
                return True

            if visited[cur_v]:
                continue
            visited[cur_v] = True

            for next_v, next_w in graph[cur_v]:
                if not visited[next_v] and next_w >= weight:
                    que.append(next_v)

        return False

    start = 1
    end = 1e9
    result = -1

    while start <= end:
        mid = int((start + end) // 2)

        if dfs(f1, f2, mid):
            start = mid + 1
            result = mid

        else:
            end = mid - 1

    return result


print(limit_weight(f1, f2))
