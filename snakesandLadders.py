# first step we want one board  for testing we choose 3*3 grid
# next we have to implement snakes and ladders
# snakes - will decrease our index
# ladder - increase our index
# next game play when we got 1
# if we reach the end of the grid display win!
board = {1: "1", 2: "2", 3: "3", 4: "4", 5: "5", 6: "6", 7: "7", 8: "8", 9: "9"}
import random
import time


def print_board(board):
    print(board[7] + " | " + board[8] + " | " + board[9] + " |")
    print("--+--+--+--")
    print(board[4] + " | " + board[5] + " | " + board[6] + " |")
    print("--+--+--+--")
    print(board[1] + " | " + board[2] + " | " + board[3] + " |")
    print("--+--+--+--")


# print_board(board)


def snakesandLadders():
    snakes = set(random.randint(2, 8) for i in range(2))
    ladders = set(random.randint(2, 8) for i in range(2))
    if invalidsnakesandLadders(snakes, ladders) == True:
        snakesandLadders()
    else:
        return tuple(snakes), tuple(ladders)


def invalidsnakesandLadders(snakes, ladders):
    if len(snakes.intersection(ladders)) > 0:
        return True
    else:
        return False


def checkisSnakes(move, snakes):

    for snake in snakes:
        if move == snake:
            return True
        else:
            return False


def checkisLadders(move, ladders):

    for ladder in ladders:
        if move == ladder:
            return True
        else:
            return False


def game(board):
    print("   Snakes🐍 And Cyclones🌀      ")
    playerMarker = "O"
    print_board(board)
    try:
        snakes, ladders = snakesandLadders()
        print(snakes)
        print(ladders)
    except:
        snakes = (4, 7)
        ladders = (3, 5)
    while True:
        print("_______________________")
        summa = input(f" {playerMarker}'s Turn.. move the dice🎲 by pressing any key:")
        move = random.randint(1, 4)
        time.sleep(1)
        print(f" your Dice🎯 Value Is:{move}")
        try:
            for key, value in board.items():
                if value == playerMarker:
                    position = key
                    board[key] = str(key)
            move = position + move
            board[move] = playerMarker
        except:
            board[move] = playerMarker
        print("------------------")
        print_board(board)
        if checkisSnakes(move, snakes) == True:
            undo_mov = move
            board[undo_mov] = str(move)
            move = move - 1
            time.sleep(1)
            print("You Got a snake bite🐍...")
            board[move] = playerMarker
            print("____________________________________________")
            print_board(board)
            # playerMarker = "X" if playerMarker == "O" else "O"
        elif checkisLadders(move, ladders) == True:
            undo_mov = move
            board[undo_mov] = str(move)
            move = move + 1
            time.sleep(1)
            print("You Got a Ladder🌀!!!")
            board[move] = playerMarker
            print("____________________________________________")
            print_board(board)
            # playerMarker = "X" if playerMarker == "O" else "O"
        elif move == 9:
            print(f" {playerMarker} is win💥!!! ")
            break
        if playerMarker == "O":
            playerMarker = "X"
        else:
            playerMarker = "O"


def restart(board):
    des = input("Do You Wanna Play Again 👉(yes)or (no)👈:").lower()
    if des == "yes":
        game(board)
    else:
        print("ThankYou for Playing👯!!!...🤹Come Again🧗")


if __name__ == "__main__":
    game(board)
    restart(board)
