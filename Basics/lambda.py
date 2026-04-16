# Lambda function ....

# cube = lambda x: x*x*x
# print(cube(5))

# Fibonacci Series ....

# n = int(input("Enter number of terms: "))

# a = 0
# b = 1

# for i in range(n):
#     print(a, end=" ")
#     c = a + b
#     a = b
#     b = c

# Now writting fibonacci through "recursion" ....

fibValue = int(input("Enter any value to find the fibonacci\n"))

def fibonacci(n):
    if(n == 0 or n==1):
        return n
    
    return fibonacci(n-2) + fibonacci(n-1)

print(fibonacci(fibValue));

