import sys

input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))


def right_big_number(arr):
    stack = []
    result = []

    for i, num in enumerate(arr):
        while stack and stack[-1][1] < num:
            temp = stack.pop()
            temp[1] = num
            result.append(temp)

        stack.append([i, num])

    for i in stack:
        i[1] = -1
        result.append(i)

    result.sort()
    return result


for i in right_big_number(arr):
    print(i[1], end=" ")
