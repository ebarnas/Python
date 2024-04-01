def main():
    top_artists = ["The Beatles", "Madonna", "Elton John", "Elvis Presley", "Mariah Carey", "Stevie Wonder", "Janet Jackson", "Michael Jackson", "Whitney Houston", "Rihanna"]
    #This will replace the artists with a different one. If the user inputs incorrectly, it will let them know that an error has ocurred. 
    def replace_artist(top_artists):
        try:
            index = int(input("Enter the index of the artist you want to replace: "))
            if index < 0 or index >= len(top_artists):
                raise IndexError
            new_artist = input("Enter the name of the new artist: ")
            top_artists[index] = new_artist
            print("Artist replaced successfully.")
        except (ValueError, IndexError):
            print("An input error occurred.")

    replace_artist(top_artists)

main()