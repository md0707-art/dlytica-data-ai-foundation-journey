# Day 3 Assignment
# Personal Bio-Data Card

print("===== Personal Bio-Data Card =====\n")

# String
name = input("Enter Full Name: ")
city = input("Enter City: ")

# Integer
age = int(input("Enter Age: "))

# Float
height = float(input("Enter Height (in feet): "))

# Boolean
student_answer = input("Are you a student? (yes/no): ").lower()
is_student = student_answer == "yes"

# Tuple
day = int(input("Birth Day: "))
month = int(input("Birth Month: "))
year = int(input("Birth Year: "))

birth_date = (day, month, year)

# List
hobby1 = input("Enter Hobby 1: ")
hobby2 = input("Enter Hobby 2: ")
hobby3 = input("Enter Hobby 3: ")

hobbies = [hobby1, hobby2, hobby3]

# Set
lang1 = input("Enter Language 1: ")
lang2 = input("Enter Language 2: ")
lang3 = input("Enter Language 3: ")

languages = {lang1, lang2, lang3}

# Dictionary
profile = {
    "name": name,
    "city": city,
    "age": age,
    "height": height,
    "student": is_student,
    "birth_date": birth_date,
    "hobbies": hobbies,
    "languages": languages
}

print("\n" + "=" * 40)
print("PERSONAL BIO-DATA CARD")
print("=" * 40)

print(f"Name: {profile['name']}")
print(f"City: {profile['city']}")
print(f"Age: {profile['age']}")
print(f"Height: {profile['height']} ft")
print(f"Student: {profile['student']}")
print(f"Birth Date: {profile['birth_date']}")
print(f"Hobbies: {profile['hobbies']}")
print(f"Languages: {profile['languages']}")

print("\n----- Extra Information -----")

print(f"First Letter of Name: {name[0]}")
print(f"Number of Hobbies: {len(hobbies)}")
print(f"Number of Unique Languages: {len(languages)}")

print("\n----- Data Types -----")

print("Age Type:", type(age))
print("Height Type:", type(height))
print("Student Type:", type(is_student))
print("Birth Date Type:", type(birth_date))
print("Hobbies Type:", type(hobbies))
print("Languages Type:", type(languages))