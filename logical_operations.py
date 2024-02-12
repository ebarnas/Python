#Asks the user for two integers which will be used later on
integer = float(input("Input a random integer: "))
integer_two = float(input("Input another random integer: "))

#Compares both numbers to 0 and 100
if integer and integer_two > 0:
    print("Both numbers greater than 0: True")
else:
    print("Both numbers greater than 0: False")

if integer and integer_two > 100:
    print("Both numbers greater than 100: True")
else:
    print("Both numbers greater than 100: False")

#Uses the 'not' command, compares both numbers to each other and the first number to zero
if not integer == integer_two:
    print("They do not equal each other.")
else:
    print("They do equal each other.")

if not integer == 0:
    print("It does not equal 0.")
else:
    print("It does equal to 0.")

#Uses the 'or' command, it will check to see if either number is greater than 10 and if either number is less than 100
if integer <= 100 or integer_two <= 100:
    print("Either number is less than 100?: True")
else:
    print("Either number is not less than 100?: False")

if integer >= 10 or integer_two >= 10:
    print("Either number is greater than 10?: True")
else:
    print("Either number is greater than 10?: False")