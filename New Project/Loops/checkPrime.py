number = int(input("Enter a number : "))
if number <=1 :
    print("The number is not prime")
else:
    for i in range(2,number):
        if number%2 == 0:
            print("Not prime")
            break
        else:
            print("Prime")
            break