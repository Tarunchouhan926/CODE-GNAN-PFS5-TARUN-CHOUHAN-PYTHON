#Reverse of a given number

n=int(input("enter the number:"))#135
rev=0

while(n>0):
   a=n%10
   rev=rev*10+a
   n=n//10
print(rev)


#swapping of 2 numbers

n1=20
n2=30

n1,n2=n2,n1
print(n1)
print(n2)


#second largest number

a,b,c=map(int,input("enter the number:").split())

if (a>b and a>c):
    print("a is first largest number")
    secondlargest=max(b,c)
    print(f"second lagest number:{secondlargest}")
elif b>a and b>c:
    print("b is largest")
    secondlargest=max(c,a)
    print(f"second lagest number:{secondlargest}")
else:
    print("c is largest")
    secondlargest=max(a,b)
    print(f"second lagest number:{secondlargest}")
    
#add num at front and end
num=input("enter the number")
frontnum=input("enter the front number")
endnum=input("enter the end number")

value=frontnum+num+endnum
print(value)

#movie

x=int(input())
y=int(input())

speed=y/2
total=x-speed
print("the total watch time for the movie is:",total)
