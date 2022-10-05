from itertools import permutations

ex_op = ['+', '-', '*', '//']

n = int(input())
l = input().split()
ipt_op = list(map(int, input().split()))

op = []
for i in range(4):
    for j in range(ipt_op[i]):
        op.append(ex_op[i])

combi_op = list(set(permutations(op)))

def culop():
    all_result = []

    for ops in combi_op:
        result = l[0]

        for i in range(n-1):
            if (int(result) < 0) and (ops[i] == '//'):
                result = str(((int(result) * -1) // int(l[i + 1])) * -1)

            else:
                result = str(eval(ops[i].join([result, l[i + 1]])))
                
        all_result.append(int(result))

    return max(all_result), min(all_result)

max_result, min_result = culop()
print(max_result, min_result)