import sys
from collections import Counter

input = sys.stdin.readline
sys.setrecursionlimit(10**8)

n = int(input().strip())
a = input().strip()
arr = [sorted(list(map(int, input().split()))) for x in range(n - 1)]
arr.sort()


def dfs(node, tree):
    result = []
    stack = node[0][::-1]

    if stack:
        pop = stack.pop()

        if tree[pop][1] == False:
            result.append(pop)
            stack.extend(tree[pop][0][::-1])

    return result


def count_true(node, tree):
    cnt = 0
    for i in node[0]:
        if tree[i][1] == True:
            cnt += 1

    return cnt


def morning_walk(a, arr):
    anw = 0
    tree = [[[]] for x in range(n + 1)]

    for v1, v2 in arr:
        tree[v1][0].append(v2)
        tree[v2][0].append(v1)

    for i in range(n):
        if a[i] == "1":
            tree[i + 1].append(True)
        else:
            tree[i + 1].append(False)

    for node in tree[1:]:
        stack = node[0]
        num_true = count_true(node, tree)

        if node[1] == False:
            anw += num_true * (num_true - 1)

            other_outside = dfs(node, tree)
            for i in other_outside:
                otherside_true = count_true(tree[i], tree)
                anw += num_true * otherside_true

        else:
            anw += num_true

    return anw


print(morning_walk(a, arr))

"""
5
10111
1 2
2 3
2 4
4 5
"""
