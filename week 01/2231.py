n = int(input())
def divide_sum(n):
    for i in range(n):
        sum = i
        origin_i = i
        while i > 0:
            sum += i % 10
            i //= 10
        
        if sum == n:
            return origin_i

    return 0

print(divide_sum(n))