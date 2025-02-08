for i in range(3):  
    try:
        num1 = int(input("Enter the first number: "))
        num2 = int(input("Enter the second number: "))

        if num1 < 0 or num2 < 0: 
            raise ValueError("Negative numbers are not allowed!")

        result = num1 / num2  
        print("The result is:", result, "\n")
        break 
    
    except ValueError as e:
        print(f"Invalid input: {e}. Please enter a valid positive number.")

    except ZeroDivisionError:
        print("NUM2 cannot be zero. Please enter a non-zero number.")

print("Execution completed.")