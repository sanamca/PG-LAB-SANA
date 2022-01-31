str=input("enter string:")
print("string is",str)
if(str.endswith("ing")):
    str=str+'ly'
else:
        str=str+'ing'
print("the formatted string is:",str)       
