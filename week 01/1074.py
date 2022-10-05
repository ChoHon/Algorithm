def move_z(n, r, c):
    anw = 0
    half = 2 ** (n-1)

    if n == 0:
        return 0

    if half > r:
        if half > c:
            anw += move_z(n-1, r, c)
        else:
            anw += half ** 2 + move_z(n-1, r, c - half)
    else:
        if half > c:
            anw += (half ** 2) * 2 + move_z(n-1, r - half, c)
        else:
            anw += (half ** 2) * 3 + move_z(n-1, r - half, c - half)

    return anw

n, r, c = map(int, input().split())
print(move_z(n, r, c))


