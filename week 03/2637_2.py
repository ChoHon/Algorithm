import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
m = int(input())
arr = [list(map(int, input().split())) for x in range(m)]


def assemble_toy(arr):
    graph = [[] for x in range(n + 1)]
    in_degree = [0 for x in range(n + 1)]
    for end, start, cnt in arr:
        graph[start].append([end, cnt])
        in_degree[end] += 1

    board = [[0] * (n + 1) for x in range(n + 1)]
    # 기본 부품
    basic = []
    que = deque([])
    for i in range(1, n + 1):
        if in_degree[i] == 0:
            que.append(i)
            basic.append(i)

    while que:
        pop = que.popleft()

        for end, cnt in graph[pop]:
            # pop이 기본 부품이면 표에서 end행의 필요개수를 더함
            if pop in basic:
                board[end][pop] += cnt

            # pop이 중간 부품이면 표에서 pop행의 값 * 필요개수를 end행에 더함
            else:
                for i in range(1, n + 1):
                    board[end][i] += board[pop][i] * cnt

            in_degree[end] -= 1
            if in_degree[end] == 0:
                que.append(end)

    return [x for x in enumerate(board[n]) if x[0] in basic]


for comp, cnt in assemble_toy(arr):
    print(comp, cnt)
