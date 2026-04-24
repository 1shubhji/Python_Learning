class Point:
    def __init__(self,x,y):
        self.x = x 
        self.y = y

    def sum(self,newPoint):
        return Point((self.x + newPoint.x),(self.y + newPoint.y))

    def print_sum(self):
        print(f"The Co-ordinates of sum of these points x = {self.x} and y = {self.y}. ") 