L1 = [1,3,6,78,35,55]
L2 = [12,24,35,24,88,120,155]
lst = []

for i in range(len(L1)):
    if L1[i] in L2:
        lst.append(L1[i])

print(lst)