try:
    file = open("myfile.txt", "r")  
    content = file.read()
    print(content)
    file.close()

except FileNotFoundError:
    print(" Error: The file does not exist. Please check the file name.")