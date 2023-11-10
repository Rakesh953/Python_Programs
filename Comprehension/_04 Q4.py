# L=[2,3,5,1,4,7]
# Target=6
# newL=[L[ind1],L[ind2] for ind in range(ind1-10),for ind2 in range(ind+1) L[ind1]l[indd2]]
# print(newL)

L = [2, 3, 5, 1, 4, 7]
Target = 6
newL = [(L[ind1], L[ind2]) for ind1 in range(len(L)) for ind2 in range(ind1 + 1) if L[ind1] + L[ind2] == Target]
print(newL)
