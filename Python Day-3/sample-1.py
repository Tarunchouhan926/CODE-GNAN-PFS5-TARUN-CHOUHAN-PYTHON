'''#case-1
name=input("enter your name:")
age=int(input("enter your age:"))
print(name)
print(age)

#case-2(using .format)

print("my name is {},{} is my age".format(name,age))

#case-3(using f-string)

print(f"my name is {name},{age} is my age")
'''

#Task

fname,lname=input("enter your name[fname-lname]:").split("-")
height1,height2=input("enter your height:").split("-")
height=(f"{height1}.{height2}:")
age=int(input("enter your age:"))
salary=float(input("enter your salary:"))

print(f"First name:{fname}")
print(f"last name:{lname}")
print(f"height:{height}")
print(f"Age:{age}")
print(f"salary:{salary:.0f}\-")


