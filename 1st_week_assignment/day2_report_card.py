# Day 2 Assignment
# Student Report Card Generator

print("===== STUDENT REPORT CARD GENERATOR =====\n")

# Input section
name = input("Enter Student Name: ")
roll_no = input("Enter Roll Number: ")

# Marks input (float casting)
math = float(input("Enter Math Marks: "))
science = float(input("Enter Science Marks: "))
english = float(input("Enter English Marks: "))

# Store in dictionary
student = {
    "name": name,
    "roll_no": roll_no,
    "math": math,
    "science": science,
    "english": english
}

# Total and Percentage
total = math + science + english
percentage = (total / 300) * 100

# Pass/Fail condition (each subject >= 40)
is_pass = (math >= 40 and science >= 40 and english >= 40)

# Grade calculation
if percentage >= 80:
    grade = "A+"
elif percentage >= 70:
    grade = "A"
elif percentage >= 60:
    grade = "B"
elif percentage >= 50:
    grade = "C"
elif percentage >= 40:
    grade = "D"
else:
    grade = "F"

# Distinction using set membership + nested if
distinction_grades = {"A+", "A"}

if grade in distinction_grades:
    if percentage >= 85:
        remark = "DISTINCTION "
    else:
        remark = "FIRST CLASS "
else:
    remark = "NEEDS IMPROVEMENT "

# Final status using ternary operator
status = "PASS " if is_pass else "FAIL "

# Output section
print("\n======================================")
print("           STUDENT REPORT CARD        ")
print("======================================\n")

print(f"Name       : {student['name']}")
print(f"Roll No    : {student['roll_no']}")
print(f"Math       : {student['math']}")
print(f"Science    : {student['science']}")
print(f"English    : {student['english']}")

print("--------------------------------------")
print(f"Total Marks: {total}/300")
print(f"Percentage : {percentage:.2f}%")
print(f"Grade      : {grade}")
print(f"Remark     : {remark}")
print(f"Status     : {status}")
print("======================================")

# Second test case suggestion (for assignment requirement)
print("\nNOTE: Run program twice for testing:")
print("1. Enter high marks (pass case)")
print("2. Enter low marks (fail case)")