def two_letter_combinations(characters):
    #This will make sure that the generated letters are combined together
    for char1 in characters:  
        for char2 in characters:  
            yield char1 + char2  

def main():
    #This will generate the letters and then combine them together in a pair
    characters = ['a', 'b', 'c', 'd', 'e']  
    for combination in two_letter_combinations(characters):
        print(combination)

if __name__ == "__main__":
    main()