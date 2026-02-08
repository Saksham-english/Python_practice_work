import math
# To check whether the quadratic equation has real roots or imaginary roots
a= int(input("Enter coefficient a: "))
b= int(input("Enter coefficient b: "))
c= int(input("Enter coefficient c: "))

D= b**2 - 4*a*c
    
root1= (-b + math.sqrt(abs(D)))/(2*a)
root2= (-b - math.sqrt(abs(D)))/(2*a)

root1= round(root1,2)
root2= round(root2,2)
if D>0:
    print("The roots are real and different")
    print("Root 1: ",root1)
    print("Root 2: ",root2)
elif D==0:
    print("The roots are real and same")
    print("Root: ",root1)
else:
    print("The roots are imaginary")
    print("Root 1: ",root1,"i")
    print("Root 2: ",root2,"i")