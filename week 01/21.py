def is_prime_n(n):
    if n == 1:
        return False
    for i in range(2, n):
        if (n % i) == 0:
            return False
    return True

def count_prime_n(l):
    cnt = 0
    for n in l:
        if is_prime_n(n):
            cnt += 1
        
    return cnt

t = int(input())
l = list(map(int, input().split()))
print(count_prime_n(l))