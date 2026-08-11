#Program to demonstrate ALL Python Operators
#Arithmetic, Relational, Logical, Assignment, Bitwise, Membership, Identity

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("\n========== 1. ARITHMETIC OPERATORS ==========")
print("Addition        (a + b)  =", a + b)
print("Subtraction     (a - b)  =", a - b)
print("Multiplication  (a * b)  =", a * b)
print("Division        (a / b)  =", a / b)
print("Floor Division  (a // b) =", a // b)
print("Modulus         (a % b)  =", a % b)
print("Exponent        (a ** b) =", a ** b)

print("\n========== 2. RELATIONAL / COMPARISON OPERATORS ==========")
print("Equal to            (a == b) =", a == b)
print("Not equal to        (a != b) =", a != b)
print("Greater than        (a > b)  =", a > b)
print("Less than           (a < b)  =", a < b)
print("Greater or equal    (a >= b) =", a >= b)
print("Less or equal       (a <= b) =", a <= b)

print("\n========== 3. LOGICAL OPERATORS ==========")
x = True
y = False
print("True and False =", x and y)
print("True or False  =", x or y)
print("not True       =", not x)

print("\n========== 4. ASSIGNMENT OPERATORS ==========")
c = a                 # Assign
print("c = a                 -> c =", c)
c += b                # Add and assign
print("c += b                -> c =", c)
c -= b                # Subtract and assign
print("c -= b                -> c =", c)
c *= b                # Multiply and assign
print("c *= b                -> c =", c)
c /= b                # Divide and assign
print("c /= b                -> c =", c)
c //= b               # Floor divide and assign
print("c //= b               -> c =", c)
c %= b                # Modulus and assign
print("c %= b                -> c =", c)
c = a
c **= b               # Exponent and assign
print("c **= b               -> c =", c)

print("\n========== 5. BITWISE OPERATORS ==========")
print("Bitwise AND     (a & b)  =", a & b)
print("Bitwise OR      (a | b)  =", a | b)
print("Bitwise XOR     (a ^ b)  =", a ^ b)
print("Bitwise NOT     (~a)     =", ~a)
print("Left Shift      (a << 2)=", a << 2)
print("Right Shift     (a >> 2)=", a >> 2)

print("\n========== 6. MEMBERSHIP OPERATORS ==========")
fruits = ["apple", "banana", "cherry"]
print("'apple' in fruits     =", "apple" in fruits)
print("'mango' in fruits     =", "mango" in fruits)
print("'mango' not in fruits =", "mango" not in fruits)

print("\n========== 7. IDENTITY OPERATORS ==========")
p = a
print("p is a      =", p is a)
print("p is not b  =", p is not b)
