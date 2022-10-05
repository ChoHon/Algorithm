import sys

input = sys.stdin.readline

n, k = map(int, input().split())
number = input().strip()


def make_bigger(number, k):
    n_arr = list(map(int, list(number)))
    stack = []

    for i in n_arr:
        while stack and k > 0 and stack[-1] < i:
            stack.pop()
            k -= 1

        stack.append(i)

    while k > 0:
        stack.pop()
        k -= 1

    return "".join(map(str, stack))


print(make_bigger(number, k))
