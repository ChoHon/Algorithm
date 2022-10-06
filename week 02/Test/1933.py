from heapq import *
import sys

input = sys.stdin.readline

n = int(input())
b_arr = [list(map(int, input().split())) for x in range(n)]


def skyline(b_arr):
    arr, heap, result = [], [], []

    # 건물 시작점(True), 끝점(False)을 구분해서 리스트 생성
    # idx는 b_arr 인덱싱을 통해 건물 높이와 끝점 찾기 위함
    for idx, b in enumerate(b_arr):
        arr.append([b[0], True, idx])
        arr.append([b[2], False, idx])

    # 정렬
    # 우선순위 1 : x좌표. 오름차순 -> Sweeping
    # 우선순위 2 : 시작점, 끝점. 시작점 먼저 -> 끝점과 시작점이 겹치는 경우 시작점 우선
    # 우선순위 3 : 건물의 높이. 내림차순 -> 시작점이 겹치는 경우 건물 높이 큰 것 우선
    arr.sort(key=lambda x: (x[0], -x[1], -b_arr[x[2]][1]))

    for x in arr:
        height = b_arr[x[2]][1]
        end = b_arr[x[2]][2]

        # 시작점일 때
        if x[1]:
            # 건물이 하나도 없거나 시작하는 건물의 높이가 현재 최대 높이보다 높을 때
            # Log 작성
            if not heap or height > -heap[0][0]:
                result.append([x[0], height])

            heappush(heap, [-height, end])

        # 끝점일 때
        else:
            # 끝나는 건물의 높이가 현재 최대 높이 때
            if heap and -heap[0][0] == height:
                heappop(heap)

                # 이미 끝난 높이들 끝점 위치를 통해 heap에서 삭제
                while heap and heap[0][1] <= end:
                    pop = heappop(heap)

                if heap:
                    # 높이가 같은 두 건물의 시작점과 끝점이 겹칠 때
                    # Log 출력 없이 이어지게 하기 위해서
                    if -heap[0][0] != height:
                        result.append([x[0], -heap[0][0]])
                else:
                    result.append([x[0], 0])

    return result


for i, j in skyline(b_arr):
    print(i, j, end=" ")

"""
3
1 5 5
3 4 6
4 3 7

8
1 11 5
2 6 7
3 13 9
12 7 16
14 3 25
19 18 22
23 13 29
24 4 28

2
1 1 2
1 2 2

4
0 5 5
1 2 7
2 3 5
3 4 5

2
1 1 2
2 1 3
"""
