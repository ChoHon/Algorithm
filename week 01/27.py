from itertools import permutations
from copy import deepcopy

# n = int(input())
# r = int(input())
# l = [input() for x in range(n)]

n, r = 4, 2
l = ['1', '2', '12', '1']

def card(n, r, l):
    permu_l = list(permutations(l, r))
    str_permu_l = [[str(x) for x in y] for y in permu_l]
    join_l = [''.join(x) for x in str_permu_l]
    
    return len(set(join_l))

result = set({})
def card2(o, n, r, l, number):
    if o == r:
        result.add(number)
    
    else:
        for i in l:
            temp_l = deepcopy(l)
            temp_l.remove(i)

            card2(o + 1, n, r, temp_l, number + i)

card2(0, n, r, l, '')
print(len(result))
# print(card(n, r, l))
