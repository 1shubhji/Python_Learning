# num1 = int(input("Enter first no. :"))
# num2 = int(input("Enter second no. :"))

# def sum(a,b):
#     try:
#         sum =  a + b

#     except Exception as e:
#         print(f"There is an error pls rewrite your code. And you error is {e}")

    
# # else tbhi chlega jb program me try me koi error na ho to
#     else:
#         return (f"dekho else chl gya jb try me koi error nii aya to ,aur sum hai {sum}")

# # finally hamesa chlta hai chahe kuch bhi ho jaye
#     # finally:
#     #     print("Bhai kuch bhi ho jaye mai to chalunga hi ....")

# print(sum(num1,num2))

# # sum(num1,num2)


class myerror(Exception):
    pass

def myerror_msg():
    raise myerror("Kuch bhi galat hua to ye chlega ")


try:
    myerror_msg()

except myerror as e:
    print(f"There is an error pls rewrite your code. And you error is {e}")