import sys

input = sys.stdin.readline
INF = 1e7

n = int(input())
arr = [list(map(int, input().split())) for x in range(n)]

# 모든 경로에 대한 최소비용 리스트
dist_arr = [[0] * (1 << n) for x in range(n)]


def traveling_salesman(start, route):
    # 최소비용 리스트에 값이 있으면 그냥 가져옴(DP)
    if dist_arr[start][route]:
        return dist_arr[start][route]

    # route의 모든 비트가 1 = 모든 곳을 방문
    # 다시 시작점으로 복귀
    if route == (1 << n) - 1:
        return arr[start][0] if arr[start][0] > 0 else INF

    cost = INF
    # 다시 시작점으로 돌아오기 때문에 한점에서 출발하는 경우만 계산해도 됨
    for i in range(1, n):
        # i번째 도시 방문 여부 체크 and 길이 연결되어 있는지 체크
        if not route & (1 << i) and arr[start][i]:
            # i와 i번째 도시를 방문으로 갱신한 route로 재귀
            value = traveling_salesman(i, route | (1 << i))
            cost = min(cost, value + arr[start][i])

    dist_arr[start][route] = cost
    return dist_arr[start][route]


print(traveling_salesman(0, 1))
