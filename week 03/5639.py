import sys

sys.setrecursionlimit(10**8)
input = sys.stdin.readline

arr = []
while True:
    try:
        arr.append(int(input()))
    except:
        break


def post_order(root, end):
    if root > end:
        return

    # 루트 노드의 오른쪽 트리 시작점 탐색
    right = end + 1
    for node in range(root + 1, end + 1):
        if arr[root] < arr[node]:
            right = node
            break

    # postorder
    post_order(root + 1, right - 1)
    post_order(right, end)
    print(arr[root])


post_order(0, len(arr) - 1)
