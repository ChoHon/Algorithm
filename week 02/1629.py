a, b, c = map(int, input().split())


def mul(a, b, c):

    if b == 1:
        return a % c

    mid = b // 2

    temp = mul(a, mid, c)
    remain = (temp**2) % c
    if b % 2 == 1:
        remain = (remain * (a % c)) % c

    return remain


print(mul(a, b, c))
