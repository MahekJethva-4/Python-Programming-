# Program on Functions and Arguments in Python

print("========== 1. TYPES OF FUNCTIONS ==========")

# 1. Function without arguments and without return value
def greet():
    print("Hello, Welcome to Python!")

# 2. Function with arguments and without return value
def add(a, b):
    print("Sum =", a + b)

# 3. Function without arguments and with return value
def pi():
    return 3.14

# 4. Function with arguments and with return value
def multiply(x, y):
    return x * y


greet()
add(10, 20)
print("Pi =", pi())
print("Product =", multiply(5, 6))


print("\n========== 2. TYPES OF ARGUMENTS ==========")

# 1. Required / Positional Arguments
def details(name, age):
    print("Name:", name, "| Age:", age)

print("-- Required Arguments --")
details("Rahul", 20)

# 2. Keyword Arguments
print("-- Keyword Arguments --")
details(age=21, name="Priya")

# 3. Default Arguments
def student(name, course="B.Tech CSE"):
    print("Name:", name, "| Course:", course)

print("-- Default Arguments --")
student("MahekJ")
student("Rohit", "BCA")

# 4. Variable-length Arguments (*args) - tuple
def total(*numbers):
    s = 0
    for n in numbers:
        s += n
    print("Sum of", numbers, "=", s)

print("-- Variable-length Arguments (*args) --")
total(1, 2, 3)
total(10, 20, 30, 40, 50)

# 5. Keyword Variable-length Arguments (**kwargs) - dictionary
def info(**data):
    for key, value in data.items():
        print(key, "=", value)
        
print("-- Keyword Variable-length Arguments (**kwargs) --")
info(name="ABC", age=20, city="Rajkot")


print("\n========== 3. RECURSION (Function calling itself) ==========")
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)

print("Factorial of 5 =", factorial(5))
