try:
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    result = num1 / num2

    print("The result is: ", result)

except ValueError:
    print("Invalid input. Please enter a valid number.")

except ZeroDivisionError:
    print("NUM2 can not be zero.")

finally:
    print("Execution completed.")