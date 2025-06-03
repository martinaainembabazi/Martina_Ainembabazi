age = 18
grade = 85

if age >= 18: 
    if grade >= 80:  
        print("You are eligible for the scholarship!")
        if grade >= 90:  
            print("You are eligible for the scholarship with honors!")
        else:
            print("You are eligible for the scholarship without honors.")
    else:
        print("Your grade is too low for the scholarship.")
else:
    print("You are not old enough to apply for the scholarship.")
