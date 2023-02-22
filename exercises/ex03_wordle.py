"""EX03 - Wordle."""
__author__ = "730405020"

def contains_char(secret: str, letter: str) -> bool:
    """Checks to see if secret word has the guessed character."""
    assert len(letter) == 1
    index: int = 0
    while index < len(secret):
        if letter == secret[index]:
            return True
        index += 1
    return False

def emojified(guess: str, secret: str) -> str:
    """Returns string of emoji coding for the guessed word."""
    assert len(guess) == len(secret)
    index: int = 0
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    results: str = ""
    while index < len(secret):
        if guess[index] == secret[index]:
            results = results + GREEN_BOX
        else:
            if contains_char(secret, guess[index]):
                results = results + YELLOW_BOX
            else:
                results = results + WHITE_BOX
        index = index + 1
    return results

def input_guess(length: int) -> str:
    """Prompts user for a guess and continues prompting until expected length is met."""
    guess = input(f"Enter a {length} character word: ")
    while len(guess) != length: 
        guess = input(f"That wasn't {length} chars! Try again: ")
    if len(guess) == length:
        return guess

def main() -> None:
    """The entrypoint of the program and main game loop."""
    secret: str = "codes"
    length: int = len(secret)
    turn: int = 1
    check: bool = True 
    while turn < 7 and check:
        print(f"=== Turn {turn}/6 ===")
        guess: str = input_guess(len(secret))
        print(emojified(guess, secret))
        if guess == secret:
            check = False
        turn = turn + 1
    if check is False:
        print(f"You won in {turn - 1}/6 turns!")
    else:
        print("X/6 - Sorry, try again tomorrow!")


if __name__ == "__main__":     
    main()