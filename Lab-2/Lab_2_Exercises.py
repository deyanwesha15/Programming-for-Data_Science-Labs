
# Exercise 1: Course Marks with a List

marks = [75, 82, 68, 91, 45]

total = 0
passed = 0

for mark in marks:
    total += mark

    if mark >= 50:
        passed += 1

average = total / len(marks)
highest = max(marks)
lowest = min(marks)

print("Course Marks:", marks)
print("Total Marks:", total)
print("Average Marks:", average)
print("Highest Mark:", highest)
print("Lowest Mark:", lowest)
print("Courses Passed:", passed)

# Exercise 2: Weekend Temperature with a Tuple

temperatures = (28, 31, 26, 29, 33, 27)

print("Weekend Temperatures:")

for temperature in temperatures:
    print(temperature, "°C")

print("Highest Temperature:", max(temperatures), "°C")
print("Lowest Temperature:", min(temperatures), "°C")

# Exercise 3: Word Analyzer

text = input("Enter a word or short sentence: ")

characters = len(text)
vowels = 0
spaces = 0

for char in text:
    if char.lower() in "aeiou":
        vowels += 1

    if char == " ":
        spaces += 1

print("Number of Characters:", characters)
print("Number of Vowels:", vowels)
print("Number of Spaces:", spaces)

# Exercise 4: Grade Calculator Function

def calculate_grade(marks):
    average = sum(marks) / len(marks)

    if average >= 80:
        grade = "A"
    elif average >= 70:
        grade = "B"
    elif average >= 60:
        grade = "C"
    elif average >= 50:
        grade = "D"
    else:
        grade = "F"

    return grade


marks = [85, 78, 90, 72, 80]

grade = calculate_grade(marks)

print("Marks:", marks)
print("Average:", sum(marks) / len(marks))
print("Grade:", grade)

# Exercise 5: Shopping Cart Processor

products = [
    {"name": "Notebook", "price": 120, "quantity": 3},
    {"name": "Pen", "price": 20, "quantity": 5},
    {"name": "USB Drive", "price": 850, "quantity": 2},
    {"name": "Mouse", "price": 650, "quantity": 1}
]

total = 0

for product in products:
    cost = product["price"] * product["quantity"]
    total += cost

    print(
        product["name"],
        "- Cost:",
        cost
    )


def apply_discount(total):
    if total >= 2000:
        return total * 0.90
    else:
        return total


final_price = apply_discount(total)

print("Total Cart Cost:", total)
print("Final Price After Discount:", final_price)

# Exercise 6: Countdown

number = int(input("Enter a number: "))

while number >= 0:
    print(number)
    number -= 1

print("Countdown finished!")

# Problem 6: Countdown

number = int(input("Enter a non-negative integer: "))

if number < 0:
    print("Please enter a non-negative integer.")
else:
    while number >= 0:
        print(number)
        number -= 1
       
 # Problem 7: Student Record Analyzer

students = [
    {"name": "Rahim", "department": "CSE",
     "marks": 85, "attendance": 92},

    {"name": "Karim", "department": "CSE",
     "marks": 48, "attendance": 76},

    {"name": "Sara", "department": "DS",
     "marks": 91, "attendance": 95},

    {"name": "Nadia", "department": "DS",
     "marks": 67, "attendance": 84},

    {"name": "Hasan", "department": "CSE",
     "marks": 73, "attendance": 78}
]

passed_students = 0
total_marks = 0
highest_student = students[0]

for student in students:
    print(
        "Name:", student["name"],
        "| Marks:", student["marks"]
    )

    total_marks += student["marks"]

    if student["marks"] >= 50:
        passed_students += 1

    if student["marks"] > highest_student["marks"]:
        highest_student = student

average = total_marks / len(students)

print("\n----- Class Summary -----")
print("Total Students:", len(students))
print("Passed Students:", passed_students)
print("Class Average:", average)
print("Highest Mark:", highest_student["marks"])
print("Top Student:", highest_student["name"])

# Problem 8: Product Inventory Summary

products = [
    {"name": "Notebook", "price": 120, "quantity": 3},
    {"name": "Pen", "price": 20, "quantity": 5},
    {"name": "USB Drive", "price": 850, "quantity": 2},
    {"name": "Mouse", "price": 650, "quantity": 1}
]

total_inventory_value = 0
highest_product = None
highest_line_total = 0

for product in products:
    line_total = product["price"] * product["quantity"]

    print(
        "Product:", product["name"],
        "| Line Total:", line_total
    )

    total_inventory_value += line_total

    if line_total > highest_line_total:
        highest_line_total = line_total
        highest_product = product["name"]

print("\n----- Inventory Summary -----")
print("Total Inventory Value:", total_inventory_value)
print("Highest Value Product:", highest_product)
print("Highest Line Total:", highest_line_total)

