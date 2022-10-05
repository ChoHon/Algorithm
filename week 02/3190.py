from collections import deque
import sys

input = sys.stdin.readline

n = int(input())
k = int(input())
apple_arr = [list(map(int, input().split())) for x in range(k)]
l = int(input())
turn_arr = [input().split() for x in range(l)]
turn_arr = deque(turn_arr)


def snake(n, apple_arr, turn_arr):
    head = [1, 1]
    body = deque([])
    next_turn = turn_arr.popleft()
    # 방향 리스트 : 로테이션으로 머리를 돌림
    direc_arr = deque(["R", "D", "L", "U"])
    cnt = 0

    while True:
        cnt += 1
        previous_head_pos = head[:]

        # 머리(head) 이동
        if direc_arr[0] == "R":
            head[1] += 1
        elif direc_arr[0] == "U":
            head[0] -= 1
        elif direc_arr[0] == "L":
            head[1] -= 1
        elif direc_arr[0] == "D":
            head[0] += 1

        # 게임오버
        if head[0] < 1 or head[1] < 1 or head[0] > n or head[1] > n or head in body:
            return cnt

        # 몸(body) 이동
        # 사과 먹으면 사과 삭제
        # 사과 못먹으면 꼬리 삭제
        body.appendleft(previous_head_pos)
        if head not in apple_arr:
            body.pop()
        else:
            apple_arr.remove(head)

        # 머리 방향 돌리기
        if int(next_turn[0]) == cnt:
            if next_turn[1] == "D":
                direc_arr.rotate(-1)
            else:
                direc_arr.rotate(1)

            if len(turn_arr) > 0:
                next_turn = turn_arr.popleft()


print(snake(n, apple_arr, turn_arr))
