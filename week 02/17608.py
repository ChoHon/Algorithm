import sys

input = sys.stdin.readline

n = int(input())


def stick():
    stack = []

    for i in range(n):
        s = int(input())

        while stack and stack[-1] <= s:
            stack.pop()

        stack.append(s)

    return len(stack)


print(stick())
