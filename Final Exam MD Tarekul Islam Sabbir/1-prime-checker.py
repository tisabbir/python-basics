def check_prime(value):
    if value < 2:
        return False
    for i in range(2, int(value ** 0.5) + 1):
        if value % i == 0:
            return False
    return True

for num in range(100, 401):
    if check_prime(num):
        print(num, end=", ")