#Asks for your age
age = float(input("What is your age? "))

#Determines if the user is old enough to drive
number = age
if number >= 18:
    print("You are eligible to drive.")
else:
    print("You are not eligible to drive.")

#Determines if the user is old enough to vote
number = age
if number >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")

#Determines if the user is old enough to buy alcohol
number = age
if number >= 21:
    print("You are eligible to buy alcohol.")
else:
    print("You are not eligible to buy alcohol.")

#Determines if the user is old enough to get a senior discount
number = age
if number >= 65:
    print("You are eligible to get a senior discount.")
else:
    print("You are not eligible to get a senior discount.")