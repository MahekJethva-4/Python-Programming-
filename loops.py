#Loops
# Loops are used to execute a block of code repeatedly

# -------------------------------------------
# 1. FOR LOOP
# -------------------------------------------

# For loop with range(stop)
print("--- For Loop with range(stop) ---")
for i in range(5):
    print("Iteration:", i)

# For loop with range(start, stop)
print("\n--- For Loop with range(start, stop) ---")
for i in range(2, 8):
    print("Value:", i)

# For loop with range(start, stop, step)
print("\n--- For Loop with range(start, stop, step) ---")
for i in range(1, 11, 2):
    print("Odd Number:", i)

# For loop with list
print("\n--- For Loop with List ---")
fruits = ["Apple", "Banana", "Cherry", "Mango"]
for fruit in fruits:
    print("Fruit:", fruit)

# For loop with string
print("\n--- For Loop with String ---")
word = "Python"
for char in word:
    print("Character:", char)

# For loop with tuple
print("\n--- For Loop with Tuple ---")
colors = ("Red", "Green", "Blue")
for color in colors:
    print("Color:", color)

# For loop with dictionary
print("\n--- For Loop with Dictionary ---")
student = {'Name':'Mahek', 'ID':89, 'Grade':'A'}
print("Keys:")
for key in student:
    print("-", key)

print("\nValues:")
for value in student.values():
    print("-", value)

print("\nKey-Value Pairs:")
for key, value in student.items():
    print(f"{key}: {value}")

# For loop with enumerate (getting index)
print("\n--- For Loop with enumerate ---")
subjects = ["Maths", "Science", "English"]
for index, subject in enumerate(subjects):
    print(f"Subject {index + 1}: {subject}")

# For loop with break statement
print("\n--- Break Statement ---")
for i in range(1, 11):
    if i == 6:
        print("Breaking loop at", i)
        break
    print("Number:", i)

# For loop with continue statement
print("\n--- Continue Statement ---")
for i in range(1, 8):
    if i == 4:
        print("Skipping", i)
        continue
    print("Number:", i)

# For loop with else clause
print("\n--- For Loop with else ---")
for i in range(1, 4):
    print("Value:", i)
else:
    print("Loop completed normally (no break)")

# For loop with else that does NOT execute (break occurred)
print("\n--- For Loop with else (break occurred) ---")
for i in range(1, 6):
    if i == 3:
        print("Break at", i)
        break
    print("Value:", i)
else:
    print("This will NOT print because break occurred")

# Nested for loop
print("\n--- Nested For Loop ---")
print("Multiplication Table (1 to 3):")
for i in range(1, 4):
    for j in range(1, 4):
        print(f"{i} x {j} = {i*j}")
    print("---")

# -------------------------------------------
# 2. WHILE LOOP
# -------------------------------------------

# Basic while loop
print("\n--- Basic While Loop ---")
count = 1
while count <= 5:
    print("Count:", count)
    count += 1

# While loop with break
print("\n--- While Loop with Break ---")
num = 1
while num <= 10:
    if num == 7:
        print("Breaking at", num)
        break
    print("Num:", num)
    num += 1

# While loop with continue
print("\n--- While Loop with Continue ---")
num = 0
while num < 6:
    num += 1
    if num == 3:
        print("Skipping", num)
        continue
    print("Num:", num)

# While loop with else
print("\n--- While Loop with else ---")
num = 1
while num <= 3:
    print("Num:", num)
    num += 1
else:
    print("While loop completed (no break)")

# While loop with else (break occurred)
print("\n--- While Loop with else (break occurred) ---")
num = 1
while num <= 5:
    if num == 4:
        print("Breaking at", num)
        break
    print("Num:", num)
    num += 1
else:
    print("This will NOT print because break occurred")

# Infinite loop with break condition
print("\n--- Controlled Infinite Loop ---")
total = 0
while True:
    total += 1
    print("Total:", total)
    if total >= 3:
        print("Reached limit, breaking")
        break

# -------------------------------------------
# 3. PASS STATEMENT
# -------------------------------------------

print("\n--- Pass Statement ---")
for i in range(3):
    if i == 1:
        pass  # Does nothing, placeholder
    print("Value:", i)

# Using pass in an empty loop (placeholder for future code)
print("\nUsing pass as placeholder:")
for i in range(3):
    pass  # TODO: Add logic later
print("Loop with pass executed without error")

# -------------------------------------------
# 4. PRACTICAL EXAMPLES
# -------------------------------------------

# Sum of numbers using for loop
print("\n--- Sum of Numbers ---")
numbers = [10, 20, 30, 40, 50]
sum_total = 0
for num in numbers:
    sum_total += num
print("Sum of", numbers, "=", sum_total)

# Finding factorial using for loop
print("\n--- Factorial ---")
n = 5
factorial = 1
for i in range(1, n + 1):
    factorial *= i
print(f"Factorial of {n} = {factorial}")

# Printing pattern using nested loops
print("\n--- Star Pattern ---")
rows = 5
for i in range(1, rows + 1):
    for j in range(i):
        print("*", end=" ")
    print()

# Reverse pattern
print("\n--- Reverse Star Pattern ---")
for i in range(rows, 0, -1):
    for j in range(i):
        print("*", end=" ")
    print()

# Fibonacci series using while loop
print("\n--- Fibonacci Series ---")
a, b = 0, 1
terms = 8
count = 0
print("Fibonacci Series (", terms, "terms):")
while count < terms:
    print(a, end=" ")
    a, b = b, a + b
    count += 1
print()

# Finding prime numbers using loops
print("\n--- Prime Numbers (1 to 20) ---")
for num in range(2, 21):
    is_prime = True
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print(num, "is prime")

# List comprehension (compact for loop)
print("\n--- List Comprehension ---")
squares = [x ** 2 for x in range(1, 8)]
print("Squares:", squares)

even_numbers = [x for x in range(1, 11) if x % 2 == 0]
print("Even Numbers:", even_numbers)

# Using zip to loop through multiple lists
print("\n--- Looping with zip() ---")
names = ["Rahul", "Priya", "Amit"]
marks = [85, 92, 78]
for name, mark in zip(names, marks):
    print(f"{name} scored {mark} marks")

# -------------------------------------------
# 5. LOOPS SUMMARY
# -------------------------------------------
print("\n--- Loops Summary ---")
print("1. for loop - iterates over a sequence (list, tuple, string, range)")
print("2. while loop - repeats while a condition is True")
print("3. break - exits the loop immediately")
print("4. continue - skips current iteration, moves to next")
print("5. pass - does nothing, used as placeholder")
print("6. else with loop - executes if loop finishes normally (no break)")
print("7. Nested loops - loop inside another loop")
print("8. enumerate() - get index and value in for loop")
print("9. zip() - iterate multiple sequences in parallel")
print("10. List comprehension - compact way to create lists")
