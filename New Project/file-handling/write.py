file_path = r"C:\Projects\python-basic\New Project\file-handling\file.txt"

with open(file_path, "w", encoding="utf-8") as file:
    file.write("This is a new line.\n")
    file.write("Overwrites existing content.\n")

print("File written successfully.")
