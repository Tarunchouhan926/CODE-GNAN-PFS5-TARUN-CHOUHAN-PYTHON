from os import *

#mkdir("sample")
#rmdir("sample")
#mkdir("sample 1")
#mkdir("sample 2")
#print(listdir())
#chdir("sample 1")
#print(listdir())

'''
import datetime
print(datetime.datetime.now())
print(datetime.date.today())
'''

import datetime
x = datetime.date(2024,7,29)
print(x)

from datetime import date
y = date(2024,7,29)
print(y)

'''
class sai:
    def __init__(self):
        print("I am a constructor")
    a = 10
    b = 20
    def wopwor(self):
        print("I am WOPWOR")
    def wopwr(self):
        return "I am WOPWR"
    def wpwor(self,a,b):
        x = a+b
        print("I am WPWOR,",x)
    def wpwr(self,a,b):
        x = a*b
        res = "I am WPWR" + str(x)
        return res
ob1 = sai()
print(ob1.a)
print(ob1.b)
ob1.wopwor()
print(ob1.wopwr())
ob1.wpwor(10,20)
a = ob1.wpwr(2,5)
print(a)
x1 = sai()
x2 = sai()
x1.wpwor(2,5)
x2.wpwor(5,5)
x1 = sai()
x2 = sai()
'''
'''
class sai1:
    def __init__(self,a,b):
        print(a+b)
x1 = sai1(10,20)
x2 = sai1(100,200)
'''
'''
class xyz:
    def __init__(self,a,b):
        print(a+b)
n1 = 30
n2 = 40
x1 = xyz(n1,n2)
'''
class details:
    def __init__(self):
        self.name = input("enter Your Name : ")
        self.mobile = int(input("enter Your Mobile Number : "))
    def display1(self):
        print("My name is :",self.name)
    def display2(self):
        print("My Mobile number is :",self.mobile)
ob1 = details()
ob1.display1()
ob2 = details()
ob2.display1()
'''
class xyz:
    a = 10
    b = 20
    def __init__(self):
        print("I am constructor")
    def display(self,name):
        print("Hello",name)
x1 = xyz()
x1.display("Sai Vardhan")
'''
#Access specifiers
#Public Access Specifier
'''
class xyz:
    value = 0
    def __init__(self):
        self.value = 100
    def display(self):
        print(self.value)
obj = xyz()
obj.display()
obj.value = 200
obj.display()
'''
#Private Access Specifier
'''
class xyz:
    __value = 0
    def __init__(self):
        self.__value = 100
    def display(self):
        print(self.__value)
obj = xyz()
obj.display()
obj.__value = 200
obj.display()
'''
#Encapsulation
'''
class car:
    def fuel(self):
        print("Fuel : 75%")
    def indicator(self):
        print("Left indicatior Enabled")
    def speedometer(self):
        print("Speed 100km/hr")
    def __init__(self):
        print("I am Odometer")
        self.fuel()
        self.indicator()
        self.speedometer()
c1 = car()
'''

#Multi level Inheritance
'''
class A:
    def fun1(self):
        print("I am from class a")
class B(A):
    def fun2(self):
        print("I am from class b")
class c(B):
    def fun3(self):
        print("I am from class c")
oc = c()
oc.fun3()
oc.fun2()
oc.fun1()
'''
#Hirarical Inheritance
'''
class A:
    def fun1(self):
        print("I am from class a")
class B(A):
    def fun2(self):
        print("I am from class b")
class C(A):
    def fun3(self):
        print("I am from class c")
oc = C()
oc.fun3()
oc.fun1()
ob = B()
ob.fun2()
ob.fun1()
'''
#Hybrid Inheritance
'''
class A:
    a = 10
class B(A):
    b = 20
class C(A):
    c = 30
class D(C):
    d = 40
od = D()
print(od.d)
print(od.c)
print(od.a)
print(od.b)
'''
#Problem
'''
class A:
    def abc(self):
        a = 10
        b = 20
        return a
class B(A):
    def xyx(self):
        print(self.abc())
ob = B()
ob.xyx()
'''
#Abstraction
'''
from abc import ABC,abstractmethod
class A(ABC):
    @abstractmethod
    def abc(self):
        print("I am abc")
    def xyz(self):
        print("I am xyz")
oa = A()
'''
#Exception Handling
#Example - 1
'''
try:
    a = 10
    b = "mnl"
    c = a + b
except:
    print("Error Occured")
else:
    print(c)
finally:
    print("I am Final Block")
'''
#Example - 2
'''
try:
    a = 10
    c = z
except ZeroDivisionError:
    print("Denominator should not be 0")
except TypeError:
    print("Type error occured")
except:
    print("Other Error Occured")
else:
    print(c)
finally:
    print("Finally Block")
'''
#Example - 3
'''
try:
    a = 10
    c = z
except ZeroDivisionError:
    print("Denominator should not be 0")
except TypeError:
    print("Type error occured")
except Exception as e:
    print(e)
else:
    print(c)
finally:
    print("Finally Block")
'''
























    









