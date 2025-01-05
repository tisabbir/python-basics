# Grade finder 
a = float(input("Enter the mark of the subject : "))
if a > 100 : 
    print("Invalid Marks. Marks cannot be more than 100")
elif a >= 80 : 
    print("Congratulations! You got an A+")
elif a >= 75 : 
    print("Your grade is A")
elif a >= 70 :
    print("Your grade is A-")
elif a>= 65 :
    print("Your grade is B+")
elif a>=60 :
    print("Your grade is B")
elif a>=55 : 
    print("Your grade is B-")
elif a>=50 :
    print("Your grade is C")
elif a>=40 :
    print("Your grade is D")
else : print("You are failed. Try again later.")


