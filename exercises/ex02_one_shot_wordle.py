"""EX02 - One Shot Wordle."""
__author__ = "730405020"

guess: str = input("What is your 6-letter guess? ")
word: str = "python"

index: int = 0
guess_length = len(guess)

while guess_length != len(word):
    guess = input(f"That was not {len(word)} letters! Try again: ")
    guess_length = len(guess)

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

results: str = ""

while index < len(word):
    if guess[index] == word[index]:
        results = results + GREEN_BOX
    else: 
        check: bool = False
        index_2: int = 0
        while index_2 < len(word) and not check:
            if guess[index] == word[index_2]:
                results = results + YELLOW_BOX
                check = True
            index_2 = index_2 + 1
        if check == False:
            results = results + WHITE_BOX
    index = index + 1

print(results)

if guess != word:
    print("Not quite. Play again soon!")
if guess == word:
    print("Woo! You got it!")
