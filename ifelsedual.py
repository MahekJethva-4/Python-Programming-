print(" DANCE COMPETITION REGISTRATION")

name = input("Enter participant name: ")
roll_no = input("Enter roll number: ")
class_name = input("Enter class: ")
age = int(input("Enter age: "))

print("\nAvailable Dance Categories:")
print("1. Solo Dance")
print("2. Duet Dance")
print("3. Group Dance")
print("4. Classical Dance")

choice = int(input("Select category (1-4): "))

if choice == 1:
    category = "Solo Dance"
elif choice == 2:
    category = "Duet Dance"
elif choice == 3:
    category = "Group Dance"
elif choice == 4:
    category = "Classical Dance"
else:
    category = "Invalid Category"

if category != "Invalid Category":
    print("\n===== REGISTRATION DETAILS =====")
    print("Participant Name :", name)
    print("Roll Number      :", roll_no)
    print("Class            :", class_name)
    print("Age              :", age)
    print("Dance Category   :", category)
    print("Registration Successful!")
else:
    print("Invalid category selection.")