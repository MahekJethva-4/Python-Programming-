#Program to create pyramid program using looping control structure
#Pyramid pattern 
rows = 5

for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()
rows = int(input("Enter number of rows: "))

for i in range(1, rows + 1):
    print(" " * (rows - i), end="")
    print(str(i) * (2 * i - 1))
    
    #Pyramid center aligned
    rows = int(input("Enter number of rows: "))

for i in range(1, rows + 1):
    print(" " * (rows - i), end="")
    print(str(i) * (2 * i - 1))