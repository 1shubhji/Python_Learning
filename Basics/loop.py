# for loop 
# i is variable and range(10) is iterable mtlb jispe iterate kiya ja rha hai, ek or chiz yha range ek python ka built-in function hai
# for i in range(10):
#     print(i)

# for iterator in range(0,10):
#     print(iterator)

# And both the loops give the same output

# WHile Loop

# i=0;
# while(i<10):
#     print(i)
#     i+=1;


# So this is while loop


# Break, continue and pass

print("This is break : ")
i=0;
while(i<10):
    if i==5:
        break;
    print(i)
    i+=1;
# output is : 0,1,2,3,4


print("This is Continue : ")
j=0;
while(j<10):
    if j==5:
      j+=1;
      continue;
    print(j)
    j+=1;
# output will be :0,1,2,3,4,6,7,8,9


print("This is Pass : ")
k=0;
while(k<10):
    if k==5:
        pass;
    print(k)
    k+=1;
# output will be: 0,1,2,3,4,5,6,7,8,9