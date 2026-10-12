#File  Pointer Operations

f = open("student1.txt", "w")
f.write("Python Programming")
f.close()

f = open("student1.txt", "r")

print("Current position:", f.tell())

f.seek(7)
print("Remaining content:", f.read())
f.close()
