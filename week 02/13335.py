from collections import deque
import sys

input = sys.stdin.readline

n, w, l = map(int, input().split())
arr = list(map(int, input().split()))


def truck(bridge_length, weight, truck_weights):
    fin = []
    ing = deque([truck_weights[0]])
    ing_time = deque([bridge_length + 1])
    wait = deque(truck_weights[1:])
    time = 1

    while True:
        if len(fin) == n:
            return time

        time += 1

        if ing_time[0] <= time:
            fin.append(ing.popleft())
            ing_time.popleft()

        if wait:
            if sum(ing) + wait[0] <= weight:
                ing.append(wait.popleft())
                ing_time.append(time + bridge_length)


print(truck(w, l, arr))
