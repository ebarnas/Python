class InvalidInputError(Exception):
    pass

def main():
    while True:
        try:
            user_input = input("Please enter a number: ")
            number = float(user_input)
        except ValueError:
            print("Error: Invalid input. Please enter a valid number.")
        except InvalidInputError as e:
            print(f"Error: {e}")
        else:
            print("Input is valid.")
            break
        finally:
            print("End of program execution.")

if __name__ == "__main__":
    main()