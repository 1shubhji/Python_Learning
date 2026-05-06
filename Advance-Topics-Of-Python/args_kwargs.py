
from functools import reduce

# args is basically a tuple
def sum(*args):

    # print(type(args))
    return reduce(lambda x,y: x+y, args)
    # return sum(args)

print(sum(1,2,34,5,0))

# kwargs is basically a dictionarry
def students(**kwargs):
    for keys,values in kwargs.items():
        print(f"{keys} : {values}")


students(Shubham=15, HarryBhai =5, Gurmeet = 78, priya = 18)



def argsAndKwargs(*args, **kwargs):
    print(args,kwargs)


argsAndKwargs(7,8,5,2,3,5, shubham =78, munni = 74, chutki = 45, bheem =12)


