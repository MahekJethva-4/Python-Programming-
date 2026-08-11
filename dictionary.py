#Dictionary
# A dictionary stores data in key-value pairs

# Creating a dictionary
Student = {'Name':'Mahek', 'ID':89, 'Contact':9876543210}
print("Original Dictionary:", Student)

# Accessing values using keys
print("\nAccessing Values")
print("Student Name:", Student['Name'])
print("Student ID:", Student['ID'])

# Adding new key-value pairs
print("\nAdding New Data")
Student['Grade'] = 'A'
Student['City'] = 'Surat'
print("After Adding:", Student)

# Updating existing values
print("\nUpdating Values")
Student['Grade'] = 'A+'
print("After Update:", Student)

# Removing items
print("\nRemoving Items")
Student.pop('City')
print("After Removing City:", Student)

# Dictionary Methods
print("\nDictionary Methods")
print("All Keys:", Student.keys())
print("All Values:", Student.values())
print("All Items:", Student.items())

# Looping through dictionary
print("\nLooping Through Dictionary")
for key, value in Student.items():
    print(key, ":", value)


# Nested Dictionary
print("\nNested Dictionary")
Classroom = {
    'Student1': {'Name':'Rahul', 'Marks':85},
    'Student2': {'Name':'Priya', 'Marks':92},
    'Student3': {'Name':'Amit', 'Marks':78}
}
print("Classroom Data:", Classroom)

# Accessing nested dictionary values
print("\nAccessing Nested Values")
print("Student2 Name:", Classroom['Student2']['Name'])
print("Student3 Marks:", Classroom['Student3']['Marks'])
print("Student4 Marks:", Classroom['Student4']['Marks'])
# Length of dictionary
print("\nDictionary Length")
print("Number of Students:", len(Classroom))

