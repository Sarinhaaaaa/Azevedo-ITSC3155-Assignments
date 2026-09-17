import random

# VIOLATION: KISS (Keep It Simple, Stupid) - Unnecessary variables
spotonepoints = 1
spottwopoints = 2
spotthreepoints = 3
spotfourpoints = 4
spotfivepoints = 5
spotsixpoints = 6
spotsevenpoints = 7
spoteightpoints = 8
spotninepoints = 9
spottenpoints = 10
spotelevenpoints = 11
spottwelvepoints = 12
spotthirteenpoints = 13
spotfourteenpoints = 14
spotfifteenpoints = 15
spotsixteenpoints = 16
spotseventeenpoints = 17
spoteighteenpoints = 18
spotnineteenpoints = 19
spottwentypoints = 20

spots = {1: '0', 2: '0', 3: '0', 4: '0', 5: '0',
         6: '0', 7: '0', 8: '0', 9: '0', 10: '0',
         11: '0', 12: '0', 13: '0', 14: '0', 15: '0',
         16: '0', 17: '0', 18: '0', 19: '0', 20: '0'}


# FUNCTION 1
def draw_board(spots):
    board = (f"|{spots[1]}|{spots[2]}|{spots[3]}|{spots[4]}|\n"
             f"|{spots[5]}|{spots[6]}|{spots[7]}|{spots[8]}|\n"
             f"|{spots[9]}|{spots[10]}|{spots[11]}|{spots[12]}|\n"
             f"|{spots[13]}|{spots[14]}|{spots[15]}|{spots[16]}|\n"
             f"|{spots[17]}|{spots[18]}|{spots[19]}|{spots[20]}|")
    return board


# FUNCTION 2
def place_bombs():
    # VIOLATION: Repeating random.randint instead of a loop
    one = random.randint(1, 20)
    spots[one] = "0"

    two = random.randint(1, 20)
    spots[two] = "0"

    three = random.randint(1, 20)
    spots[three] = "0"

    return one, two, three


