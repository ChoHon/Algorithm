from copy import deepcopy

l = ['1', '2', '12', '1']

result = []
def permu(k, l, per):
    if k == 0:
        result.append(per)

    else:
        for i in l:
            temp_l = deepcopy(l)
            temp_l.remove(i)
                
            permu(k-1, temp_l, per + [i])

permu(2, l, [])
print(result)