file_path = "C:\\Projects\\python-basic\\New Project\\file-handling\\file.txt"

with open(file_path, "r", encoding="utf-8") as file:
    content = file.read()

print(content)