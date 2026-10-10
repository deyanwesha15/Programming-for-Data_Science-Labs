
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
