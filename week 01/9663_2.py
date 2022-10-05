# 느림
# 퀸을 둘 수 있는지 Check하는 is_promising이 O(n)이라서?

n = int(input())
anw = 0
row = [0] * n

def is_promising(x):
    for i in range(x):
        if row[x] == row[i] or abs(row[x] - row[i]) == abs(x - i):
            return False

    return True

def n_queens(x):
    global anw
 
    if x == n:
        anw += 1
        return

    else:
        for i in range(n):
            row[x] = i

            if is_promising(x):
                n_queens(x+1)

n_queens(0)
print(anw)