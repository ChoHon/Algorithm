import sys
from collections import deque

input = sys.stdin.readline

n, k = map(int, input().split())
coin = set([int(input()) for x in range(n)])


def cnt_coin(coin, k):
    # 이미 최소 동전 수로 계산을 했던 금액 중복 계산 방지
    visited = set([])
    que = deque([])
    que.append([k, 0])

    while que:
        k, cnt = que.popleft()

        if k == 0:
            return cnt

        for c in coin:
            # 남은 금액이 동전 가치보다 크거나
            # (남은 금액 - 동전 가치)가 계산된적 없는 금액이면 진행
            if k >= c and (k - c) not in visited:
                visited.add(k - c)
                que.append([k - c, cnt + 1])

    return -1


print(cnt_coin(coin, k))

"""
3 15
1
5
12

37 5613
87790
43967
559
72151
67275
38910
84025
67209
32377
21308
9286
3383
87781
88748
97756
51628
2340
60417
8975
23368
79102
93121
36903
82895
66167
32839
55158
14845
11282
12749
98911
49607
65978
80144
8161
12970
25526

"""
