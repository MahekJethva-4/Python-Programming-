print("Sports Event Registration")
name=input("Enter participant name:")
age = int(input("Enter sport(Cricket/Football/Tennis):"))
score=int(input("Enter your selection trial score(0-100):"))

print("/n----Result----")
#IF STATEMENT
if sports.lower()=="yes":
            print("Medical fitness check passed.")
#IF-ELSE STATEMENT
if age>=18:
            print("You are eligible by age.")
else:
            print("You are not eligible by age.")
print("Participate details:")
print("Name:",name)
print("Age:",age)

