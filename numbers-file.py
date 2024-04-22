def main():
    total = 0.0
    count = 0

    try:
        with open("sales_totals.txt", "r") as file:
            for line in file:
                try:
                    number = float(line.strip())  #This will convert each line to a float
                    total += number  #This will add each number to the running total
                    count += 1  #This increases the count by 1
                    print("{:.2f}".format(number))  #This will format the number and print it out
                except ValueError:
                    print("Error: Could not convert '{}' to a float".format(line.strip()))
    except FileNotFoundError:
        print("Error: File not found")

    if count > 0:
        average = total / count
        print("\nTotal: {:.2f}".format(total))
        print("Count: {}".format(count))
        print("Average: {:.2f}".format(average))

if __name__ == "__main__":
    main()