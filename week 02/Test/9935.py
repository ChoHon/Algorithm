import sys

input = sys.stdin.readline

string = input().strip()
bomb = input().strip()


def bomb_string(string, bomb):
    stack = []
    bomb_length = len(bomb)
    last_bomb_char = bomb[-1]

    for char in string:
        stack.append(char)

        if char == last_bomb_char and stack[-bomb_length:] == list(bomb):
            del stack[-bomb_length:]

    if not stack:
        return "FRULA"
    return "".join(stack)


print(bomb_string(string, bomb))

"""
mirkovC4nizCC44
C4

12ab112ab2ab
12ab
"""
