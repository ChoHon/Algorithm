from itertools import permutations

n, m = map(int, input().split())
l = list(map(int, input().split()))

anw = 0


def blackjack1(n, m, l):
    temp_l = []

    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                if l[i] + l[j] + l[k] <= m:
                    temp_l.append(l[i] + l[j] + l[k])                

    return max(temp_l)

def blackjack2(n, m, l):
    permu = list(permutations(l, 3))
    all_sum = [sum(x) for x in permu if sum(x) <= m]
    
    return max(all_sum)

def blackjack3(o, m, l, sum_):
    global anw

    if o == 3:
        if sum_ <= m:
            anw = max(anw, sum_)
    
    else:
        for i in l:
            temp_l = [x for x in l if x is not i]
            blackjack3(o + 1, m, temp_l, sum_ + i)

    return anw

print(blackjack1(n, m, l))
