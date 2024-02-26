def calculate_interest(principal, rate, time):
    #This calculates the interest rate
    interest = (principal * rate * time) / 100
    
    #This prints out the statement of the interest rate
    print(f"The simple interest for a principal amount of ${principal:,.2f} at an interest rate of {rate}% over a period of {time} years is: ${interest:,.2f}")
    
    #This returns the interest
    return interest

#This is the numbers needed to use to calculate the interest rate
calculate_interest(500, 10, 5)