"""EX06 - Choose Your Own Adventure."""
__author__ = "730405020"

name: str 
def greet() -> None:
    global name 
    name = input("Hi, what is your name? ")

points: int = 0

import random 

def cust_proc() -> None:
    global points 
    doub_coin: list[str] = ["Heads", "Tails"]
    coin_toss: str = random.choice(doub_coin)
    choice = input(f"{name}, do you choose Heads or Tails? ")
    if choice == coin_toss:
        points = points + 1
        print(f"{name}, thats correct! You have {points} point(s). ")
    else:
        print(f"{name}, thats incorrect. You have {points} point(s). ")

def cust_funct(points: int) -> int:
    dice: list[int] = [1, 2, 3, 4, 5, 6]
    dice_roll: int = random.choice(dice)
    choice = input(f"{name}, do you choose 1, 2, 3, 4, 5, or 6? ")
    if choice == dice_roll:
        points == points * 2
        print(f"{name}, thats correct! You have {points} points. ")
    else:
        print(f"{name}, thats incorrect. You have {points} point(s). ")
    return points

NAMED_CONSTANT: str = "\U0001F601"

def main() -> None:
    global points
    greet()
    decision = input(f"{name}, Type 'coin toss' to guess the outcome of a coin toss (to earn 1 point). Type 'dice roll' to guess the outcome of a dice roll (to double your points). Type 'Quit' to leave the game. ")
    while decision != "Quit":
        if decision == "coin toss":
            cust_proc()
        if decision == "dice roll":
            points = cust_funct(points)
        decision = input(f"{name}, Type 'coin toss' to guess the outcome of a coin toss (to earn 1 point). Type 'dice roll' to guess the outcome of a dice roll (to double your points). Type 'Quit' to leave the game. ")
    if decision == "Quit":
        print(f"Thanks for playing {name} {NAMED_CONSTANT}. You earned {points} point(s).")

if __name__ == "__main__":     
    main()  