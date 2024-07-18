#dictionary
#Creating a dictionary
'''
d={1:10,2:20,3:30}

print(d)

d={}

print(d)

d={}

for i in range (3):
   x,y=map(int,input().split())
   d[x]=y
print(d)

#Accesing of elements
d={1:10,2:20,3:30}
print(d[3])
print(d.get(3))
print(d.get(40))


for i in d:
     print(i,d[i])

#Modifing Dictionary
d={1:10,2:20,3:30}
d[2]=200
print(d)

#insertion into dictionary
d={1:10,2:20,3:30}
d[4]=400
print(d)

#Deletion of dixtionary

d={1:10,2:20,3:30}
del d


#Methods in Dictionary
#get()
d={1:10,2:20,3:30}
print(d.get(2))

#pop
d={1:10,2:20,3:30}
d.pop(3)
print(d)

#popitem
d={1:10,2:20,3:30}
d.popitem()
print()
'''
l="the quick brown for jumps over the lazy dog"
b=len(l)
print(b)

 

