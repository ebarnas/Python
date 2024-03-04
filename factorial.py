def factorial(n):
    #N equals to 0 or 1
    if n == 0 or n == 1:
        return 1
    
    else:
        return n * factorial(n - 1)

def main():
    try:
        #Asks the user for a non-negative integer
        user_input = int(input("Enter a non-negative integer: "))

        #Checks if the user inputted a negative integer, if so they must re-enter a non-negative integer
        if user_input < 0:
            print("Please enter a non-negative integer.")
        else:
            #Gets the factorial function from before and inputs into the main function
            result = factorial(user_input)

            #Displays the result
            print(f"The factorial of {user_input} is {result}.")
    except ValueError:
        print("Invalid input. Please enter a non-negative integer.")
main()
