def fact(f):
    "fact of num"
    for i in range(1,f+1):
        if f % i==0:
            print(i)
fact(5)
