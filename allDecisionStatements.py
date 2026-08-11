# ============================================================
# ALL DECISION CONTROL STATEMENTS IN PYTHON
# ============================================================
# Decision control statements are used to execute a block of
# code only when a condition is True (or False).
#
# Python provides these decision-making statements:
#   1. if statement                (simple)
#   2. if-else statement
#   3. if-elif-else ladder
#   4. Nested if statements
#   5. Conditional expression (ternary operator)

print("=" * 50)
print("1. SIMPLE IF STATEMENT")
print("=" * 50)
# Executes a block only when the condition is True.
num = int(input("Enter a number: "))
if num > 0:
    print(f"{num} is a positive number.")
# If the condition is False, nothing happens.


print()
print("=" * 50)
print("2. IF-ELSE STATEMENT")
print("=" * 50)
# Executes one block when the condition is True,
# and another block when it is False.
num = int(input("Enter a number: "))
if num % 2 == 0:
    print(f"{num} is even.")
else:
    print(f"{num} is odd.")


print()
print("=" * 50)
print("3. IF-ELIF-ELSE LADDER")
print("=" * 50)
# Used when there are multiple conditions to check.
# The first True condition's block runs, the rest are skipped.
marks = int(input("Enter your marks (0-100): "))
if marks >= 90:
    grade = "A"
elif marks >= 70:
    grade = "B"
elif marks >= 50:
    grade = "C"
elif marks >= 35:
    grade = "D"
else:
    grade = "F"
print("Your grade is: {grade}")


print()
print("=" * 50)
print("4. NESTED IF STATEMENT")
print("=" * 50)
# An if statement inside another if statement.
age = int(input("Enter your age: "))
if age >= 18:
    has_id = input("Do you have a valid ID? (yes/no): ").lower()
    if has_id == "yes":
        print("You are allowed to vote.")
    else:
        print("You are old enough, but you need a valid ID.")
else:
    print("You are not old enough to vote.")


print()
print("=" * 50)
print("5. CONDITIONAL EXPRESSION (TERNARY OPERATOR)")
print("=" * 50)
# A short, one-line if-else.
# Syntax:  value_if_true if condition else value_if_false
num = int(input("Enter a number: "))
result = "Positive" if num >= 0 else "Negative"
print(f"The number is {result}.")


print()
print("=" * 50)
print("6. COMBINED EXAMPLE - DAY OF THE WEEK")
print("=" * 50)
# A practical program that uses multiple decision statements.
day = int(input("Enter a number (1-7) for the day: "))
if day == 1:
    print("Monday - Start of the work week!")
elif day == 2:
    print("Tuesday")
elif day == 3:
    print("Wednesday")
elif day == 4:
    print("Thursday")
elif day == 5:
    print("Friday - Almost weekend!")
elif day == 6:
    print("Saturday - Weekend!")
elif day == 7:
    print("Sunday - Rest day!")
else:
    print("Invalid input! Please enter a number between 1 and 7.")

