# program to create dictionary of student marks

marks = {
    "Aman": 85,
    "Rohan": 78,
    "Priya": 92,
    "Sneha": 74
}

name = input("Enter student name: ")

if name in marks:
    print("Marks of", name, "are", marks[name])
else:
    print("Student not found")
