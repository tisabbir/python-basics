def get_positive_number():
    num = float(input("Enter a positive number: "))
    if num < 0:
        raise ValueError("Negative numbers are not allowed.")
    return num

try:
    num = get_positive_number()
    print(f"You entered: {num}")
except ValueError as e:
    print(e)

