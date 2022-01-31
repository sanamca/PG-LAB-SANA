from graphics import rectangle
from graphics import circle
from graphics.ThreeDgraphics import cuboid
from graphics.ThreeDgraphics import sphere

l=int(input("Enter the length,l : "))
b=int(input("Enter the breadth,b : "))
rectangle.perimeter(l,b)
rectangle.area(l,b)

r=int(input("Enter the radius,r : "))
circle.perimeter(r)
circle.area(r)

l=int(input("Enter the length,l : "))
b=int(input("Enter the breadth,b : "))
h=int(input("Enter the height,h : "))
cuboid.perimeter(l,b,h)
cuboid.area(l,b,h)

r=int(input("Enter the radius,r : "))
sphere.volume(r)
sphere.area(r)
