print("Sports Event Registration")
name = input("Enter participant name:")
age = int(input("Enter your age:"))
sport = input("Enter sport (Cricket/Football/Tennis):")
score = int(input("Enter your selection trial score (0-100):"))
fitness = input("Medical fitness check passed? (yes/no):")

print("\n----Result----")
# IF STATEMENT
if fitness.lower() == "yes":
    print("Medical fitness check passed.")

# IF-ELSE STATEMENT
if age >= 18:
    print("You are eligible by age.")
else:
    print("You are not eligible by age.")

# IF-ELIF-ELSE STATEMENT for sport selection score
if score >= 90:
    print("Selection: Excellent - Selected for the team!")
elif score >= 70:
    print("Selection: Good - Selected for the team.")
elif score >= 50:
    print("Selection: Average - On the waiting list.")
else:
    print("Selection: Not selected.")

print("Participant details:")
print("Name:", name)
print("Age:", age)
print("Sport:", sport)
print("Trial score:", score)
