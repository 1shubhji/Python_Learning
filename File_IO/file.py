# f = open(r"C:\Users\sharm\Finishing_Python\File_IO\shubham.txt","rt")

# content = f.read()

# print(content)

# f.close()


""" 
Opening file "with" keyword, it's a context management.
If anyhow error happens before close() → file never closes
👉 This can cause:

-> memory issues
-> file lock issues
-> resource leaks

So, what with does :- 
👉 Behind the scenes:

-> File opens
-> Code runs
-> Automatically closes file, even if error happens.
"""


# with open("shubham.txt","r") as f:
#     content = f.read()
#     print(content)


with open("rahaysya.txt","w") as newFile:
    
    nayaContent = """ 1. Hello duniya walo
    2. ye mera rahaysaya hai, or mai ab is rahaysya ko secret nii rakhna chahta
    3. ab mai isko freedom of sppech dena chahta hu. 

"""

    newFile.write(nayaContent)


with open("rahaysya.txt","a") as appendingSomething:

    phirSeNayaContent = "ye ab nayi line hia jo mai phir se add krna chahta hu "
    appendingSomething.write(phirSeNayaContent)
 