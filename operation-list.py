#This displays what kind of seats are available
def display_available_seats(seats):
    print("Available seats: ", seats)

#This will sell the seats to the user
#If the user tries to buy a seat that they already bought
#It will state that it is no longer available
def sell_ticket(seats):
    while True:
        display_available_seats(seats)
        selected_seat = input("Enter the seat number you want to purchase (enter '0' to finish): ")

        if selected_seat == '0':
            break

        try:
            seat_number = int(selected_seat)
            if seat_number in seats:
                print(f"You have purchased seat {seat_number}.")
                seats.remove(seat_number)
            else:
                print("Seat not available. Please choose another seat.")
        except ValueError:
            print("Invalid input. Please enter a valid seat number.")

#This creates the list of how many seats there are
seating_list = list(range(1, 21))

#This is the ticket is is attached to the seat list
sell_ticket(seating_list)