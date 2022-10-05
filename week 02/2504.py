import sys

input = sys.stdin.readline

vps = input().strip()


def parenth(vps):
    stack = []
    value = 0
    temp = 1

    for i in range(len(vps)):
        char = vps[i]

        if char == "(":
            stack.append("(")
            temp *= 2

        elif char == "[":
            stack.append("[")
            temp *= 3

        elif char == ")":
            if not stack or stack[-1] != "(":
                return 0

            if vps[i - 1] == "(":
                value += temp

            stack.pop()
            temp //= 2

        elif char == "]":
            if not stack or stack[-1] != "[":
                return 0

            if vps[i - 1] == "[":
                value += temp

            stack.pop()
            temp //= 3

    if stack:
        return 0

    return value


print(parenth(vps))
