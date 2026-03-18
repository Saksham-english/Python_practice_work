#LAB MANNUAL 
# Create a class student and instantiate 3 objects by taking inputs from the user and display the details of the students.
class student:
    def __init__(self, name, age, course, marks):
        self.name=name
        self.age=age
        self.course=course
        self.marks=marks

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Course:", self.course)
        print("Marks:", self.marks)
        print()

students=[]

for i in range(3):
    print("Enter details of student", i+1)

    name=input("Enter name: ")
    age=int(input("Enter age: "))
    course=input("Enter course: ")
    marks=float(input("Enter marks: "))

    s=student(name, age, course, marks)
    students.append(s)


print("\n__________Student Details____________\n")

for s in students:
    s.display()

