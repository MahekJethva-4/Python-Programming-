name = "MAHEK"

for i in range(len(name)):
    print(" " * (len(name) - i - 1), end="")
    for j in range(i + 1):
        print(name[j], end=" ")
    print()
