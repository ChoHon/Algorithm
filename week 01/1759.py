from itertools import combinations
import sys
input = sys.stdin.readline

# l, c = map(int, input().split())
# char_arr = input().split()

l, c = 4, 6
char_arr = ['a', 't', 'c', 'i', 's', 'w']

vowel = ['a', 'e', 'i', 'o', 'u']

com_arr = list(combinations(char_arr, l))
for i in com_arr:
    sentence = ''
    con, vow = 0, 0
    for j in i:
        if j in vowel:
            vow += 1
        else:
            con += 1
        sentence += j
    if (con > 1 and vow > 0): print(sentence)