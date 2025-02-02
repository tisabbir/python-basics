email = input("Enter your email: ")
Name = input("Enter your Name: ")
Fathers_Name = input("Enter your Fathers_Name: ")
Mothers_Name = input("Enter your Mothers_Name: ")
Institute_Name = input("Enter your Institute_Name: ")

user_info_list = [email, Name, Fathers_Name, Mothers_Name, Institute_Name]

users_info_file = open("user_info_file.txt", "a")

for info in user_info_list:
    users_info_file.write(info + "\n ")


created_file = open("user_info_file.txt", "r")
contents = created_file.read()
print("Your Info is here: ", contents )
users_info_file.close()