"""EX06 - Choose Your Own Adventure."""
__author__ = "730405020"


import random 
player: str = ''
NAMED_CONSTANT: str = "\U0001F601"
points: int = 0


def greet() -> None:
    """Greets player."""
    global player 
    player = input("Hi, what is your name? ")
    print(f"{player}, welcome!")


def cust_proc() -> None:
    """Runs the coin toss part of the game."""
    global points 
    doub_coin: list[str] = ["Heads", "Tails"]
    coin_toss: str = random.choice(doub_coin)
    choice: str = input(f"{player}, do you choose Heads or Tails? ")
    if choice == coin_toss:
        points += 1
        print(f"{player}, thats correct! You have {str(points)} point(s). ")
    else:
        print(f"{player}, thats incorrect. You have {str(points)} point(s). ")


def cust_funct(points: int) -> int:
    """Runs the dice roll part of the game."""
    dice: list[int] = [1, 2, 3, 4, 5, 6]
    dice_roll: int = random.choice(dice)
    choice: str = input(f"{player}, do you choose 1, 2, 3, 4, 5, or 6? ")
    if choice == str(dice_roll):
        points == points * 2
        print(f"{player}, thats correct! You have {points} points. ")
    else:
        print(f"{player}, thats incorrect. You have {points} point(s). ")
    return points


def main() -> None:
    """Runs the whole game together."""
    global points
    greet()
    decision: str = input(f"{player}, Type 'coin toss' to guess the outcome of a coin toss (to earn 1 point). Type 'dice roll' to guess the outcome of a dice roll (to double your points). Type 'Quit' to leave the game. ")
    while decision != "Quit":
        if decision == "coin toss":
            cust_proc()
        if decision == "dice roll":
            points = cust_funct(points)
        decision = input(f"{player}, Type 'coin toss' to guess the outcome of a coin toss (to earn 1 point). Type 'dice roll' to guess the outcome of a dice roll (to double your points). Type 'Quit' to leave the game. ")
    if decision == "Quit":
        print(f"Thanks for playing {player} {NAMED_CONSTANT}. You earned {points} point(s).")


if __name__ == "__main__":     
    main()  