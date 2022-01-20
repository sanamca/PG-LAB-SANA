f1=open("ffile.txt","w")
f1.write("This is my first file in python.\nWant to work with files.\nThis is my third.")
f1.close()

f1=open("ffile.txt","r")
f1.seek(0,0)
ff=f1.readlines()
for x in range(0,len(ff)):
    print(ff[x])

print()
print(ff)
f1.close()