# FUNCTION 3
def play_game(one, two, three):
    score = 0
    playing = True

    # VIOLATION: DRY (Don't Repeat Yourself) - Giant if/elif chain doing the same thing
    while playing:
        choice = int(input("Enter a spot (1-20): "))
        print(draw_board(spots))
        if choice == one or choice == two or choice == three:
            playing = False
            print("Woops! You hit a bomb ૮ ⸝⸝o̴̶̷᷄ ·̭ o̴̶̷̥᷅⸝⸝  ྀིა")
            print(draw_board(spots))
            print(f"Final Score: {score}")
            break
        elif choice == 1:
            spots[1] = "-"
            print(" ")
            print("૮꒰˶ᵔ ᗜ ᵔ˶꒱ა˖⁺‧₊˚")
            print(draw_board(spots))
            print("Safe!")
            score += spotonepoints
            print(f"Current score: {score}")
        elif choice == 2:
            spots[2] = "-"
            print(" ")
            print("૮꒰ ˶• ༝ •˶꒱ა ♡")
            print(draw_board(spots))
            print("Safe!")
            score += spottwopoints
            print(f"Current score: {score}")
        elif choice == 3:
            spots[3] = "-"
            print(" ")
            print("Pick another spot!")
            print(draw_board(spots))
            print("ദ്ദി(˵ •̀ ᴗ - ˵ ) ✧")
            score += spotthreepoints
            print(f"Current score: {score}")
        elif choice == 4:
            spots[4] = "-"
            print(" ")
            print("૮꒰˶ᵔ ᗜ ᵔ˶꒱ა")
            print(draw_board(spots))
            print("Safe!")
            score += spotfourpoints
            print(f"Current score: {score}")
        elif choice == 5:
            spots[5] = "-"
            print(" ")
            print("≽^•⩊•^≼")
            print(draw_board(spots))
            print("Safe!")
            score += spotfivepoints
            print(f"Current score: {score}")
        elif choice == 6:
            spots[6] = "-"
            print(" ")
            print("૮꒰ ˶꒦ິ꒳꒦ິ˶꒱ა♡")
            print(draw_board(spots))
            print("Safe!")
            score += spotsixpoints
            print(f"Current score: {score}")
        elif choice == 7:
            spots[7] = "-"
            print(" ")
            print("ฅ^>⩊<^ ฅ")
            print(draw_board(spots))
            print("Safe!")
            score += spotsevenpoints
            print(f"Current score: {score}")
        elif choice == 8:
            spots[8] = "-"
            print(" ")
            print("٩(^ᗜ^ )و♡")
            print(draw_board(spots))
            print("Safe!")
            score += spoteightpoints
            print(f"Current score: {score}")
        elif choice == 9:
            spots[9] = "-"
            print(" ")
            print("૮꒰ ˶• ༝ •˶꒱ა ♡")
            print(draw_board(spots))
            print("Safe!")
            score += spotninepoints
            print(f"Current score: {score}")
        elif choice == 10:
            spots[10] = "-"
            print(" ")
            print("( ๑ ˃̵ᴗ˂̵)و ♡")
            print(draw_board(spots))
            print("Safe!")
            score += spottenpoints
            print(f"Current score: {score}")
        elif choice == 11:
            spots[11] = "-"
            print(" ")
            print("ദ്ദി(ᵔᗜᵔ)")
            print(draw_board(spots))
            print("Safe!")
            score += spotelevenpoints
            print(f"Current score: {score}")
        elif choice == 12:
            spots[12] = "-"
            print(" ")
            print("(づ๑•ᴗ•๑)づ♡")
            print(draw_board(spots))
            print("Safe!")
            score += spottwelvepoints
            print(f"Current score: {score}")
        elif choice == 13:
            spots[13] = "-"
            print(" ")
            print("(ෆ˙ᵕ˙ෆ)♡")
            print(draw_board(spots))
            print("Safe!")
            score += spotthirteenpoints
            print(f"Current score: {score}")
        elif choice == 14:
            spots[14] = "-"
            print(" ")
            print("໒꒰ྀིᵔ ᵕ ᵔ ꒱ྀི১")
            print(draw_board(spots))
            print("Safe!")
            score += spotfourteenpoints
            print(f"Current score: {score}")
        elif choice == 15:
            spots[15] = "-"
            print(" ")
            print("૮꒰ ˶• ༝ •˶꒱ა ♡")
            print(draw_board(spots))
            print("Safe!")
            score += spotfifteenpoints
            print(f"Current score: {score}")
        elif choice == 16:
            spots[16] = "-"
            print(" ")
            print("૮꒰ ˶• ༝ •˶꒱ა ♡")
            print(draw_board(spots))
            print("Safe!")
            score += spotsixteenpoints
            print(f"Current score: {score}")
        elif choice == 17:
            spots[17] = "-"
            print(" ")
            print("ദ്ദി ˉ͈̀꒳ˉ͈́ )✧")
            print(draw_board(spots))
            print("Safe!")
            score += spotseventeenpoints
            print(f"Current score: {score}")
        elif choice == 18:
            spots[18] = "-"
            print(" ")
            print("ᓚ₍⑅^..^₎♡")
            print(draw_board(spots))
            print("Safe!")
            score += spoteighteenpoints
            print(f"Current score: {score}")
        elif choice == 19:
            spots[19] = "-"
            print(" ")
            print("໒꒰ྀིづ˶•༝•˶꒱ྀི১づ")
            print(draw_board(spots))
            print("Safe!")
            score += spotnineteenpoints
            print(f"Current score: {score}")
        elif choice == 20:
            spots[20] = "-"
            print(" ")
            print("૮꒰˶ᵔ ᵕ ᵔ˶꒱ა˖⁺‧₊˚")
            print(draw_board(spots))
            print("Safe!")
            score += spottwentypoints
            print(f"Current score: {score}")


# Start the game
welcome = input("Welcome! Type 'Start' to begin: ")
bomb1, bomb2, bomb3 = place_bombs()
print(draw_board(spots))
print(" ")
play_game(bomb1, bomb2, bomb3)