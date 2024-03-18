def main():
    #This asks the user for a book title, and uses a counter to count to 10 titles
    titles = []
    print("Please enter 10 book titles:")
    count = 0
    while count < 10:
        title = input(f"Enter title {count + 1}: ")
        titles.append(title)
        count += 1
    
    #This sorts the titles into a list
    sorted_titles = sorted(titles)
    
    #This displays the titles
    print("\nSorted Book Titles:")
    for title in sorted_titles:
        print(title)

main()