from functools import reduce
import time

def decorator(func):
    def wrapper():
        print("Funciton is going to be executed")
        func()
        print("Function is executed !")
    return wrapper


@decorator
def sayHello():
    print("Hello!")

# sayHello()

# *************************************************************************************

def timer(func):
    def wrapper():
        start = time.time()
        result = func()
        end = time.time()
        print(f"The sum of these no. is {result}  ,Execution time of this function is : {end - start}sec")
    return wrapper

@timer
def sum():
    sume=0

    for i in range(1,1000001):
        sume = sume + i

    return sume

# sum()

# ****************************************************************************************

class Employee:
    def __init__(self,salary):
        self._salary = salary

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self,n):
        if (n > 0):
            self._salary = n
        
        else:
            print("Don't set -ve values to salary.")



# shubham = Employee(300000)

# print(shubham.salary)

# shubham.salary = 500000

# print(shubham.salary)

# ***********************************************************************************

class MathUtils:
    @staticmethod
    def add(a,b):
        return a+b
    
    @classmethod
    def description(cls):
        print("This is a utility class for math operations.")


# print(MathUtils.add(4,5))

# MathUtils.description()

# *************************************************************************************

class Book:
    def __init__(self,title,author):
        self.title = title
        self.author = author

    def __str__(self):
        return (f"{self.title} by {self.author}")
    
    def __len__(self):
        return len(self.title)
    

book1 = Book("Rich dad Poor Dad","Robert Kiyosaki")
book2 = Book("The Psychology of Money","Pta nii")

# print(str(book1))
# print(len(book2))

# *********************************************************************************************

class NegativeNumberError(Exception):
    pass

def isNegativeOrNot(num):
    if (num <0):
        raise NegativeNumberError("Please Don't enter a -ve number. ")
    
    return num

# try:
#     num = isNegativeOrNot(int(input("Enter a no.")))
#     a = 15/num

# except ValueError as e:
#     print("This is not a number !",e)

# except ZeroDivisionError :
#     print("don't try to divide it with zero.")

# except NegativeNumberError as e:
#     print(e)


# **********************************************************************************************

list1 = [1,2,3,4,5]

cube = map(lambda x: x*x*x, list1)

# print(list(cube))

list2 = [10,11,12,13,14]

filterEvenNum = filter(lambda x: x%2 ==0, list2)
# print(list(filterEvenNum))

list3 = [1,2,3,4]

product = reduce(lambda a,b: a*b, list3)

# print(product)


# ********************************************************************************

# while (num := input("Kuch Bhi Likh de Bhai ... ")) != "quit":
    # print("Ye quit k brabar nii hai")



listt = ["python", "rocks", "ai"]

# filteredList = filter(lambda x: len(x) > 4,listt)

# print(list(filteredList))

s= [w for w in listt if (x := len(w)) > 4]

# print(s)

# *********************************************************************************

def sum_all(*args):

    som = reduce(lambda a,b: a+b, args)
    return som

print(sum_all(7,8,9,4,5,6,4,7,8,5,1,1))
    

def printDetails(**kwargs):

    for key,values in kwargs.items():
        print(f"{key} : {values}")


printDetails(name="shubham", age=45, city="Ptanii" )
