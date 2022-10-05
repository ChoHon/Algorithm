def self_number():
    arr = {x for x in range(1, 10001)}
    
    def d(n):
        sum_ = n
        while n > 0:
            n, d = divmod(n, 10)
            sum_ += d
        
        return sum_

    for i in range(1, 10001):
        arr.discard(d(i))

    return list(arr)

for i in self_number():
    print(i)
