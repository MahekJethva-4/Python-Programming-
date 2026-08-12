print("===== SPORTS DAY REGISTRATION =====")

name = input("Enter student name: ")
roll_no = input("Enter roll number: ")
class_name = input("Enter class: ")
age = int(input("Enter age: "))

print("\nAvailable Events:")
print("1. Running")
print("2. Long Jump")
print("3. High Jump")
print("4. Cricket")

choice = int(input("Select event (1-4): "))

if choice == 1:
    event = "Running"
elif choice == 2:
    event = "Long Jump"
elif choice == 3:
    event = "High Jump"
elif choice == 4:
    event = "Cricket"
else:
    event = "Invalid Event"

if event != "Invalid Event":
    print("\n===== REGISTRATION DETAILS =====")
    print("Student Name :", name)
    print("Roll Number  :", roll_no)
    print("Class        :", class_name)
    print("Age          :", age)
    print("Event        :", event)
    print("Registration Successful!")
else:
    print("Invalid event selection.")