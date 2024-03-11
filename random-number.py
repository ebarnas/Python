import random

def main():
    try:
        #This generates a random number between 1-100
        actual_number = random.randint(1, 100)
        
        while True:
            #Asks the user to input a guess
            user_guess = int(input("Enter your guess (between 1 and 100): "))
            
            #This calculate the guess from the user to the actual number 
            difference = abs(user_guess - actual_number)
            
            #This will determine if the user's guess is close to the actual number
            if difference <= 5:
                print("Very Hot")
            elif difference <= 15:
                print("Hot")
            elif difference <= 25:
                print("Cool")
            else:
                print("Cold")
            
            #If the user has guessed the actual number, it will congratulate them
            if user_guess == actual_number:
                print("Congratulations! You guessed the correct number.")
                break
                
    except ValueError:
        print("Invalid input. Please enter a valid number.")
main()