# WAP to count and display the number of 1. capital letter  2. small letters in a given string .
a= str(input("Enter a string: "))
count =0
small =0
for ch in a :
    if ch.isupper():
        count +=1 
    elif ch.islower():
        small +=1
print(f"Number of capital letters : {count} ")
print(f"Number of small letters : {small}")
print(a)

