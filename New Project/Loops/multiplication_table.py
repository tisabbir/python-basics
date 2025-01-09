# Multiplication Table

number = int(input("Enter the number you want to have a multiplication table : "))

for i in range(1,11):
    print(f"{number} * {i} = {number * i}")