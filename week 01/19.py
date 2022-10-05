def reverse_c(a, b):
    reverse_a = int(a[::-1])
    reverse_b = int(b[::-1])

    if reverse_a > reverse_b:
        return reverse_a
    else:
        return reverse_b

a, b = input().split()
print(reverse_c(a, b))