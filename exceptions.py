def square_number():
    while True:
        try:
            #Asks the user to input a number
            number = input("Enter a number to square: ")

            #This will convert the user input into a integer
            number = int(number)

            #This squares the integer
            squared_number = number ** 2

            #This will print the result
            print(f"The square of {number} is {squared_number}.")
        except ValueError:
            #If the user does not input a number, it will ask to re-enter another one
            print("Invalid input. Please enter a valid number.")
square_number()