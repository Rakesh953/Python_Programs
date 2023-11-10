L=[12,14,13,10,8,9]
n=len(L)
LI=-1
for FI in range(n//2):
    L[FI],L[LI]=L[LI],L[FI]
    LI-=1
print(L)        # Values are replace in existing memory location
