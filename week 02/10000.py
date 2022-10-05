import sys

input = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().split())) for x in range(n)]


def circle(arr):
    INIT = 0
    OSC = 1
    NOT_OSC = 2

    # 원의 왼쪽(True) 끝 x 좌표
    event_arr = list(map(lambda x: [True, x[0] - x[1]], arr))
    # 원의 오른쪽(False) 끝 x 좌표
    event_arr += list(map(lambda x: [False, x[0] + x[1]], arr))
    # x 좌표 오름차순, 같으면 우 -> 좌 순으로
    event_arr.sort(key=lambda x: (x[1], x[0]))
    stack = []
    sol = 0

    for i, event in enumerate(event_arr):
        if stack:
            # 새로운 원이 추가되었을 때 or 직전 원까지 접한 것이 이어지고 있을 때
            # 지금 원이 직전 원과 접하는지 판단
            if stack[-1] == INIT or stack[-1] == OSC:
                stack[-1] = OSC if event[1] == event_arr[i - 1][1] else NOT_OSC

        # 왼쪽 끝 x 좌표 = 새로운 원 추가(push)
        if event[0]:
            stack.append(0)
        # 오른쪽 끝 x 좌표 = 원 닫기(pop)
        # 닫을 때 접한 원들로 위아래가 갈렸다면 추가치(sol) 증가
        else:
            sol += 1 if stack[-1] == OSC else 0
            stack.pop()

    return sol + n + 1


print(circle(arr))
