f = open("C:\\Projects\\python-basic\\New Project\\file-handling\\file.txt", "r")
content = f.read()
counting_word = "new"

x = content.count(counting_word)
print(content)
print(counting_word, "is here for ", x, "times")
f.close()
