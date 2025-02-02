name = input("Enter your name: ")
dept = input("Enter your dept: ")
roll = input("Enter your roll: ")
batch = input("Enter your batch: ")

file_name = roll + ".txt"

created_file = open(file_name, "a")

student_name = "Student Name : " + name + "\n "
student_dept = "Student Dept : " + dept + "\n "
student_roll = "Student Roll : " + roll + "\n "
student_batch = "Student Batch : " + batch + "\n "

created_file.write(student_name)
created_file.write(student_dept)
created_file.write(student_roll)
created_file.write(student_batch)

created_file.close()