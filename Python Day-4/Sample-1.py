#if
'''
a=int(input("enter the number:"))
if a>0:
  print("positive")


#if-else

a=int(input("enter the number:"))
if a>0:
  print("positive")
else:
  print("negative")

#elif

a=int(input("enter the number:"))
if a>0:
    print("positive")
elif a==0:
    print("not positve not negative")
else :
     print("negative")

#nested if

a=int(input("enter the number:"))
if a%2==0:
      if a>0:
          print("poitive even number")
      elif a==0:
           print("not positve not negative")
      else:
           print("negative even number")
else:
    if a<0:
         print("negative odd number")
    else:
         print("negative even number")

'''
for i in range(1,20):
   print(i)
