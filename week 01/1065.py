def is_hansu(n):
    str_n = str(n)

    if (int(str_n[1]) - int(str_n[0])) == (int(str_n[2]) - int(str_n[1])):
        return True
    else:
        return False

def cnt_hansu(n):
    cnt = 99
    if n < 100:
        return n
    else:
        for i in range(100, n+1):
            if is_hansu(i):
                cnt += 1
        
        return cnt

ipt = int(input())
print(cnt_hansu(ipt))