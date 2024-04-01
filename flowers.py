def main():
    #This is the list for naming flowers
    flower_list = []
    while True:
        flower = input("Enter a flower name (or 'done' to finish): ")
        if flower.lower() == 'done':
            break
        flower_list.append(flower)
    
    if not flower_list:
        print("No flowers entered.")
        return
    #This will sort the flowers in order
    flower_list.sort()
    for i, flower in enumerate(flower_list, 1):
        print(f"{i}. {flower}")
    #This will search for the certain flower that the user has asked for in the list
    search_flower = input("Enter a flower to search for: ")
    if search_flower in flower_list:
        print(f"{search_flower} found in the list.")
    else:
        print(f"{search_flower} not found in the list.")
    #This will access the list to show the flower that the user has asked for via using numbers
    try:
        flower_index = int(input("Enter the number of the flower you want to access: "))
        if flower_index < 1 or flower_index > len(flower_list):
            print("Invalid input. Please enter a number within the range.")
        else:
            print(f"Selected flower: {flower_list[flower_index - 1]}")
    except ValueError:
        print("Invalid input. Please enter a valid number.")
    except IndexError:
        print("Invalid input. The number is out of range.")
    except:
        print("An error occurred.")

main()