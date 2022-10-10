import sys

input = sys.stdin.readline

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for x in range(m)]


def bead(n, arr):
    over_half = n // 2 + 1

    graph = {x: [set(), set()] for x in range(1, n + 1)}
    for v1, v2 in arr:
        if v1 != v2:
            graph[v1][1].add(v2)
            graph[v2][0].add(v1)

    def dfs(start, k):
        cnt = 0
        que = list(graph[start][k])

        while que:
            pop = que.pop()
            cnt += 1

            if cnt == over_half:
                return True

            for v in graph[pop][k]:
                que.append(v)

        return False

    result = 0
    for i in range(1, n + 1):
        if dfs(i, 0):
            result += 1
            continue

        elif dfs(i, 1):
            result += 1

    return result


print(bead(n, arr))

"""
5 4
2 1
4 3
5 1
4 2

5 4
2 1
2 1
2 1
2 1
"""
