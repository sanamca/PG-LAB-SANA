s=int(input("enter the 1st year"))
l=int(input("enter the last year"))
if(s<l):
    print("laep yera is",end=" ")
for i in range(s,l):
    if i%4==0 and i%100!=0:
        print(i,end=" ")
        