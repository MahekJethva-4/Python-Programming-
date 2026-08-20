import re

# Input student details
name = input("Enter student name: ")
roll_no = input("Enter roll number: ")
email = input("Enter email: ")
# Regular expression patterns
name_pattern = r'^[A-Za-z ]+$'
roll_pattern = r'^IV\d{4}$'
email_pattern = r'^[\w.-]+@[\w.-]+\.\w+$'
#validation
if re.match(name_pattern, name):
    print("Valid student name")
else:
    print("Invalid student name")

if re.match(roll_pattern, roll_no):
    print("Valid industrial visit roll number")
else:
    print("Invalid roll number")

if re.match(email_pattern, email):
    print("Valid email address")
else:
    print("Invalid email address")

if re.match(phone_pattern, phone):
    print("Valid phone number")
else:
    print("Invalid phone number")
    
    
    
    
    
    
    
    
    