texts = input("Enter your texts: ")
# print(texts)
file1 = open("users_file", "w")
file1.write(texts)

file1.close()