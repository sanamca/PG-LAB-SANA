f1 = open("ffile.txt","r")
for x in f1:
    print(x)
print("---------------")
f1.seek(0,0)
ff=f1.readlines()
print("Looping through the file using Readline\n")
print("---------------")
for x in range(0,len(ff)):
    if(x%2==0):
        print(ff[x])
print("---------------")
