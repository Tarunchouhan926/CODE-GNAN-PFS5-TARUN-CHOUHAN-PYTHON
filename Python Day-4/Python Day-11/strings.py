#creation of string
'''
a="hello"
print(a)

#creation of string by input
a=input()
print(a)

#accessing of elements in the string

b="string"
print(b[1])
print(b[-1])

#modifications of strings
b="liger"
print(b)

#del string name
del b
print(b)
'''
#string built in fuctions

#endswith
a="poiuytrewqwertyuiop"
print(a.endswith("p"))
print(a.endswith("q"))

#startswith
print(a.startswith("p"))

#replace
a="hello python"
b=a.replace("hello","namaste")
print(b)

#isdigit

a="12345654321"
print(a.isdigit())

#isalpha
a="asdfghjklkjhgfdsa"
print(a.isalpha())

#isdecimal
a="123456543"
print(a.isdecimal())

#isalnum

a="12345asdfgh"
print(a.isalnum())

#string.lower

a="ASDFGHJKLPOIUYTREWQ"
print(a.lower())

#string.upper

a="asdfghjklkjhgfdsa"
print(a.upper())

#string.swapcase()

a="lkjhgfdsadfghjmk LKJHGFDSDFGHJKL"
print(a.swapcase())

#string.capitalize

a="my name tarun"
print(a.capitalize())

#string.find

a="tarun chouhan"
print(a.find("u"))

#string.rfind
a="tarun chouhan"
print(a.rfind("u"))

#string.count

a="asdfghjklaaaaa"
print(a.count("a"))

#string built in functions

#len()
a="a b"
print(len(a))

#max()
a="AbcdBcdz"
print(max(a))

#min()
a="AbcdBcdz"
print(min(a))

