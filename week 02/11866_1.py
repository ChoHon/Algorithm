import sys

input = sys.stdin.readline

n, k = map(int, input().split())


def josephus(n, k):
    arr = list(range(1, n + 1))
    result = []
    removed_arr = [False] * n
    idx = -1

    while len(result) < n:
        for i in range(k):
            idx += 1
            if idx == n:
                idx = 0
            while removed_arr[idx]:
                idx += 1
                if idx == n:
                    idx = 0

        removed_arr[idx] = True
        result.append(arr[idx])

    return result


string = ""
for i in josephus(n, k):
    string = string + str(i) + ", "
print(f"<{string[:-2]}>")
