#Asks for your budget
total_budget = float(input("What is your total budget? "))

#Asks for your budget on certain areas
housing_rent = float(input("What is your budget on housing rent? "))
utilities = float(input("What is your budget on utilities? "))
groceries = float(input("What is your budget on groceries? "))
transportation = float(input("What is your budget on transportation? "))
health_care = float(input("What is your budget on health care? "))
personal_care = float(input("What is your budget on personal care? "))
clothing = float(input("What is your budget on clothing? "))
debt = float(input("What is your budget on paying off debt? "))

#Does the math of how much of the certain areas affecting your budget
percent_one = housing_rent / total_budget
percent_two = utilities / total_budget
percent_three = groceries / total_budget
percent_four = transportation / total_budget
percent_five = health_care / total_budget
percent_six = personal_care / total_budget
percent_seven = clothing / total_budget
percent_eight = debt / total_budget

#States the certain areas affecting your budget.
print = "The results you will receive will be in decimal formatted, just move the decimal two spots over to the right to get the percent."
print = "The amount for housing rent being spent into your total budget is" + str(percent_one) + "."
print = "The amount for utilities being spent into your total budget is" + str(percent_two) + "."
print = "The amount for groceries rent being spent into your total budget is" + str(percent_three) + "."
print = "The amount for transportation being spent into your total budget is" + str(percent_four) + "."
print = "The amount for health care being spent into your total budget is" + str(percent_five) + "."
print = "The amount for personal care being spent into your total budget is" + str(percent_six) + "."
print = "The amount for clothing being spent into your total budget is" + str(percent_seven) + "."
print = "The amount for debt being spent into your total budget is" + str(percent_eight) + "."