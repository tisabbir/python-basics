students = ['karim', 'rahim', 'jalil', 'khalil']
print("Original Students", students)

students.append("Majed")
print("After appending", students)

students.insert(3,"Mango")
print("After inserting", students)

students.remove("rahim")
print("After removing", students)

print("First Student", students[0])

print("Length of the list", len(students))

for std in students:
    print(std)