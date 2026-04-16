
# code to check that you can vote or not : 

# age = int(input("Enter Your Age"));

# if(age < 18):{
#     print("You can't Vote")
# }
# else:{
# print("You can Vote")
#     }

# *****************************************************************

# Basic Calculator App 

firstValue = int(input("Enter the first Value :"))
seconodValue = int(input("Enter the second value"))
operator = input("Enter the operation which you want to do with them: ")


match (operator):
    case ("+"):
        print(f"The sum of {firstValue} and {seconodValue} is {firstValue + seconodValue}");
    case ("-"):
        print(f"The subtraction of {firstValue} and {seconodValue} is {firstValue - seconodValue}");
    case ("*"):
        print(f"The multiplication of {firstValue} and {seconodValue} is {firstValue * seconodValue}");
    case ("/"):
        print(f"The division of {firstValue} and {seconodValue} is {firstValue / seconodValue}");
    case _:
        print(f"Type a valid operator : ");
    

