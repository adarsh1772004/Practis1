##write a program to input the prise of television & check the prise of a Television is greater then 50000 then get 10% discount
a=int(input("enter the prise of television"))
if a>50000:
    discount=a*10/100
    print (discount)
else:
    print("No Discount")