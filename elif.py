#Asks the user for their numeric grade
grade = float(input("What is your numeric grade number? "))

if grade < 60:
    print("You have a F.")
elif grade < 69:
    print("You have a D.")
elif grade < 79:
    print("You have a C.")
elif grade < 89:
    print("You have a B.")
elif grade < 100:
    print("You have an A.")
else:
    print("You have passed the class.")