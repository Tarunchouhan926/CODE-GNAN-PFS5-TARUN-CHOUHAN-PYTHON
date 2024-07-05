#for loop
'''
for i in range(5):
    print(i)
for i in range(1,10,2):
    print(i)

for i in range(-1,-9,-1):
   print(i)

a =[1,2,3,4,5,5,66,7,87]
for i in a:
    print(i)


#while loop
a=5
while a<10:
    print("hi")
    a+=1

#nested for loop
for i in range(0,3):
    for j in range(0,3):
        print(i+j)
'''
#triangular validator -A triangle validator is a function or tool that checks if three given side lengths can form a valid triangle according to the triangle inequality theorem.

a,b,c=map(int,input().split())

if a+b>c and a+c>b and b+c>a:
    print("yes")

else:
     print("no")
