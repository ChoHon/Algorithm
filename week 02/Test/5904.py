# 테스트 케이스 통과
# 시간 초과

import sys
from collections import deque

input = sys.stdin.readline

n = int(input())


def len_of_moo(k):
    if k == 0:
        return 3

    return (len_of_moo(k - 1) * 2) + k + 3


def test(k):
    if k == 0:
        return [3]

    return test(k - 1) + [k + 3] + test(k - 1)


def make_moo(k):
    if k == 0:
        return "moo"

    return make_moo(k - 1) + "m" + ("o" * (k + 2)) + make_moo(k - 1)


def moo(n):
    temp = 0
    sum_ = 0
    while sum_ < n:
        sum_ += len_of_moo(temp)
        temp += 1

    idx = n - len_of_moo(temp - 1)

    t = deque(test(temp))
    while idx >= t[0]:
        idx = idx - t.popleft()

    if idx == 0:
        return "m"
    else:
        return "o"


print(moo(n))
