# numList = [i for i in range(1,11)]
# print(numList[:3])
# print(numList[-3:])

newList = [7,8,5,2,3,5,65,2,7,8,8,]
newSet = set(newList)
updatedList = list(newSet)

print(updatedList)


prodcutDict = {
    "Pc":100000,
    "Gaming Chair":1000,
    "Pc setup":5000,
    "Chairs": 15000
}

sum= 0

for i in prodcutDict.values():
    if (i > 0):
        sum = i

