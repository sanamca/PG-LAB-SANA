class rectangle:

  def __init__(self,l,b):
    self.__length=l
    self.__breadth=b     

  def area(self):
    self.area=self.__length*self.__breadth
    print("Area of Rectangle: ",self.area)

  def __lt__(self,second):
   if self.area < second.area:
    return True
   else:
    return False

print("Rectangle 1")
length1=int(input("Enter the length:"))
breadth1=int(input("Enter the breadth:"))
obj1=rectangle(length1,breadth1)
obj1.area()

print("\nRectangle 2")
length2=int(input("Enter the length:"))
breadth2=int(input("Enter the breadth:"))
obj2=rectangle(length2,breadth2)
obj2.area()

if obj1 > obj2 :
    print("\nRectangle 1 is Larger.....")
else:
    print("\nRectangle 2 is Larger....")
