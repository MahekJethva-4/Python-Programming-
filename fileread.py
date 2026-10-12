f = open("student1.txt" , "w")
f.write("Python Programming")
f.close( )

f = open("student1.txt" , "r")

print("Current position:" , f.tell())

f.seek(7)
print("Position after seek:", f.tell())

print("Remaining content:", f. read())

f.close()
