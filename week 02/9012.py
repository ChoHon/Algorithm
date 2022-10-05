n = int(input())
arr = [input() for x in range(n)]


def parenth(vps):
    stack = []
    for char in vps:

        if char == "(":
            stack.append("(")

        elif char == ")":
            if not stack:
                print("NO")
                return

            stack.pop()

    if not stack:
        print("YES")
    else:
        print("NO")

    return


for i in arr:
    parenth(i)
