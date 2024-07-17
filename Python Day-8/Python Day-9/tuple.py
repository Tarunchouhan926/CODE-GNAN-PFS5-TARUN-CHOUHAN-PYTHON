#creating a tuple
'''
x=(1,2,3)
print(type(x))

x=()
print(type(x))

#how to create a single element in tuple

x=(1,)
print(x)
print(type(x))

#how to take input from user from tuple

x=tuple(map(int,input().split()))
print(x)

#how to delete input from user from tuple

x=(1,2,3,4,5,6)
del(x)
print(x)

#how to find index and count of tuple

x=(1,2,3,4,5,2,2,3,4)
print(x.count(2))
print(x.index(4))

#tuple built in functions
x=(1,2,2,34,5,66,7,8)
print(sum(x))
print(all(x))
print(any(x))
print(min(x))
print(max(x))
print(sorted(x))
print(len(x))
'''
