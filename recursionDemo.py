# ============================================
# RECURSION IN PYTHON
# ============================================
# A function that calls itself is called a recursive function.
# Every recursive function needs:
#   1. A BASE CASE  -> stops the recursion
#   2. A RECURSIVE CALL -> calls itself with a smaller problem

# ---------- Example 1: Factorial ----------
# n! = n * (n-1) * (n-2) * ... * 1
# n! = n * (n-1)!            <- recursive formula
# 0! = 1,  1! = 1            <- base case

def factorial(n):
    if n == 0 or n == 1:      # base case
        return 1
    return n * factorial(n - 1)   # recursive call

print("Factorial of 5 is:", factorial(5))   # Output: 120


# ---------- Example 2: Fibonacci ----------
# Fibonacci series: 0, 1, 1, 2, 3, 5, 8, 13, ...
# fib(n) = fib(n-1) + fib(n-2)   <- recursive formula
# fib(0) = 0, fib(1) = 1         <- base case

def fibonacci(n):
    if n <= 1:                    # base case
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)   # recursive call

print("Fibonacci of 6 is:", fibonacci(6))   # Output: 8


# ---------- Example 3: Sum of first n natural numbers ----------
# sum(n) = n + sum(n-1)
# sum(0) = 0

def natural_sum(n):
    if n == 0:                    # base case
        return 0
    return n + natural_sum(n - 1) # recursive call

print("Sum of first 10 natural numbers:", natural_sum(10))  # Output: 55


# ---------- Example 4: Power of a number ----------
# pow(x, n) = x * pow(x, n-1)
# pow(x, 0) = 1

def power(x, n):
    if n == 0:                    # base case
        return 1
    return x * power(x, n - 1)    # recursive call

print("2 raised to power 5:", power(2, 5))   # Output: 32


# ---------- Example 5: Print numbers from 1 to n ----------
def print_1_to_n(n):
    if n == 0:                    # base case
        return
    print_1_to_n(n - 1)           # recursive call
    print(n, end=" ")

print("Numbers from 1 to 5:")
print_1_to_n(5)
print()


# ============================================
# HOW RECURSION WORKS (STACK)
# ============================================
# When factorial(5) is called:
#   factorial(5) -> 5 * factorial(4)
#   factorial(4) -> 4 * factorial(3)
#   factorial(3) -> 3 * factorial(2)
#   factorial(2) -> 2 * factorial(1)
#   factorial(1) -> 1         (base case reached)
# Then it unwinds back:
#   factorial(2) = 2 * 1 = 2
#   factorial(3) = 3 * 2 = 6
#   factorial(4) = 4 * 6 = 24
#   factorial(5) = 5 * 24 = 120
