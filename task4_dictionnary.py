class Student:
    def __init__(self, name, age, gpa):
        self.name = name
        self.age = age
        self.gpa = gpa

student1 = Student("Alice", 20, 3.8)
student2 = Student("Bob", 22, 3.5)
student3 = Student("Charlie", 21, 3.9)

students = [student1, student2, student3]

students.sort(key=lambda student: student.name)

print("Sorted by name (alphabetical order):")
for student in students:
    print(f"Name: {student.name}, Age: {student.age}, GPA: {student.gpa}")

students.sort(key=lambda student: student.gpa)

print("\nSorted by GPA (ascending order):")
for student in students:
    print(f"Name: {student.name}, Age: {student.age}, GPA: {student.gpa}")

students.sort(key=lambda student: student.gpa, reverse=True)

print("\nSorted by GPA (descending order):")
for student in students:
    print(f"Name: {student.name}, Age: {student.age}, GPA: {student.gpa}")
