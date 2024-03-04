#Global and constant conversion
POUND_TO_KG = 0.453592
INCH_TO_METER = 0.0254

def main():
    #Gets user input for weight
    weight_user = input("Enter your weight in pounds: ")
    
    #Gets user input for height
    height_user = input("Enter your height in inches: ")

    try:
        #Converts input to numerical values
        weight = float(weight_user)
        height = float(height_user)

        #This checks for valid numerical inputs
        if weight <= 0 or height <= 0:
            print("Please enter valid positive values for weight and height.")
            return

        #This convert weight and height to metric units
        weight_kg = weight * POUND_TO_KG
        height_m = height * INCH_TO_METER

        #This is the Calculate BMI
        bmi = weight_kg / (height_m * height_m)

        #This displays the calculated BMI with two decimal places
        print(f"Your BMI is: {bmi:.2f}")

        #This displays what weight category that the user is in based off of the BMI
        if bmi < 18.5:
            print("Category: Underweight")
        elif 18.5 <= bmi < 24.9:
            print("Category: Normal weight")
        elif 25 <= bmi < 29.9:
            print("Category: Overweight")
        else:
            print("Category: Obese")

    except ValueError:
        #This handles invalid inputs with an message to make them re-enter their weight and height
        print("Invalid input. Please enter valid numerical values for weight and height.")
main()