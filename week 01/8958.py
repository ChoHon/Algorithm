n = int(input())

def ox_score(ipt):
    sum_score = 0
    next_score = 1

    for i in ipt:
        if i == 'O':
            sum_score += next_score
            next_score += 1
        else:
            next_score = 1

    return sum_score

for i in range(n):
    print(ox_score(input()))