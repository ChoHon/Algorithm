x, y, w, h = map(int, input().split())

def escape(x, y, w, h):
    d = [x, y]
    d.append(w - x)
    d.append(h - y)

    return min(d)  

print(escape(x, y, w, h))