def word_sort(l):
    if len(l) == 1:
        return l
    
    mid = len(l) // 2

    low_l = word_sort(l[:mid])
    high_l = word_sort(l[mid:])

    merged_l = []
    i = j = 0
    
    while (i < len(low_l)) and (j < len(high_l)):
        
        if len(low_l[i]) > len(high_l[j]):
            merged_l.append(high_l[j])
            j += 1

        elif len(low_l[i]) < len(high_l[j]):
            merged_l.append(low_l[i])
            i += 1

        else:
            if low_l[i] > high_l[j]:
                merged_l.append(high_l[j])
                j += 1

            elif low_l[i] == high_l[j]:
                merged_l.append(low_l[i])
                i += 1
                j += 1

            else:
                merged_l.append(low_l[i])
                i += 1

    merged_l += low_l[i:]
    merged_l += high_l[j:]

    return merged_l

t = int(input())
l = [input() for x in range(t)]

for i in word_sort(l):
    print(i)