# Program on Types of Variables in Python
# Local, Global, Instance, and Class variables

# ================= 1. GLOBAL VARIABLE =================
# Declared outside all functions/classes, accessible everywhere
College = "Marwadi University"

# ================= 2. CLASS VARIABLE =================
# Declared inside a class but outside any method, shared by all objects
class Student:
    # Class variable (shared by all instances)
    course = "B.Tech CSE"

    def __init__(self, name):
        # Instance variable (belongs to each object)
        self.name = name

    def show(self):
        # Local variable (declared inside a method)
        message = "Welcome to College"
        print("Local Variable  ->", message)
        print("Instance Variable ->", self.name)
        print("Class Variable  ->", Student.course)
        print("Global Variable ->", College)


# ================= 4. LOCAL VARIABLE =================
def student():
    # Local variable (only accessible inside this function)
    name = "MahekJ"
    print("Student Name:", name)
    print("Institute:", College)


print("========== GLOBAL VARIABLE (outside) ==========")
print("College:", College)

print("\n========== LOCAL VARIABLE (inside function) ==========")
student()

print("\n========== CLASS & INSTANCE VARIABLE ==========")
s1 = Student("Rahul")
s2 = Student("Priya")
s1.show()

print("\nClass variable is shared by all objects:")
print("s1.course =", s1.course)
print("s2.course =", s2.course)
