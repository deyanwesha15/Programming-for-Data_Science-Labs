# Problem 1: Basic Arithmetic

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print("Sum:", num1 + num2)
print("Difference:", num1 - num2)
print("Product:", num1 * num2)

if num2 != 0:
    print("Quotient:", num1 / num2)
else:
    print("Quotient cannot be calculated because divisor is zero.")

    # Problem 2: Student Profile

name = input("Enter student name: ")
student_id = input("Enter student ID: ")
age = int(input("Enter age: "))
department = input("Enter department: ")
cgpa = float(input("Enter CGPA: "))

print("\n----- Student Profile -----")
print("Name:", name)
print("Student ID:", student_id)
print("Age:", age)
print("Department:", department)
print("CGPA:", cgpa)

# Problem 3: Temperature Conversion

celsius = float(input("Enter temperature in Celsius: "))

fahrenheit = (celsius * 9 / 5) + 32
kelvin = celsius + 273.15

print("Temperature in Celsius:", celsius)
print("Temperature in Fahrenheit:", fahrenheit)
print("Temperature in Kelvin:", kelvin)

# Problem 4: Course Marks Analysis

name = input("Enter student name: ")

marks = []

for i in range(5):
    mark = float(input(f"Enter marks for course {i + 1}: "))
    marks.append(mark)

total = sum(marks)
average = total / len(marks)
highest = max(marks)
lowest = min(marks)

passed_courses = 0

for mark in marks:
    if mark >= 50:
        passed_courses += 1

print("\n----- Result Summary -----")
print("Student Name:", name)
print("Marks:", marks)
print("Total Marks:", total)
print("Average Marks:", average)
print("Highest Mark:", highest)
print("Lowest Mark:", lowest)
print("Passed Courses:", passed_courses)