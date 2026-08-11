#Program to create a math calculator that supports infinite numbers (multiple operands)
#This calculator supports addition, subtraction, multiplication, division, floor division, modulus and exponent

def get_numbers():
    """Get an infinite list of numbers from the user."""
    numbers = []
    print("Enter numbers (type 'done' and press Enter to finish):")
    while True:
        val = input("> ")
        if val.lower() == 'done':
            break
        try:
            numbers.append(float(val))
        except ValueError:
            print("Invalid input! Please enter a numeric value or 'done'.")
    return numbers

def calculator():
    print("\n===== MATH CALCULATOR (Infinite Numbers) =====")
    print("Operations available:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Floor Division (//)")
    print("6. Modulus (%)")
    print("7. Exponent (**)")
    print("8. Exit")

    while True:
        print("\n-----------------------------")
        choice = input("Enter your choice (1-8): ")

        if choice == '8':
            print("Thank you for using the calculator. Goodbye!")
            break

        if choice in ['1', '2', '3', '4', '5', '6', '7']:
            numbers = get_numbers()

            if len(numbers) < 2:
                print("Please enter at least two numbers.")
                continue

            result = numbers[0]
            expression = str(numbers[0])
            error = False

            for n in numbers[1:]:
                if choice == '1':
                    result += n
                    expression += f" + {n}"
                elif choice == '2':
                    result -= n
                    expression += f" - {n}"
                elif choice == '3':
                    result *= n
                    expression += f" * {n}"
                elif choice == '4':
                    if n == 0:
                        print("Error! Division by zero is not allowed.")
                        error = True
                        break
                    result /= n
                    expression += f" / {n}"
                elif choice == '5':
                    if n == 0:
                        print("Error! Division by zero is not allowed.")
                        error = True
                        break
                    result //= n
                    expression += f" // {n}"
                elif choice == '6':
                    if n == 0:
                        print("Error! Division by zero is not allowed.")
                        error = True
                        break
                    result %= n
                    expression += f" % {n}"
                elif choice == '7':
                    result = result ** n
                    expression += f" ** {n}"

            if not error:
                print(f"{expression} = {result}")
        else:
            print("Invalid choice! Please enter a number between 1 and 8.")

# Run the calculator
calculator()
