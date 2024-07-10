#list
#Declaration
'''
l=[1,2,34,56]
print(l)
l=[1,2,3,'tarun']
print(l)
l=list(map(int,input().split()))
print(l)

#accessing

#positive indexing
x=[1,2,3,4]
print(x[1])
print(x[2])
y=[1,2,3,5]
print(y[-1])
print(y[-2])

#for loop with range

x=[1,2,3,4,5]
for i in range(4):
    print(i,end=" ")

#for loop without range

x=[1,2,3,4,56,7]
for i in x:
    print(i,end=" ")

x=[12,23,4,5,3,55]
print(*x)
print(*x,sep=" ")
print(*x,sep="_")


