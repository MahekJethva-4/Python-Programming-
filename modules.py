class Student:
    def __init__(self, roll_no, name, marks):
        self.roll_no = roll_no
        self.name = name
        self.marks = marks

    def total(self):
        return sum(self.marks)

    def percentage(self):
        return self.total() / len(self.marks)

    def grade(self):
        percentage = self.percentage()

        if percentage >= 90:
            return "A+"
        elif percentage >= 80:
            return "A"
        elif percentage >= 70:
            return "B"
        elif percentage >= 60:
            return "C"
        elif percentage >= 50:
            return "D"
        else:
            return "F"

    def display(self):
        print("\nRoll Number :", self.roll_no)
        print("Name        :", self.name)
        print("Marks       :", self.marks)
        print("Division     :", self.division)
        print("Multiplication :", self.multiplication)
        print("Total       :", self.total())
        print("Percentage  :", round(self.percentage(), 2), "%")
        print("Grade       :", self.grade())