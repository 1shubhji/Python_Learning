# name = "Shubham Kumar"
# print(name[0],name[-1],len(name))

# name1 = "Hello"
# name2 = "World"
# print(f"{name1} {name2}")

# Program to count vowel in a given string .

# str1 = input("Enter any string to count vowels in that . ")

# print(f'''
#       a is {str1.count("a")} times.
#       e is {str1.count("e")} times.
#       i is {str1.count("i")} times.
#       o is {str1.count("o")} times.
#       u is {str1.count("u")} times.''')

# function to check if a string is palindrom or not .

def palindormeOrNot(str):
    if (str == str[::-1]):
       print("Yes, it is palindrom. ")

    else:
       print("No, it is not a palindrom. ")


palindormeOrNot("level")