
from functools import reduce

newTuple = (4,7,8,9,6,4,1)

length = (4,7,8,9,6,4,1)
breadth = [8,4,5,12,7,8,7]

# cubeNo = map(lambda x: x*x*x, newTuple)

# print(list(cubeNo))

AreaOfRectangle = map(lambda x,y: 2*(x+y), length,breadth)

# print(list(AreaOfRectangle))

numTuple = (1,2,3,4,5,6,7,8,9,7,8,9,4,5,6,1,3,3)

evenTuple = filter(lambda x : x%2 == 0, numTuple)

print(list(evenTuple))

sumOfNum = reduce(lambda x,y: x+y, newTuple)

print(sumOfNum)

