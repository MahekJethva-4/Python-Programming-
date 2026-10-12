#Program to read and write data into a file using different file modes
f = open("student.txt", "w")
f.write("Welcome to Python\n")
f.close()

#Append mode
f = open("student1.txt", "a")
f.write("Learning file handling\n")
f.close()

#Read mode
f = open("student1.txt", "r")
print(f.read())
f.close()
