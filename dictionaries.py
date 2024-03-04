#This is the phonetic alphabet
def create_nato_alphabet():
    nato_alphabet = {
        'A': 'Alpha', 'B': 'Bravo', 'C': 'Charlie', 'D': 'Delta', 'E': 'Echo',
        'F': 'Foxtrot', 'G': 'Golf', 'H': 'Hotel', 'I': 'India', 'J': 'Juliet',
        'K': 'Kilo', 'L': 'Lima', 'M': 'Mike', 'N': 'November', 'O': 'Oscar',
        'P': 'Papa', 'Q': 'Quebec', 'R': 'Romeo', 'S': 'Sierra', 'T': 'Tango',
        'U': 'Uniform', 'V': 'Victor', 'W': 'Whiskey', 'X': 'X-ray', 'Y': 'Yankee',
        'Z': 'Zulu'
    }
    return nato_alphabet
#This will spell out the word in nato alphabet
def spell_word_with_nato(word, nato_dict):
    for letter in word:
        #This makes sure that the program can handle lowercase and uppercase letters
        uppercase_letter = letter.upper()
        if uppercase_letter in nato_dict:
            print(nato_dict[uppercase_letter])

def main():
    #This makes sure that the nato alphabet function can work in the main function
    nato_alphabet_dict = create_nato_alphabet()

    #This asks the user for a word
    user_input = input("Enter a word: ")

    #This will spell out the inputted word with the nato alphabet
    spell_word_with_nato(user_input, nato_alphabet_dict)
main()