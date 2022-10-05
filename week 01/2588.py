a, b = [int(input()) for x in range(2)]

def multiple(a, b):
    origin_b = b

    while b > 0:
        print(a * (b % 10))
        b = b // 10
        
    print(a * origin_b)

    return

multiple(a, b)