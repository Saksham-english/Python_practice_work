# Take two sets and apply set operations on them .
# Taking input for two sets
s1 = set(input("Enter elements of first set separated by space: ").split())
s2 = set(input("Enter elements of second set separated by space: ").split())

print("\nSet s1:", s1)
print("Set s2:", s2)

# Set operations
print("\nUnion:", s1 | s2)
print("Intersection:", s1 & s2)
print("Difference (s1 - s2):", s1 - s2)
print("Difference (s2 - s1):", s2 - s1)
print("Symmetric Difference:", s1 ^ s2)
