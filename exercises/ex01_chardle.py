"""EX01 - Chardle - A cute step toward Wordle."""
__author__ = "730405020"

word: str = input("Enter a 5-character word: ")
if len(word) < 5: 
    exit("Error: Word must contain 5 characters ")
    
letter: str = input("Enter a single character: ")
if len(letter) != 1:
    exit("Error: Character must be a single character. ")

print("Searching for " + letter + " in " + word)
number_instances: int = 0

if letter == word[0]:
    print(letter + " found at index 0")
    number_instances = number_instances + 1
if letter == word[1]:
    print(letter + " found at index 1")
    number_instances = number_instances + 1
if letter == word[2]:
    print(letter + " found at index 2")
    number_instances = number_instances + 1
if letter == word[3]:
    print(letter + " found at index 3")
    number_instances = number_instances + 1
if letter == word[4]:
    print(letter + " found at index 4")
    number_instances = number_instances + 1
if number_instances == 1:
    print("1 instance of " + letter + " found in " + word)
if number_instances == 0:
    print("No instances of " + letter + " found in " + word)
if number_instances > 1:
    print(str(number_instances) + " instances of " + letter + " found in " + word)
   