def check_prime(value):
    if value < 2:
        return False
    for i in range(2,value):
        if(value % i == 0):
            return False
    return True

for num in range(100, 401):
    if check_prime(num):
        print(num)