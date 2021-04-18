# Tic -Tac -Toe game
import os
# creating board
board = ["-","-","-",
         "-","-","-",
         "-","-","-"]

#global variables
player = "X"
play = True
winner = None


def print_board():
    print("\tTic-Tac-Toe : PanditProgrammr.com")
    print("\n\n\t",board[0]+" | "+board[1]+" | "+board[2])
    print("\t",board[3]+" | "+board[4]+" | "+board[5])
    print("\t",board[6]+" | "+board[7]+" | "+board[8])

def check_row():
    global play

    row_1 = board[0] == board[1] == board[2] != "-"
    row_2 = board[3] == board[4] == board[5] != "-"
    row_3 = board[6] == board[7] == board[8] != "-"

    if row_1 or row_2 or row_3:
        play = False
    # returning winner
    if row_1:
        return board[0]
    elif row_2:
        return board[3]
    elif row_3:
        return board[6]
    else:
        return

def check_col():
    global play

    col_1 = board[0] == board[3] == board[6] != "-"
    col_2 = board[1] == board[4] == board[7] != "-"
    col_3 = board[2] == board[5] == board[8] != "-"

    if col_1 or col_2 or col_3:
        play = False
    # returning winner
    if col_1:
        return board[0]
    elif col_2:
        return board[1]
    elif col_3:
        return board[2]
    else:
        return

def check_diagonal():
    global play

    diagonal_1 = board[0] == board[4] == board[8] != "-"
    diagonal_2 = board[6] == board[4] == board[2] != "-"

    if diagonal_1 or diagonal_2:
        play = False
    # returning winner
    if diagonal_1:
        return board[0]
    elif diagonal_2:
        return board[6]
    else:
        return


def check_win():
    global winner
    row_win = check_row()
    col_win = check_col()
    diagonal_win = check_diagonal()

    if row_win:
        winner = row_win
    elif col_win:
        winner = col_win
    elif diagonal_win:
        winner = diagonal_win
    else:
        winner = None
    return


def check_tie():
    global play
    if "-" not in board:
        play = False
    return


def check_game_over():
    check_win()
    check_tie()


def flip_player():
    global player
    if player == "X":
        player = "O"
    elif player == "O":
        player = "X"
    return


def turn(player):
    print("\n\tPlayer ",player,"Turn ")
    position = input("\tChoose position 1-9 ")

    valid_position = False
    while not valid_position:

        while position not in ["1","2","3","4","5","6","7","8","9"]:
            position = input("\tInvalid ! Choose position 1-9 ")

        position = int(position)-1
        if board[position] == "-":
            valid_position = True
        else:
            print("\tPosition Reserved! Enter Again ")

    board[position] = player
    print_board()

def gameEnd():
    if winner == "X" or winner == "O":
        print("\n\t",winner +" Won!\n")
    elif winner == None:
        print("\n\tTie\n")

def PlayGame():
    global play
    while play:
        os.system("cls")
        print_board()
        turn(player)
        check_game_over()
        flip_player()
    gameEnd()

def PlayAgain():
    global player
    player = "X"
    global play
    play= True
    global winner
    winner = None
    global board
    board = ["-", "-", "-",
             "-", "-", "-",
             "-", "-", "-"]
    PlayGame()


#main function
if __name__ == '__main__':
    while True:
        PlayAgain()
        x = input("Do you want to play Again? Y/N ")
        if x == "Y" or x == "y":
            continue
        else:
            break



