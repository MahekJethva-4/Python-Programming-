#Math Formulas on Loop
# This file demonstrates common math formulas implemented using loops in Python

# -------------------------------------------
# 1. FACTORIAL (n!)
# Formula: n! = 1 x 2 x 3 x ... x n
# -------------------------------------------
print("--- Factorial (n!) ---")
n = 5
factorial = 1
for i in range(1, n + 1):
    factorial *= i
print(f"{n}! = {factorial}")

# -------------------------------------------
# 2. SUM OF FIRST N NATURAL NUMBERS
# Formula: Sum = n(n+1)/2
# -------------------------------------------
print("\n--- Sum of First N Natural Numbers ---")
n = 10
sum_n = 0
for i in range(1, n + 1):
    sum_n += i
print(f"Sum of 1 to {n} = {sum_n}")

# -------------------------------------------
# 3. SUM OF SQUARES
# Formula: Sum of squares = n(n+1)(2n+1)/6
# -------------------------------------------
print("\n--- Sum of Squares ---")
n = 5
sum_squares = 0
for i in range(1, n + 1):
    sum_squares += i * i
print(f"Sum of squares 1 to {n} = {sum_squares}")

# -------------------------------------------
# 4. SUM OF CUBES
# Formula: Sum of cubes = [n(n+1)/2]^2
# -------------------------------------------
print("\n--- Sum of Cubes ---")
n = 4
sum_cubes = 0
for i in range(1, n + 1):
    sum_cubes += i * i * i
print("Sum of cubes 1 to {n} = {sum_cubes}")

# -------------------------------------------
# 5. AVERAGE OF A LIST
# Formula: Average = Sum / Count
# -------------------------------------------
print("\n--- Average of Numbers ---")
numbers = [10, 20, 30, 40, 50]
total = 0
for num in numbers:
    total += num
average = total / len(numbers)
print(f"Numbers: {numbers}")
print(f"Average = {average}")

# -------------------------------------------
# 6. POWER (x^y) using loop
# Formula: x^y = x multiplied y times
# -------------------------------------------
print("\n--- Power using loop (x^y) ---")
x = 3
y = 4
result = 1
for i in range(y):
    result *= x
print(f"{x}^{y} = {result}")

# -------------------------------------------
# 7. FIBONACCI SERIES
# Formula: F(n) = F(n-1) + F(n-2), F(0)=0, F(1)=1
# -------------------------------------------
print("\n--- Fibonacci Series ---")
terms = 10
a, b = 0, 1
print("Fibonacci Series:", end=" ")
for i in range(terms):
    print(a, end=" ")
    a, b = b, a + b
print()

# -------------------------------------------
# 8. MULTIPLICATION TABLE
# Formula: number x i
# -------------------------------------------
print("\n--- Multiplication Table ---")
num = 7
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")

# -------------------------------------------
# 9. SQUARE AND CUBE TABLE
# Formula: square = i^2, cube = i^3
# -------------------------------------------
print("\n--- Square and Cube Table ---")
for i in range(1, 6):
    print(f"{i}  Square={i*i}  Cube={i*i*i}")

# -------------------------------------------
# 10. PERCENTAGE
# Formula: percentage = (obtained / total) x 100
# -------------------------------------------
print("\n--- Percentage of Marks ---")
marks = [85, 90, 78, 92, 88]
total_obtained = 0
for mark in marks:
    total_obtained += mark
max_total = len(marks) * 100
percentage = (total_obtained / max_total) * 100
print(f"Marks: {marks}")
print(f"Total Obtained = {total_obtained} / {max_total}")
print(f"Percentage = {percentage:.2f}%")

# -------------------------------------------
# 11. SIMPLE INTEREST using loop
# Formula: SI = (P x R x T) / 100
# -------------------------------------------
print("\n--- Simple Interest ---")
principal = 1000
rate = 5
for time in range(1, 6):  # interest for 1 to 5 years
    si = (principal * rate * time) / 100
    print(f"Year {time}: Simple Interest = {si}")

# -------------------------------------------
# 12. PRIME NUMBERS
# Formula: num is prime if divisible only by 1 and itself
# -------------------------------------------
print("\n--- Prime Numbers (1 to 30) ---")
for num in range(2, 31):
    is_prime = True
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print(num, end=" ")
print()

# -------------------------------------------
# 13. GCD (Greatest Common Divisor)
# Formula: Euclid's algorithm
# -------------------------------------------
print("\n--- GCD of two numbers ---")
a = 36
b = 24
while b:
    a, b = b, a % b
print(f"GCD of 36 and 24 = {a}")

# -------------------------------------------
# 14. SUM OF DIGITS
# Formula: sum of each digit of a number
# -------------------------------------------
print("\n--- Sum of Digits ---")
num = 12345
sum_digits = 0
while num > 0:
    sum_digits += num % 10
    num //= 10
print(f"Sum of digits of 12345 = {sum_digits}")

# -------------------------------------------
# 15. EVEN/ODD NUMBERS count
# Formula: num % 2 == 0
# -------------------------------------------
print("\n--- Even and Odd Numbers (1 to 20) ---")
evens = []
odds = []
for i in range(1, 21):
    if i % 2 == 0:
        evens.append(i)
    else:
        odds.append(i)
print("Even Numbers:", evens)
print("Odd Numbers:", odds)
