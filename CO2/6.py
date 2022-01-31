t_str=str(input("enter a string:"))
freq={}
for i in t_str:
    if i in freq:
        freq[i]+=1
    else:
        freq[i]=1
        print("count all char:"+str(freq))
