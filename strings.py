def main():
    # Example string
    example_string = "Hello, Python programmers!"
    # TODO: Iterate through the string and print each character
    print("Iterating through the string:")
    for char in example_string:
        print(char)
    # TODO: Find and print the character with the minimum ASCII value in the string
    print("\nCharacter with the minimum ASCII value:")
    min_character = min(example_string)
    print(min_character)
    # TODO: Find and print the character with the maximum ASCII value in the string
    print("\nCharacter with the maximum ASCII value:")
    max_character = max(example_string)
    print(max_character)
    # TODO: Find and print the index of the first occurrence of 'o' in the string
    print("\nIndex of 'o':")
    first_o = example_string.find('o')
    print(first_o)
    # TODO: Convert the string into a list of characters and print the list
    print("\nConverting string to a list of characters:")
    character_list = list(example_string)
    print(character_list)
    # TODO: Count and print the number of occurrences of 'o' in the string
    print("\nCount of 'o' in the string:")
    o_count = example_string.count('o')
    print(o_count)
main()
