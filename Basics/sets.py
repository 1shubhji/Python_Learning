# Sets are unordered
# Sets has no duplicates

myFirstSet = {5,4,7,8,4,5,1,1,12} # SO set has no duplicates.
# print(myFirstSet)

secondSet = {7,8,4,0,1,50,14,9,8,6,5}

unionSet = myFirstSet.union(secondSet)
# print(f"So this is a set of union of two sets which i created. {unionSet}")

intersectionSet = myFirstSet.intersection(secondSet)
# print(f"So this is a set of intersection of two sets which i created. {intersectionSet}")

differenceSet1 = myFirstSet.difference(secondSet)
differenceSet2 = secondSet.difference(myFirstSet)
# print(f"So this is a set1 of Difference of two sets which i created. {differenceSet1}")
# print(f"So this is a set2 of Difference of two sets which i created. {differenceSet2}")


# Some common methods of sets are :- 

secondSet.add(91)
print(secondSet)

secondSet.remove(0)   
print(secondSet)

# secondSet.remove(545) # if element is not present in sets then, it give an error

secondSet.discard(545)  # if element is not present in sets then, it can't give an error
print(secondSet)

