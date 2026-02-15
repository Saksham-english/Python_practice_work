# scan n values in range of 0-3 and print the no. of times each value has occured .
n = int(input("Enter number of values: "))

count = [0, 0, 0, 0]   # For 0,1,2,3

print(f"Enter {n} values (between 0 and 3):")

for _ in range(n):
    value = int(input())
    
    if 0 <= value <= 3:
        count[value] += 1
    else:
        print("Invalid input! Enter numbers between 0 and 3 only.")

print("\nOccurrences:")
for i in range(4):
    print(f"{i} occurs {count[i]} times")
