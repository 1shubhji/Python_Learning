# So now here we are going to 


class Point:
    def __init__(self,x,y):
        self.x = x 
        self.y = y

    def sum(self,newPoint):
        return Point((self.x + newPoint.x),(self.y + newPoint.y))
    
    def __add__(self, newPoint):
        return Point((self.x + newPoint.x),(self.y + newPoint.y))
    
    def __mul__(self, other):
        return Point((self.x * other.x),(self.y * other.y))

    def priint(self):
        print(f"The Co-ordinates of sum of these points x = {self.x} and y = {self.y}. ") 


p1 = Point(2,5)
p2 = Point(7,9)

# SumOfP = p1.sum(p2)

SumOfP = p1 + p2

productOfP = p1 * p2
productOfP.priint()

SumOfP.priint()