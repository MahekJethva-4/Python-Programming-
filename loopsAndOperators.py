#Program to demonstrate how Loops and Operators work together
#Combining for loops, while loops, and nested loops with all Python operators

#USING OPERATORS INSIDE A FOR LOOP
print("========== 1. FOR LOOP + ARITHMETIC OPERATORS ==========")
print("Table of 5 using multiplication operator:")
for i in range(1, 11):
    result = 5 * i          # Multiplication operator
    print(f"5 x {i} = {result}")

#USING OPERATORS INSIDE A WHILE LOOP
print("\n========== 2. WHILE LOOP + ARITHMETIC OPERATORS ==========")
n = 1
total = 0
while n <= 5:
    total += n              # Addition & assignment operator
    print(f"Adding {n} -> running total = {total}")
    n += 1                  # Increment operator
print("Sum of 1 to 5 =", total)

#USING RELATIONAL OPERATORS TO CONTROL LOOPS
print("\n========== 3. RELATIONAL OPERATORS IN LOOP CONDITION ==========")
for i in range(1, 8):
    if i > 5:               # Greater than operator
        print(f"{i} > 5 -> break the loop")
        break
    print(f"{i} <= 5 -> continue")

#USING LOGICAL OPERATORS IN LOOP CONDITIONS
print("\n========== 4. LOGICAL OPERATORS IN LOOP CONDITION ==========")
for i in range(1, 8):
    if i % 2 == 0 and i > 2:   # Modulus + Logical AND
        print(f"{i} is even AND greater than 2")
    if i % 2 == 1 or i == 2:   # Logical OR
        print(f"{i} is odd OR equals 2")

#USING COMPARISON OPERATORS WITH LOOPS ON LISTS (membership)
print("\n========== 5. MEMBERSHIP OPERATOR + FOR LOOP ==========")
marks = [85, 90, 78, 92, 88]
for m in marks:               # 'in' membership operator
    if m >= 90:               # Relational operator
        print(f"Score {m} -> Grade A")
    elif m >= 80:
        print(f"Score {m} -> Grade B")
    else:
        print(f"Score {m} -> Grade C")

#NESTED LOOPS WITH OPERATORS (pattern printing)
print("\n========== 6. NESTED LOOPS + OPERATORS ==========")
for i in range(1, 6):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()                  # new line

#SUM OF EVEN AND ODD NUMBERS USING LOOP + MODULUS OPERATOR
print("\n========== 7. LOOP + MODULUS (Even/Odd Sum) ==========")
even_sum = 0
odd_sum = 0
for i in range(1, 11):
    if i % 2 == 0:           # Modulus operator to check even
        even_sum += i
    else:
        odd_sum += i
print(f"Sum of even numbers (1-10) = {even_sum}")
print(f"Sum of odd numbers (1-10)  = {odd_sum}")

#FACTORIAL USING WHILE LOOP + MULTIPLICATION OPERATOR
print("\n========== 8. FACTORIAL USING LOOP ==========")
num = int(input("Enter a number for factorial: "))
fact = 1
i = 1
while i <= num:
    fact *= i                # Multiplication operator
    i += 1
print(f"Factorial of {num} = {fact}")
