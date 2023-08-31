from itertools import combinations

lst = ['0001', '0011', '0101', '1011', '1101', '1111']
new_lst = [int(i, 2) for i in lst]

a = []
for r in range(1,len(new_lst)):
    for c in combinations(new_lst,r):
        a.append(c)

diff = []
for items in a:
    res = [i for i in new_lst if i not in items]
    c = abs(sum(res)-sum(items))
    diff.append(c)
    if c==0:
        break

print(f"The least difference is: {sorted(diff)[0]}")