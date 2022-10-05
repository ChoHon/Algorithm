n = int(input())

def movie_name():
    cnt = 0

    i = 666
    while True:
        if '666' in str(i):
            cnt += 1
            if cnt == n:
                return i
        i += 1

print(movie_name())