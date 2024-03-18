def main():
#Asks the user to input a single character
    user_input = input("Enter a character: ")
#This is the loop to make sure that the user has inputted 
#exactly one character, and if not it will keep asking
    while len(user_input) != 1:
        print("Please enter exactly one character.")
        user_input = input("Enter a character: ")
#This will convert the single character into its ASCII value
    ascii_value = ord(user_input)
#This will print the value of the single character to ASCII
    print(f"The ASCII value of {user_input} is {ascii_value}")
main()