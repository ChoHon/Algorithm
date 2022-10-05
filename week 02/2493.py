import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

def tower(arr):
    stack = []
    arr = list(enumerate(arr))

    for i in range(n):
        while True:
            if not stack:
                stack.append(arr[i])
                print(0)
                break

            elif stack[-1][1] > arr[i][1]:
                print(stack[-1][0] + 1)
                stack.append(arr[i])
                break

            else:
                stack.pop()

    return

tower(arr)
