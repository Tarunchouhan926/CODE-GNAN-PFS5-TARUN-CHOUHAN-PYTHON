'''#list methods
x=[1,2,2,"a"]
#append()
x.append("b")
print(x)
x.append([1,2,3,4,5,6])
print(x)
#extend()
x=[1,2,3,4]
x.extend([5,6,7])
print(x)
#insert()
x=[1,2,3,5,6]
x.insert(1,8)
print(x)
#remove()
x=[1,2,3,4,6]
x.remove(6)
print(x)
#pop()
x=[1,2,3,4]
x.pop(3)
print(x)
#index()
x=[1,2,3,5]
print(x.index(5))
#clear()
x=[1,2,3,4,6]
x.clear()
print(x)
#copy
a=[1,2,3,5]
b=a.copy()
print(b)
#sort
a=[1,21,99,24]
a.sort()
print(a)
#reverse
a=[1,2,3,4]
a.reverse()
print(a)
#count
a=[1,1,1,2]
b=a.count(1)
print(b)

#list built in functions
#sum
a=[1,2,3,4]
print(sum(a))

#max
a=[1,2,3,4]
print(max(a))

#min
b=[1,2,3,5]
print(min(b))

#all
a=[1,2,3,4]
print(all(a))

a=[1,2,3,0]
print(all(a))

#any
a=[1,2,0,0]
print(any(a))

#len
a=[1,2,3,4,56]
print(len(a))

#sorted
a=[1,23,4,56,2,2,3,5,56,6,7]
print(sorted(a))

#slicing
a=[1,2,3,4,5,67,87,9]
print(a)
print(a[::])
print(a[1::1])
print(a[0:4:1])
print(a[0:4:2])
print(a[::-1])
print(a[-1:-3:-1])
print(a[::3])
print(a[:3])

#sum of positive indexing

x=[4,6,23,90,24,9]
s=0
for i in x[::2]:
    if i%2==0:
        s=s+i
print(s)

#nested list

row=int(input())
col=int(input())
l=[]

for i in range(row):
    x=list(map(int,input().split()))[:col]
    l.append(x)
print(l)
for i in l:
    print(i)
    print(*i,sep=" ")
    
n=int(input())
a=list(map(int,input().split()))[:n]
print(a)
for i in range(n):
 if a[i] in a[i+1:]:
    print(a[i])
       

    

        

