#creating a set
'''
s={1,2,3,4}
print(s)

s1={1,2,3,4,4.13,"python"}
print(s1)

s2=set([1,2,3,4])
print(s2)

s3=set(map(int,input().split()))
print(s3)

#Accessing of set elements

s4={1,2,3,4,5,6}
for i in s4:
    print(i,end=" ")

#Set methods
'''
#add

s1={1,2,3,4,5,6,7}
s1.add(10)
print(s1)

#update

s1={1,2,3,4,5,6,7}
s2={8,9,3}
s1.update(s2)
print(s1)

#copy

s1={1,2,3,4,5,6,7}
s2=s1.copy()
print(s2)

#clear

s1={1,2,3,4,5,6,7}
s1.clear()
print(s1)

#remove

s1={1,2,3,4,5,6,7}
s1.remove(2)
print(s1)

#discard
s1 = {1, 2, 3, 4, 5, 6, 7}
s1.discard(3)
print(s1)  # Output: {1, 2, 4, 5, 6, 7}
)
#pop

s1 = {1, 2, 3, 4, 5, 6, 7}
popped_element = s1.pop()
print(popped_element)  # Output: (an arbitrary element from the set, e.g., 1)
print(s1)  # Output: {2, 3, 4, 5, 6, 7}

#union
s1 = {1, 2, 3}
s2 = {3, 4, 5}
s3 = s1.union(s2)
print(s3)  # Output: {1, 2, 3, 4, 5}

#intersection
s1 = {1, 2, 3}
s2 = {3, 4, 5}
s3 = s1.intersection(s2)
print(s3)  # Output: {3}

#intersection_update
s1 = {1, 2, 3}
s2 = {3, 4, 5}
s1.intersection_update(s2)
print(s1)  # Output: {3}

#intersection set
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
intersection_set = set1 & set2
print(intersection_set)  # Output: {3, 4}

#differnce
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
difference_set = set1 - set2
print(difference_set)  # Output: {1, 2}


#difference update
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
set1.difference_update(set2)
print(set1)  # Output: {1, 2}

#Symmetric Difference

set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
symmetric_difference_set = set1.symmetric_difference(set2)
print(symmetric_difference_set)# Output: {1, 2, 5, 6}

#Symmetric Difference update

set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
set1.symmetric_difference_update(set2)
print(set1)  # Output: {1, 2, 5, 6}

#Is Disjoint#no common elements returns true
set1 = {1, 2, 3}
set2 = {4, 5, 6}
print(set1.isdisjoint(set2))  # Output: True

#is subset() all the elements of set 1 are in set2 
set1 = {1, 2}
set2 = {1, 2, 3, 4}
print(set1.issubset(set2))  # Output: True

#issuperset() All elements of set2 (which are {1, 2}) are present in set1.
set1 = {1, 2, 3, 4}
set2 = {1, 2}
print(set1.issuperset(set2))  # Output: True
