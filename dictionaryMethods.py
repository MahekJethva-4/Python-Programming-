#Program to demonstrate ALL Dictionary Methods in Python

#Creating a dictionary
Student = {'Name': 'Mahek', 'ID': 89, 'Contact': 9876543210}
print("Original Dictionary:", Student)
print()

# 1. clear() - Removes all items from the dictionary
print("========== 1. clear() ==========")
temp = {'a': 1, 'b': 2}
print("Before clear:", temp)
temp.clear()
print("After clear :", temp)
print()

# 2. copy() - Returns a shallow copy of the dictionary
print("========== 2. copy() ==========")
copied = Student.copy()
print("Copied Dictionary:", copied)
print()

# 3. fromkeys() - Creates a new dictionary with keys from sequence
print("========== 3. fromkeys() ==========")
keys = ['Name', 'Age', 'City']
new_dict = dict.fromkeys(keys, 'Unknown')
print("Keys:", keys)
print("New Dictionary:", new_dict)
print()

# 4. get() - Returns value for a key, or default if key not found
print("========== 4. get() ==========")
print("Get 'Name':", Student.get('Name'))
print("Get 'Grade' (not present):", Student.get('Grade'))
print("Get 'Grade' with default:", Student.get('Grade', 'Not Available'))
print()

# 5. items() - Returns list of key-value tuple pairs
print("========== 5. items() ==========")
print("All items:", list(Student.items()))
for key, value in Student.items():
    print(f"  {key} -> {value}")
print()

# 6. keys() - Returns list of all keys
print("========== 6. keys() ==========")
print("All keys:", list(Student.keys()))
print()

# 7. values() - Returns list of all values
print("========== 7. values() ==========")
print("All values:", list(Student.values()))
print()

# 8. pop() - Removes and returns value of specified key
print("========== 8. pop() ==========")
removed = Student.pop('Contact')
print("Removed 'Contact' value:", removed)
print("Dictionary after pop :", Student)
print()

# 9. popitem() - Removes and returns last inserted key-value pair
print("========== 9. popitem() ==========")
last_item = Student.popitem()
print("Removed last item:", last_item)
print("Dictionary after popitem:", Student)
print()

# 10. setdefault() - Returns value of key, or inserts key with default value
print("========== 10. setdefault() ==========")
print("setdefault('Name'):", Student.setdefault('Name'))
print("setdefault('Grade', 'A'):", Student.setdefault('Grade', 'A'))
print("Dictionary after setdefault:", Student)
print()

# 11. update() - Updates dictionary with key-value pairs from another
print("========== 11. update() ==========")
Student.update({'City': 'Surat', 'Grade': 'A+'})
print("Dictionary after update:", Student)
print()

# 12. len() - Returns number of items (built-in function)
print("========== 12. len() ==========")
print("Number of items in dictionary:", len(Student))
print()

# 13. in operator - Checks if a key exists (membership)
print("========== 13. 'in' membership operator ==========")
print("Is 'Name' in dictionary? ", 'Name' in Student)
print("Is 'Contact' in dictionary? ", 'Contact' in Student)
