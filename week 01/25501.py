n, k = map(int, input().split())
arr = list(map(int, input().split()))

anw = [0]
def merge_sort(arr, k):
    global anw
    
    if len(arr) < 2:
        return arr

    mid = (len(arr) + 1)// 2
    low_arr = merge_sort(arr[:mid], k)
    high_arr = merge_sort(arr[mid:], k)

    merged_arr = []
    l = h = 0
    while l < len(low_arr) and h < len(high_arr):
        if low_arr[l] < high_arr[h]:
            merged_arr.append(low_arr[l])
            anw[0] += 1
            if anw[0] == k:
                anw.append(low_arr[l])
            l += 1
        else:
            merged_arr.append(high_arr[h])
            anw[0] += 1
            if anw[0] == k:
                anw.append(high_arr[h])
            h += 1

    while l < len(low_arr):
        merged_arr.append(low_arr[l])
        anw[0] += 1
        if anw[0] == k:
            anw.append(low_arr[l])
        l += 1

    while h < len(high_arr):
        merged_arr.append(high_arr[h])
        anw[0] += 1
        if anw[0] == k:
            anw.append(high_arr[h])
        h += 1

    return merged_arr

merge_sort(arr, k)

if anw[0] < k:
    print(-1)
else:
    print(anw[1])
