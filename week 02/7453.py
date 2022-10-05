import sys

input = sys.stdin.readline

n = int(input())
A, B, C, D = [], [], [], []
for _ in range(n):
    a, b, c, d = map(int, input().split())
    A.append(a)
    B.append(b)
    C.append(c)
    D.append(d)


def abcd():
    temp_dict = dict()
    cnt = 0

    for a in A:
        for b in B:
            temp_dict[a + b] = temp_dict.get(a + b, 0) + 1

    for c in C:
        for d in D:
            cnt += temp_dict.get(-(c + d), 0)

    return cnt


print(abcd())
