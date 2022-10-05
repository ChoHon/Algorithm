def is_prime_n(n):
    if n == 1:
        return False
    for i in range(2, n):
        if (n % i) == 0:
            return False
    return True

def gold(n):
    half_n = n // 2

    while half_n > 1:
        if is_prime_n(half_n):
            if is_prime_n(n - half_n):
                return half_n
        
        half_n -= 1

t = int(input())
for i in range(t):
    ipt = int(input())
    anw = gold(ipt)
    print(anw, ipt - anw)

