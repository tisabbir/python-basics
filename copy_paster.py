copy_file = open("text_file2.txt", "r")

content = copy_file.read()

paste_file = open("pasted_file.txt", "w")

paste_file.write(content)

paste_file.close()

