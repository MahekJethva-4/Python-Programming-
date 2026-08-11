#Program to demonstrate pyramid of name by using loop concept:
name = "MAHEK"

for i in range(len(name)):
    print(name[:i+1])
#Pyramid
    
    
rows = 5

for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()
