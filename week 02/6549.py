import sys

input = sys.stdin.readline


def histogram():
    while True:
        n, *arr = list(map(int, input().split()))
        # 마지막에 일괄처리하기 위해 append
        arr.append(0)

        if n == 0:
            return

        stack = []
        max_sq = 0

        for i, sq in enumerate(arr):
            # 새로 추가된 사각형이 직전 사각형보다 높이가 낮을 때
            while stack and arr[stack[-1]] > sq:
                h = arr[stack.pop()]

                # 가로 길이는 처음 등장한 index에서 지금 index 바로 전까지
                if stack:
                    w = i - stack[-1] - 1
                else:
                    w = i

                max_sq = max(max_sq, h * w)

            # 스택에 index를 저장
            stack.append(i)

        print(max_sq)


histogram()
