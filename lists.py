#This is the list that will hold the days in a week
days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

#This list will store the amount of steps that has been taken in each day
steps = []

#Asks the user how much steps did they take on each day
for day in days:
    how_much = int(input(f"How many steps did you take on {day}? "))
    steps.append(how_much)

#This displayed how many steps the user has taken each day
for i in range(len(days)):
    print(f"{days[i]}: {steps[i]} steps")

#Counts the total steps
total_steps = sum(steps)
print(f"\nTotal steps for the week: {total_steps} steps")

#Averages out the steps
average = round(total_steps / len(steps))
print(f"Average steps per day: {average} steps")