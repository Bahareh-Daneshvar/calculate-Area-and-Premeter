from math import pi
x=int(input("input a number between 1,2,3 for the geometric shapes:\n 1.circle\n 2.square \n 3.rectangle \n "))
if x==1:
 r=float(input("input the radius:"))
 circle_perimeter=2*pi*r
 print("The area of circle is equal to: ", pi*r*r )
 print("The perimeter of circle is equal to: ", 2*pi*r )
elif x==2:
 r=float(input("input the lenght of each side: "))
 print("The area of square is equal to: ", r*r )
 print("The perimeter of square is equal to: ", 4*r )
elif x==3:
 r1=float(input("input the lenght of a side: "))
 r2=float(input("input the lenght of the other side: "))
 print("The area of square is equal to: ", r1*r2 )
 print("The perimeter of square is equal to: ", 2*r1*r2 )
else:
 print("you intered a wrong number" )
   