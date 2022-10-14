import sys

input = sys.stdin.readline

inp = input().strip()


def plus(string):
    arr = string.split("+")
    for i in range(len(arr)):
        arr[i] = int(arr[i].lstrip("0"))
    return sum(arr)


def missing_parentheses(inp):
    arr = inp.split("-")
    arr = list(map(plus, arr))

    result = arr[0]
    for temp in arr[1:]:
        result -= temp

    return result


print(missing_parentheses(inp))
