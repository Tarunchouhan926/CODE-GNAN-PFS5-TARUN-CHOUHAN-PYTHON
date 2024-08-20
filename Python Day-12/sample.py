#Compress the string
'''
s = input()
n = len(s)
c = 1
res = ""
for i in range(1,n):
    if s[i] == s[i-1]:
        c = c + 1
    else:
        res = res + s[i-1] + str(c)
        c = 1
res = res + s[-1] + str(c)
print(res)
'''
#Vowels in string
'''
s = input()
for i in s:
    if i not in "aeiouAEIOU":
        print("No")
        break
else:
    print("Yes")
'''
#VC & CC
s = input()
x = "aeiouAEIOU"
vc=cc=0
for i in s:
    if i.isalpha():
        if i in x:
            vc = vc + 1
        else:
            cc = cc + 1
print(vc,cc)

#Built in functions
'''
print(abs(-10))
print(abs(10))
print(ord("a"))
print(ord("A"))
print(chr(97))
print(chr(65))
print(eval("10+20"))
print(eval("20%10"))
a = 10
print(id(a))
print(bin(10))
print(hex(34))
print(oct(16))
print(max(10,20,30))
print(min(10,20,30))
print(sum([10,20,30]))
'''
#User Defined Functions
#Way too long words
#Approach - 1[Normal Method]
'''
s = input()
if len(s) <= 10:
    print(s)
else:
    res = ""
    res = res + s[0]
    res = res + str(len(s)-2)
    res = res + s[-1]
    print(res)
'''
#Approach - 2 [WPWR]
'''
def fun1(s):
    if len(s)<=10:
        return s
    else:
        res = ""
        res = res + s[0]
        res = res + str(len(s)-2)
        res = res + s[-1]
        return res
t = int(input())
for i in range(t):
    x = input()
    print(fun1(x))
'''
#Approach - 3 [WPWOR]
'''
def fun1(s):
    if len(s)<=10:
        print(s)
    else:
        res = ""
        res = res + s[0]
        res = res + str(len(s)-2)
        res = res + s[-1]
        print(res)
t = int(input())
for i in range(t):
    x = input()
    fun1(x)
'''
#Approach - 4 [WOPWR]
'''
def fun1():
    s = input()
    if len(s)<=10:
        return s
    else:
        res = ""
        res = res + s[0]
        res = res + str(len(s)-2)
        res = res + s[-1]
        return res
t = int(input())
for i in range(t):
    print(fun1())
'''
#Approach - 5 [WOPWOR]
'''
def fun1():
    s = input()
    if len(s)<=10:
        print(s)
    else:
        res = ""
        res = res + s[0]
        res = res + str(len(s)-2)
        res = res + s[-1]
        print(res)
t = int(input())
for i in range(t):
    fun1()
'''
#Default Arguments
'''
def fun(a=10,b=20):
    print(a+b)
fun()
fun(20)
fun(100,200)
'''
#Required Arguments
'''
def fun(a,b):
    print(a+b)
#fun()
#fun(20)
fun(100,200)
'''
#Keywords arguments
'''
def fun(a=10,b=20):
    print(a+b)
fun()
fun(b=20)
'''
#Varibale number of arguments
'''
def fun(*x):
    res = 0
    for i in x:
        res = res + i
    print(res)
fun()
fun(1)
fun(1,2)
fun(1,2,3,4)
'''
#function
'''
def add(a,b):
    return (a+b)
print(add(10,20))

add = lambda a,b : a+b
print(add(10,20))
'''
#Lambda with Filter
'''
x = [10,11,12,13,14,15]
res = list(filter(lambda a : a%2==0,x))
print(res)
'''
#lambda with Map
'''
x = [99,199,299,399]
res = list(map(lambda a : a+1,x))
print(res)
'''

#Recursion - 1
'''
def calc(n):
    if n >= 1:
        print(n)
        calc(n-1)
calc(10)
'''
#Recursion - 2
'''
import sys
sys.setrecursionlimit(2000)
def calc(n):
    print(n)
    calc(n+1)
calc(1)
'''
#Recursion - 3
#While Loop
'''
n = int(input())
while n > 1:
    if n%2 == 0:
        print(n)
    n = n - 1
'''
#Recursion
'''
def name(n):
    if n > 1:
        if n%2 == 0:
            print(n)
        name(n-1)
    else:
        return
name(10)
'''
#Recursion - 4
#While
'''
n = int(input())
x = 1
while x <= n:
    print(x)
    x = x + 1
'''
#Recusrion
'''
def xyz(n,k):
    if k <= n:
        print(k)
    else:
        return
    xyz(n,k+1)
xyz(10,1)
'''
#Recursion - 5
#Factorial Value
'''
def fact(n):
    if n==1:
        return 1
    else:
        return n * fact(n-1)
print(fact(5))
'''
#Recursion - 6
#While Loop
'''
t = int(input())
while t > 0:
    x = int(input())
    if x%2 == 0:
        print("even")
    else:
        print("Odd")
    t = t - 1
'''
#Recursion - 1
'''
def recr(t):
    if t == 0:
        return
    else:
        n = int(input())
        evenorodd(n)
    recr(t-1)
def evenorodd(n):
    if n%2==0:
        print("Even")
    else:
        print("Odd")
t = int(input())
recr(t)
'''
#Recursion - 2
'''
def recr(t):
    if t == 0:
        return
    else:
        n = int(input())
        if n%2==0:
            print("Even")
        else:
            print("Odd")
    recr(t-1)

t = int(input())
recr(t)
'''



    
#Global Variable
'''
x = 10
def fun():
    print(x)
print(x)
fun()
'''
#Local Variable
'''
def fun():
    x = 10
    print(x)
fun()
print(x)
'''
#Local and Global
'''
x = 10
def fun():
    y = 20
    print(x)
    print(y)
fun()
print(x)
print(y)
'''
#Local and global
'''
x = 10
def fun():
    x = 20
    print(x)
print(x)
fun()
'''
'''
def hello():
    for i in range(1,6):
        yield i
x = hello()
for i in x:
    print(i)
'''
'''
def infinite_even():
    n = 0
    while True:
        yield n
        n = n + 2
z = infinite_even()
for i in range(100):
    print(next(z))
'''

        













    











    


















    
        
        








































