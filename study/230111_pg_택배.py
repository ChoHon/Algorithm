# https://school.programmers.co.kr/learn/courses/30/lessons/150369

def solution_origin(cap, n, deliveries, pickups):
    answer = 0

    pi, di = n, n

    while not (pi == 0 and di == 0):
        while pi >= 1 and pickups[pi - 1] == 0:
            pi -= 1
        while di >= 1 and deliveries[di - 1] == 0:
            di -= 1

        answer += (max(pi, di)) * 2

        c = cap
        while c > 0 and pi >= 1:
            d = min(c, pickups[pi - 1])
            pickups[pi - 1] -= d
            c -= d
            if pickups[pi - 1] == 0:
                pi -= 1

        c = cap
        while c > 0 and di >= 1:
            d = min(c, deliveries[di - 1])
            deliveries[di - 1] -= d
            c -= d
            if deliveries[di - 1] == 0:
                di -= 1

    return answer

def solution_new(cap, n, deliveries, pickups):
    answer = 0
    d = 0
    p = 0
    pos = n - 1

    for i in range(n - 1, -1, -1):
        d += deliveries[i]
        p += pickups[i]

        while d > cap or p > cap:
            d -= cap
            p -= cap
            answer += 2 * (pos + 1)
            pos = i

    if d > 0 or p > 0:
        answer += 2 * (pos + 1)

    return answer