age = int(input("Enter your age : "))
if age < 13:
    print("Your are a child")
elif 13 <= age <=17 :
    print("You are a teenager")
elif 18 <=age < 60 : 
    print("You are an adult")
else: 
    print("You are a senior citizen")