n = int(input())
check_col = [True] * n
check_diag_sum = [True] * (2 * n - 1)
check_diag_diff = [True] * (2 * n - 1)
cnt = 0


def nqueen(o):
    global cnt

    if o == n:
        cnt += 1

    else:
        for i in range(n):
            if check_col[i] and check_diag_sum[o + i] and check_diag_diff[o - i + n - 1]:

                check_col[i] = check_diag_sum[o + i] = check_diag_diff[o - i + n - 1] = False

                nqueen(o + 1)

                check_col[i] = check_diag_sum[o +i] = check_diag_diff[o - i + n - 1] = True


nqueen(0)
print(cnt)
