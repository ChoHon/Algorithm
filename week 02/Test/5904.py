import sys
from collections import deque

input = sys.stdin.readline

n = int(input())

# n번째 글자가 있을 수 있는 moo수열 길이와 사이 문자열 계산
now = 3
between = 3
while n > now:
    between += 1
    now = (now * 2) + between


def moo(now, between, n):
    if now == 3:
        return "m" if n == 1 else "o"

    # moo = pre_moo + between + pre_moo
    # 바로 전 moo수열 길이 계산
    pre_moo = (now - between) // 2

    # n이 양쪽 pre_moo 수열 부분에 있을 때 재귀
    if n <= pre_moo:
        return moo(pre_moo, between - 1, n)
    elif n > pre_moo + between:
        return moo(pre_moo, between - 1, n - pre_moo - between)

    # n이 between 부분에 있을 때 반환
    else:
        return "m" if n - pre_moo == 1 else "o"


print(moo(now, between, n))
