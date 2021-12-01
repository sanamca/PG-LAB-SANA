str=(input("enter the string"))
print("input string:",str)
if(str.endswith("ing")):
    str=str='ly'
else:
    str=str+'ing'
    print("the result string is",str)