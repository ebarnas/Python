#Creates the list for names
def bubble_sort(name_list):
    n = len(name_list)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if name_list[j] > name_list[j + 1]:
                name_list[j], name_list[j + 1] = name_list[j + 1], name_list[j]

#Asks the user for five names
names = []
for _ in range(5):
    name = input("Enter a name: ")
    names.append(name)

#Sorts the list in ascending order
bubble_sort(names)

#Preps the list to be reversed
names.reverse()

#Prints the list in reversed order
print("Final reversed list:", names)