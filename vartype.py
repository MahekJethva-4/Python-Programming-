class Student:
    college = "Marwadi University"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("College:", Student.college)

s1 = Student("Mahek", 21)
s1.display()
