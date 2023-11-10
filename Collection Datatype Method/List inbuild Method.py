## List Inbuild method ##

#Index

#Count

#Join
L4=['we','are','groot']
print('-'.join(L4))
print('@'.join(L4))
print('#'.join(L4))
print(''.join(L4))

# Reverse
R=[1,2,3,4,5,6]
R.reverse()
print(R)

## Add Value to the list ##
#Append
L = [12,10,11]
L.append(22)
L.append(15)
L.append(13)
print(L)

l = [11,12]
l.append('mno')
l.append([10,120])
l.append([11,12])
print(l)

#insert
I = [11,12,13]
I.insert(1,15)
I.insert(4,16)
I.insert(-3,18)
print(I)

#Extend
E = [10,True]
E.extend('ABCD')
print(E)

E2=[10,20,True]
E2.extend('ABCD')
E2.append(False)
E2.insert(-4,'python')
E2.append('ABCD')
E2.insert(4,'easy')
print(E2)

G=['we are groot']
#G.extend(G[-2].split())  list index out of range
#G.extend(G[1].split())  list index out of range
G.extend(G[0].split())
print(G)



## Remove value From List ##
# remove
L=[11,12,11,13,15]
L.remove(11)
print(L)

#pop
L1=[11,12,11,13,15]
L1.pop() #If no argument pass then last value it will remove from the list
L1.pop(-2) 
print(L1)

L=['we are groot',12,1,0,2,-1,-2]
L[L.pop()]=L[L.pop(3)].split()
print(L)

E=['ENGINEERING',11,12,13,0,1,2]
E.extend(E.pop(0).split('I'))
print(E)


## Arrange Value in List ##

#Ascending Order
    # sort
L=['A','B','S','L','O']
L.sort()
print(L)

L1=['Prasanta','Nikhil','Rakesh','Oldmonk','Priti']
L1.sort()
print(L1)

L3=[['prasanta','Nikhil'],['Teacher,swayam'],['Rakesh','priti'],'engineering'.split('i')]
L3.sort()
print(L3)

#Decending Order
L=[12,11,14,16]
L.sort(reverse=True)
print(L)