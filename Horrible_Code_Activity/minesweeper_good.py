import random

# A list of kaomojis to randomly select from, eliminating the need for 20 print statements.
KAOMOJIS = [
    "૮꒰˶ᵔ ᗜ ᵔ˶꒱ა˖⁺‧₊˚", "૮꒰ ˶• ༝ •˶꒱ა ♡", "ദ്ദി(˵ •̀ ᴗ - ˵ ) ✧",
    "≽^•⩊•^≼", "ฅ^>⩊<^ ฅ", "٩(^ᗜ^ )و♡", "( ๑ ˃̵ᴗ˂̵)و ♡",
    "ദ്ദി(ᵔᗜᵔ)", "(ෆ˙ᵕ˙ෆ)♡", "໒꒰ྀིᵔ ᵕ ᵔ ꒱ྀི১", "ᓚ₍⑅^..^₎♡"
]


def create_board():
    """Initializes a dictionary with 20 spots set to '0'."""
    # KISS Principle Demonstration: Dictionary comprehension replaces typing 20 manual key-value pairs.
    return {i: '0' for i in range(1, 21)}


def draw_board(spots):
    """Formats and returns the current state of the board."""
    board = (f"|{spots[1]}|{spots[2]}|{spots[3]}|{spots[4]}|\n"
             f"|{spots[5]}|{spots[6]}|{spots[7]}|{spots[8]}|\n"
             f"|{spots[9]}|{spots[10]}|{spots[11]}|{spots[12]}|\n"
             f"|{spots[13]}|{spots[14]}|{spots[15]}|{spots[16]}|\n"
             f"|{spots[17]}|{spots[18]}|{spots[19]}|{spots[20]}|")
    return board


def place_bombs():
    """Returns a list of 3 random bomb locations between 1 and 20."""
    # DRY & KISS Demonstration: random.sample guarantees 3 unique numbers without repeating code.
    return random.sample(range(1, 21), 3)


def play_game():
    """Main game loop handling user input, score tracking, and win/loss conditions."""
    spots = create_board()
    bombs = place_bombs()
    score = 0
    safe_picks = 0  # Tracks how many safe spots the user has found

    input("Welcome! Type 'Start' to begin: ")
    print("\n" + draw_board(spots) + "\n")

    while True:
        try:
            choice = int(input("Enter a spot (1-20): "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        if choice < 1 or choice > 20:
            print("Choice out of range. Pick between 1 and 20.")
            continue

        if spots[choice] == "-":
            print("You already picked that spot! Choose another.")
            continue

        print(draw_board(spots))

        if choice in bombs:
            print("Whoops! You hit a bomb ૮ ⸝⸝o̴̶̷᷄ ·̭ o̴̶̷̥᷅⸝⸝  ྀིა")
            print(draw_board(spots))
            print(f"Final Score: {score}")
            break
        else:
            # DRY Demonstration: All safe choice logic is handled in one block instead of 20 elif statements.
            spots[choice] = "-"
            print("\n" + random.choice(KAOMOJIS))
            print(draw_board(spots))
            print("Safe!")

            # KISS Demonstration: The points awarded equal the spot number itself. No separate variables needed.
            score += choice
            print(f"Current score: {score}")

            # Win Condition: 20 total spots - 3 bombs = 17 safe spots to win
            safe_picks += 1
            if safe_picks == 17:
                print("\n🎉 YOU WIN! You found all 17 safe spots! 🎉")
                print(f"Perfect Final Score: {score}")
                break


# Start the game
if __name__ == "__main__":
    play_game()