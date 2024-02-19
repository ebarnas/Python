#This creates the time slots for the heart rate
time_slots = ["Morning", "Midday", "Afternoon", "Evening"]

#An empty, receiving list for heart rates on the time slots
heart_rates = []

#Asks the user for their heart rate
for time_slot in time_slots:
    while True:
        try:
            heart_rate = int(input(f"Enter your heart rate for {time_slot} (beats per minute): "))
            break
        except ValueError:
            print("Invalid input. Please enter a valid integer for heart rate.")

    #This will append the time slot and heart rate together
    heart_rates.append([time_slot, heart_rate])

#This calculates the average heart rate and the total heart rate
total_heart_rate = sum(rate[1] for rate in heart_rates)
average_heart_rate = total_heart_rate / len(heart_rates)

#This will display the heart rate
print("\nHeart Rate Data:")
for time_slot, rate in heart_rates:
    print(f"{time_slot}: {rate} bpm")

#This will display the average of the heart rate
print(f"\nAverage Heart Rate: {average_heart_rate:.2f} bpm")