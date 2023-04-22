##write a program input three size of trangle and check weather it is eqilateral, isosceles, scalene
a=int(input("Enter the First side of Triangle"))
b=int(input("Enter the Second side of Triangle"))
c=int(input("Enter the third side of Triangle"))
if(a==b and b==c and c==a):
    print("eqilateral triangle")
elif a==b or b==c or c==a:
    print("isosceles triangle")
elif a!=b and b!=c and c!=a:
    print("scalene traingle") 