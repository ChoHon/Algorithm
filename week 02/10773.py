n = int(input())
arr = [int(input()) for x in range(n)]

def zero(arr):
    stack = []
    for num in arr:
        if num == 0:
            stack.pop()
        else:
            stack.append(num)

    return sum(stack)

print(zero(arr))