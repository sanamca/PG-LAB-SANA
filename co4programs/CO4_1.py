class rectangle():
    def __init__(self,breadth,length):
        self.breadth=breadth
        self.length=length
    def area(self):
         return self.breadth*self.length
    def perimeter(self):
         return 2*(self.breadth+self.length)   
r1=rectangle(10,20)
r2=rectangle(3,5)
print("Area of rectangle 1 :",r1.area())
print("Area of rectangle 2 :",r2.area())
print("Peimeter of rectangle 1:",r1.perimeter())
print("Peimeter of rectangle 2:",r2.perimeter())
if(r1.area()>r2.area()):
     print("recangle 1 is of greater area")
else:
     print("recangle 2 is of greater area")
     