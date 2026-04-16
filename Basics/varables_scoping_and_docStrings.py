def fibonaaci(n):
    '''
    So, this is program to find the sum of n fibonaci series.
    Where we have a parmaeter :

    n = parameter to take input, mean in series starting n digits will be going to be added.

    So to do this, we use recursion function here
    we also take care of the base cases which is, if user want to want to find the fibonacci of 0 and 1. 

    Then after that we return the formula of fibonacci which is "fibo(n-1) + fibo(n-2)"

    So that's all about this function. 
    '''
    if(n == 0 or n==1):
        return n;

    return fibonaaci(n-1) + fibonaaci(n-2)


# print(fibonaaci(5))
# print(fibonaaci.__doc__)

# print(def.__doc__)

def faltu_chiz(fName,lName):
    return (f"So your first name is {fName} and last name is {lName}")

# print(faltu_chiz("Shubham","Kumar"))

sum = lambda a,b: a+b

# print(sum(5,7))

# function of 
def factorial(n):
    if( n == 0 or n==1 ):
        return 1
    
    return n * factorial(n - 1)

# recursive function of sum of n numbers ...
def sum_of_n_numbers(n):
    if( n == 0 or n==1 ):
        return 1
    
    return n + factorial(n - 1)


print(factorial(5))

