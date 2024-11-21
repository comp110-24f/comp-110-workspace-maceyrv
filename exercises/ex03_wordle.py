__author__: str = "730715418"

""" Coding Wordle the Game """

def input_guess(length: int) -> str:
    """Asks the user to input a guess of the correct length."""
    guess = input(f"Enter a {length} character word: ")  

    # Keep asking until the guess matches the length of the secret word.
    while len(guess) != length:
        guess = input(f"That wasn't {length} chars! Try again: ")  

    return guess  # Return the valid guess

def contains_char(secret_word: str, char_guess: str) -> bool:
    """Check if the character exists in the secret word"""
    assert len(char_guess) == 1 # Makes sure that char_guess is exactly one character

    # Check if char_guess is in secret_word
    for char in secret_word:
        if char == char_guess:
            return True
    return False

def emojified(guess: str, secret: str) -> str:
    assert len(guess) == len(secret)  # Checks if both words are of equal length

    # Define emoji constants
    WHITE_BOX: str = "\U00002B1C" 
    GREEN_BOX: str = "\U0001F7E9"  
    YELLOW_BOX: str = "\U0001F7E8"  


    emoji_result = ""
    
    for i in range(len(guess)):
        if guess[i] == secret[i]:
            emoji_result += GREEN_BOX  
        elif contains_char(secret, guess[i]):
            emoji_result += YELLOW_BOX 
        else:
            emoji_result += WHITE_BOX  

    return emoji_result

def main(secret: str) -> None:
    # Number of turns user has to guess the word
    turns: int = 1
    won: bool = False

    # Game loop
    while turns <= 6 and won is False: # Only allow 6 turns
        print(f"=== Turn {turns}/6 ===")
        guess = input_guess(len(secret))
        
        # Display the emoji result of the guess
        emoji_result = emojified(guess, secret)
        print(emoji_result)

        if guess == secret:
            won = True
            print(f"You won in {turns} /6 turns!")
        turns = turns + 1 

    if won is False:
        print(f"X/6 - Sorry, try again tomorrow!")

if __name__ == "__main__":
    main(secret="codes")


