sabziList = ["allo","bhindi","tamatar","Panner",5,0.5,1,500]

# sabziList.append("Dhaniya patta")
# print(sabziList)

# sabziList.clear()
sabziList2 = sabziList.copy()


sabziList2.extend(["aloo","bhindi","allo","Panner","Panner","Panner"])
# print(sabziList2)
# print(f"so ocuurenec of {sabziList2[3]} is {sabziList2.count("Panner")} times. ")

# print(sabziList2.index("Panner"))


sabziList2.insert(3,"khoya")
# print(sabziList2) 

sabziList2.pop(-4) # pop jo hai wo index k through remove krta hai, mtlb wo -4 index hai naki koi value
# print(sabziList2)

sabziList2.remove("bhindi") # remove jo hai wo value k hisab se delete krta hai, or value ki frst occurence ko delete krta hai
# print(sabziList2)

sabziList2.reverse()
# print(sabziList2)

# sabziList2.sort() # sort not work with mixed lists.

cubeOf3 = [x*x*x for x in range(1,11)] 
# print(cubeOf3)

oddList = [i for i in range(1,21) if (i % 2 != 0)] 
''' Flow :-
(i) Phle loop chalega
(ii) Phir condition check hogi (if condition lagaya hai to, agr nii to sidha experession apply hoga)
(iii)Expression apply hoga
(iv) Then List me add hoga'''
print(oddList)