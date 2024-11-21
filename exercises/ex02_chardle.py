"""EX02 - Chardle - A cute step toward Wordle."""

__author__: str = "730715418" 

import sys  # Import the sys module to use sys.exit()

def input_word() -> str:
    word = input("Enter a 5-character word: ")
    
    if len(word) != 5:
            print("Error: Word must contain 5 characters.")
            sys.exit()  # Exit if the word length is invalid
            return input_word()
    return word


def input_letter() -> str:
    """Prompt user for a single character."""
    character = input("Enter a single character: ")

    if len(character) != 1:
        print("Error: Character must be a single character.")
        sys.exit()  # Exit if the letter length is invalid
        return input_letter()
    return character


def contains_char(word: str, character: str) -> None: 
    """Checks if the guessed letter is in the word at any index"""

    print("Searching for", character, "in", word)

    count = 0  # Initialize count of letter matches
    # Manually check each of the 5 indices (0 through 4)
    for index in range(5):
        if word[index] == character:
            print(character, "found at index", index)
            count += 1

    # Print the results based on the number of matches found
    if count == 0:
        print("No instances of", character, "found in", word)
    elif count == 1:
        print("1 instance of", character, "found in", word)
    else:
        print(count, "instances of", character, "found in", word)


def main() -> None:
    """Main function to run the Chardle game."""
    word = input_word()
    character = input_letter()
    contains_char(word, character)

# Run the main function
if __name__ == "__main__":
    main()