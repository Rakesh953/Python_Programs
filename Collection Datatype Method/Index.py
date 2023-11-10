###  Index in Tuple  ###
T=([11,12,15,[18,19,[23,14,15],16,110],15],(25,'PYTHON'))
print(T[0][0])
print(T[0][1])
print(T[0][2])
print(T[0][3][0])

### Index in Dictonary ###
N = [{'a':[10,20,{11:20,13:45}]},('PYTHON',{1:'ABCD',2:'MNOP'})]
#print(N[0])
#print(N[0]['a'])
print(N[0]['a'][0])
print(N[0]['a'][1])
#print(N[0]['a'][2])
print(N[0]['a'][2][11])
print(N[0]['a'][2][13])
print(N[1][0][0])
print(N[1][0][1])
print(N[1][0][2])
print(N[1][0][3])
print(N[1][0][4])
print(N[1][0][5])
print(N[1][1][1][0])
print(N[1][1][1][1])
print(N[1][1][1][2])
print(N[1][1][1][3])
print(N[1][1][2][0])
print(N[1][1][2][1])
print(N[1][1][2][2])
print(N[1][1][2][3])

N1 = [{'a':[10,20,{11:20,13:45}]},('PYTHON',{1:'ABCD',2:'MNOP'})]
print(N1[-1][-1][2][-1])