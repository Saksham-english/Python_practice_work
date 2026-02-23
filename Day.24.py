# Create a dictionary
student = {
    "name": "Saksham",
    "age": 20,
    "course": "B.Tech"
}

# Print dictionary
print("Original Dictionary:")
print(student)

# Access a value
print("\nName:", student["name"])

# Add a new key-value pair
student["marks"] = 85

# Update a value
student["age"] = 21

# Remove a key
student.pop("course")

# Print updated dictionary
print("\nUpdated Dictionary:")
print(student)