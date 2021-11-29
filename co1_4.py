str1=str(input("enter the string"))
word= str1.split()
count=[]
for w in word:
    count.append(word.count(w))
    print("count occurence is",str(list(zip(word,count))))