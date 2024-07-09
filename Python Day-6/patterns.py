#Patterns
# # #
# # #
# # #
'''
for i in range(3):
    for j in range(3):
       print("#",end=" ")
    print()
-------------------------------    
# 
# # 
# # # 
# # # # 
# # # # # 

for i in range(5):
    for j in range(5):
         if j<=i:
           print("#",end=" ")
    print()
-------------------------------
#Approach - 1
1 1 1 1 1 
2 2 2 2 2 
3 3 3 3 3 
4 4 4 4 4 
5 5 5 5 5 
 
x=1
for i in range(5):
    for j in range(5):
        print(x,end=" ")
    x=x+1
    print()

#Approach - 2

for i in range(5):
    for j in range(5):
        print(i+1,end=" ")
    print()

#Approach - 3

for i in range(5):
    x=str(i+1)+" "
    x1=x*5
    print(x1)

----------------------------------

1 2 3
4 5 6
7 8 9

x=0
for i in range(3):
    for j in range(3):
        x=x+1
        print(x,end=" ")
    print()

-----------------------------------
# # # # #
#  # # #
# # #
# #
#

for i in range(5):
    for j in range(5):
        if(j>=i):
          print("#",end=" ")
    print()

------------------------------------

#
# #
# # #
# # # #
# # # # #
# # # #
# # #
# #
#

for i in range(5):
    for j in range(5):
        if j<=i :
         print("#",end=" ")
    print()
for I in range(4):
    for J in range(4):
        if J>=I:
         print("#",end=" ")
    print()

------------------------------------
# # # # # 
1 2 3 4 5 
# # # # # 
1 2 3 4 5 
# # # # #

for i in range(5):
    for j in range(5):
       if i%2!=0:
        print(j+1,end=" ")
       else:
        print("#",end=" ")
    print()

-------------------------------------
# # # # #
# @ @ @ #
# @ @ @ #
# @ @ @ #
# # # # #

n=int(input("enter the number"))
for i in range(n):
   for j in range(n):
      if i==0 or j==0 or i==n-1 or j==n-1:
         print("#",end=" ")
      else:
          print("@",end=" ")
   print()

----------------------------------------

# # # # #
#       #
#       #
#       #
# # # # #


for i in range(5):
    for j in range(5):
        if i==0 or i==4 or j==0 or j==4:
            print("#",end=" ")
        else:
            print(" ",end=" ")
    print()

-----------------------------------------

1
1 2
1   3
1     4
1 2 3 4 5
'''
for i in range(5):
    for j in range(5):
       if j==0 or j==i or i==4:
           print(j+1,end=" ")
       elif j < i:
            print(" ",end=" ")
    print()
            
